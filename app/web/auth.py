#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/26 10:21
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/26 10:21
 * @Desc:
"""
from flask import render_template, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user

from . import web
from .. import db
from ..forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from ..models.user import User
from app.libs.email import send_email


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账户不存在或者密码错误')

    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            send_email(form.email.data, '重置你的密码', 'email/reset_password.html', user=user, token=user.generate_token())
    return render_template('auth/forget_password_request.html', form=form)


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@web.route('/reset/password/<token>', methods=['POST', 'GET'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash('密码已经更新')
            return redirect(url_for('web.login'))
        else:
            flash('密码失败')
    return render_template('auth/forget_password.html', form=form)