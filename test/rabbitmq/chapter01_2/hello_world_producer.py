#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pika

credentials = pika.PlainCredentials("guest", "guest")
# 建立连接
conn_params = pika.ConnectionParameters("192.168.105.10", credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)
# 获取信道
channel = conn_broker.channel()
# 声明交换器
channel.exchange_declare(exchange="hello-exchange", type="direct", passive=False, durable=True, auto_delete=False)
channel.queue_declare("hello-queue")
# 通过键将队列和交换器绑定起来
channel.queue_bind(queue="hello-queue", exchange="hello-exchange", routing_key="hola")
# 创建纯文本消息
# msg = sys.argv[1]
msg = "hello world! 你好，中国！"
msg_props = pika.BasicProperties()
msg_props.conn_type = "text/plain"
# 发布消息
for i in range(1000000):
    channel.basic_publish(body=msg, exchange="hello-exchange", properties=msg_props, routing_key="hola")
