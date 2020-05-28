#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/14 10:33
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/14 10:33
 * @Desc:
"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))  # 装订版本 精装 平装
    publisher = Column(String(50))  # 出版社
    price = Column(String(20))
    pages = Column(Integer)  # 页数
    pudate = Column(String(20))  # 出版日期
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))  # 简介
    image = Column(String(50))