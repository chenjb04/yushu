#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/26 21:56
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/26 21:56
 * @Desc:
"""


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(i) for i in goods]

    @staticmethod
    def __map_to_trade(singel):
        if singel.create_datetime:
            time = singel.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=singel.user.nickname,
            time=time,
            id=singel.id
        )
