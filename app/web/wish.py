#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/26 10:21
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/26 10:21
 * @Desc:
"""
from flask import flash, redirect, url_for, current_app, render_template
from flask_login import login_required, current_user

from . import web
from .. import db
from ..models.gift import Gift
from ..models.wish import Wish
from ..view_models.wish import MyWishes


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_wish_counts(isbn_list)
    view_model = MyWishes(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.gifts)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            db.session.add(gift)
    else:
        flash('这本书已经添加至心愿清单或者已经存在，不允许重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))