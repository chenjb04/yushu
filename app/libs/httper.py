#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/12 21:28
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/12 21:28
 * @Desc:
"""
import requests


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        res = requests.get(url)
        if res.status_code != 200:
            return {} if return_json else ''
        return res.json() if return_json else res.text