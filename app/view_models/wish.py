#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/27 10:47
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/27 10:47
 * @Desc:
"""
from collections import namedtuple

from app.view_models.book import BookViewModel

MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyWishes:
    def __init__(self, gift_of_mine, wish_count_list):
        self.gifts = []
        self.__gift_of_mine = gift_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gift_of_mine:
            my_gift = self.__machting(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __machting(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        return my_gift
# class MyGift:
#     def __init__(self):
