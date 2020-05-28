#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/12 22:05
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/12 22:05
 * @Desc:
"""
from flask import Blueprint, render_template

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from app.web import book
from app.web import auth
from app.web import drift
from app.web import wish
from app.web import main
from app.web import gift
