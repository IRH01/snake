#!/usr/bin/env python
# coding=utf8

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP socket对象,
sk.setsockopt
sk.connect(('127.0.0.1', 6666))
sk.send('你好！')
