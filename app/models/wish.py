#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/26 16:57
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/26 16:57
 * @Desc:
"""
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(
            uid=uid, launched=False).order_by(
            desc(
                Wish.create_time)).all()
        return wishes

    @classmethod
    def get_wish_counts(cls, isbn_list):
        count_list = db.session.query(
            func.count(Gift.id),
            Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == '1').group_by(
            Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

from app.models.gift import Gift