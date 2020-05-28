#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/26 10:21
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/26 10:21
 * @Desc:
"""
from flask import render_template

from . import web
from ..models.gift import Gift
from ..view_models.book import BookViewModel


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', books=books)


@web.route('/personal')
def personal_center():
    pass