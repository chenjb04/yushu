#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/12 21:17
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/12 21:17
 * @Desc:
"""


def is_isbn_or_key(word: str) -> str:
    """
    判断搜索关键词是isbn 还是普通关键词
    isbn类型 1.13个0-9数字  2.10个0-9数字，中间含有‘-’
    :param word: 关键词
    :return: string
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key