#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import pika

# ./rabbitmqctl add_user rpc_user rpcme
# ./rabbitmqctl set_permissions rpc_user '.*' '.*' '.*'
creds_broker = pika.PlainCredentials("rpc_user", "rpcme")
conn_params = pika.ConnectionParameters("192.168.1.11", virtual_host="/", credentials=creds_broker)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
channel.exchange_declare(exchange="rpc", type="direct", auto_delete=False)
channel.queue_declare(queue="ping", auto_delete=False)
channel.queue_bind(queue="ping", exchange="rpc", routing_key="ping")


def api_ping(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    msg_dict = json.loads(body)
    print "Received API call ... replying..."
    channel.basic_publish(body="Pong!" + str(msg_dict["time"]), exchange="", routing_key=header.reply_to)


channel.basic_consume(api_ping, queue="ping", consumer_tag="ping")
print "Waiting for RPC calls..."
channel.start_consuming()
