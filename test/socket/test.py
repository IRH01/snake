#!/usr/bin/env python
# coding=utf8
import socket

sk = socket.socket()  # 创建socket对象
sk.setsockopt
sk.bind(('127.0.0.1', 6666))  # 设置监听的IP与端口
sk.listen(5)  # 设置client最大等待连接数
sk.setblocking(False)  # 这里设置setblocking为Falseaccept将不在阻塞，但是如果没有收到请求就会报错
