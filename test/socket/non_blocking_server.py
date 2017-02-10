#!/usr/bin/env python
# coding=utf8

import socket
import time

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP socket对象,
sk.setsockopt
sk.bind(('127.0.0.1', 6666))  # 设置监听的IP与端口
sk.listen(5)  # 设置client最大等待连接数
sk.setblocking(False)  # 这里设置setblocking为Falseaccept将不在阻塞，但是如果没有收到请求就会报错
while True:  # 循环
    try:
        print('waiting client connection .......')
        # accept()接受客户端发送过来的请求:connection代表客户端对象，address是客户端的IP
        connection, address = sk.accept()
        # recv()接收客户端信息
        client_messge = connection.recv(1024)
        # 打印客户端信息
        print('client send %s' % client_messge)
        # 发送回执信息给client
        connection.sendall(bytes('僵尸吃了你的脑子!!!', encoding='utf-8'))
        # connection.send()
        # 关闭和client的连接
        connection.close()
    except Exception as error:
        print(error)
    time.sleep(4)
