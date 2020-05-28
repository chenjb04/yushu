#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/27 14:32
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/27 14:32
 * @Desc:
"""
from flask import current_app, render_template
from flask_mail import Message

from app import mail


def send_email(to, subject, template, **kwargs):
    # msg = Message('测试', sender='2580473897@qq.com', body='Test', recipients=['2580473897@qq.com'])
    msg = Message('[鱼书] ' + subject, sender=current_app.config['MAIL_USERNAME'],  recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
