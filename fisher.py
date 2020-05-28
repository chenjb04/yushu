#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/5/11 20:12
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/5/11 20:12
 * @Desc:
"""
from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)