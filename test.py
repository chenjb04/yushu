#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/21 21:00
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/21 21:00
 * @Desc:
"""
# import threading
# from werkzeug.local import Local
#
#
# obj = Local()
# obj.a = 10
#
#
# def worker1():
#     """线程1"""
#     obj.a = 1
#     print('线程1中的a的值为：{}'.format(obj.a))
#
#
# t1 = threading.Thread(target=worker1, name='线程1')
# t1.start()
# t1.join()
# print('主线程中的a的值为：{}'.format(obj.a))
# import threading
#
# from werkzeug.local import LocalStack
#
#
# ls = LocalStack()
# ls.push(1)
#
#
# def worker1():
#     """线程1"""
#     print('线程1中的栈顶的值为：{}'.format(ls.top))
#     ls.push(2)
#     print('线程1中的栈顶的值为：{}'.format(ls.top))
#
#
# t1 = threading.Thread(target=worker1, name='线程1')
# t1.start()
# t1.join()
# print('主线程中的栈顶的值为：{}'.format(ls.top))


from werkzeug.local import LocalStack, LocalProxy
user_stack = LocalStack()
user_stack.push({'name': 'Bob'})
user_stack.push({'name': 'John'})


def get_user():
    return user_stack.pop()


# 使用 LocalProxy
user = LocalProxy(get_user)
print(user['name'])
print(user['name'])