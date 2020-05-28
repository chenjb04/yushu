#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/13 21:58
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/13 21:58
 * @Desc:
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange,DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
