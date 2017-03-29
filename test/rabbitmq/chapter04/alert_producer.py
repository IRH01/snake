#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from optparse import OptionParser

import pika

opt_parser = OptionParser()
# 读取命令行参数
opt_parser.add_option("-r", "--routing-key", dest="routing_key", help="routing key Message text for alert")
opt_parser.add_option("-m", "--message", dest="message", help="Message text for alert")
args = opt_parser.parse_args()[0]
# 建立到服务器的连接
creds_broker = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("192.168.105.10", virtual_host="/", credentials=creds_broker)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
# 将告警信息发送给服务器
msg = json.dumps(args.message)
msg_props = pika.BasicProperties()
msg_props.content_type = "application/json"
msg_props.durable = False
channel.basic_publish(body=msg, exchange="alerts", properties=msg_props, routing_key=args.routing_key)
print ("Sent message %s tagged with routing key '%s' to exchange '/'.") % (json.dumps(args.message), args.routing_key)
