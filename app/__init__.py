#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/12 22:05
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/12 22:05
 * @Desc:
"""
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from app.models.base import db

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    mail.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    """
    蓝图的注册
    :param app: Flask对象实例
    :return:
    """
    from app.web import web
    app.register_blueprint(web)


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    user = db.session.query(User).get(user_id)
    return user