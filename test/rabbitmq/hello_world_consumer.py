#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pika

credentials = pika.PlainCredentials("guest", "guest")
# 建立到代理服务器
conn_params = pika.ConnectionParameters("192.168.1.11", credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)
# 获得信道
channel = conn_broker.channel()
# 声明交换器
channel.exchange_declare(exchange="hello-exchange", type="direct", passive=False, durable=True, auto_delete=False)
# 声明队列
channel.queue_declare("hello-queue")
# 通过键将队列和交换器绑定起来
channel.queue_bind(queue="hello-queue", exchange="hello-exchange", routing_key="hola")


# 用于处理传入消息的函数
def msg_consumer(channel, method, header, body):
    # 消息确认
    channel.basic_ack(delivery_tag=method.delivery_tag)
    # 停止消费并推出
    if body == "quit":
        channel.basic_cancel(consumer_tag="hello-consumer")
        channel.stop_consuming()
    else:
        print body
    return


# 订阅消费者
channel.basic_consume(msg_consumer, queue="hello-queue", consumer_tag="hello-consumer")
# 开始消费
channel.start_consuming()
