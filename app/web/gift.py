#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/26 10:20
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/26 10:20
 * @Desc:
"""
from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from . import web
from .. import db
from ..models.gift import Gift
from ..view_models.gift import MyGifts


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyGifts(gifts_of_mine, wish_count_list)
    return render_template('my_wish.html', gifts=view_model.gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已经添加至心愿清单或者已经存在，不允许重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass