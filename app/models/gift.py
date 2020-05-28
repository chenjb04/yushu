#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/26 11:17
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/26 11:17
 * @Desc:
"""
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship
# from collections import namedtuple

from app.models.base import Base, db
from app.setting import RECENT_BOOK_COUNT
from app.spider.yushu_book import YuShuBook


# EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).order_by(
            desc(Gift.create_time)).limit(RECENT_BOOK_COUNT).distinct().all()
        return recent_gift

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched==False, Wish.isbn.in_(isbn_list), Wish.status == '1').group_by(Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

from app.models.wish import Wish