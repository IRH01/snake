#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pika

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("192.168.1.11", credentials=credentials)

conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()


def confirm_handler(frame):
    if type(frame.method) == pika.spec.Confirm.SelectOk:
        print "channel in 'confirm' mode. "
    elif type(frame.method) == pika.spec.Basic.Nack:
        if frame.method.delivery_tag in msg_ids:
            print "Message lost!"
    elif type(frame.method) == pika.spec.Basic.Ack:
        if frame.method.delivery_tag in msg_ids:
            print "Confirm received!"
            msg_ids.remove(frame.method.delivery_tag)


channel.confirm_delivery(callback=confirm_handler())
# msg = sys.argv[1]
msg = "abc"
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
msg_ids = []
channel.basic_publish(body=msg, exchange="hello-exchange", property=msg_props, routing_key="hola")
msg_ids.append(len(msg_ids) + 1)
channel.close()
