#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import smtplib

import pika


# 发送邮件到SMTP服务器
def send_mail(recipients, subject, message):
    headers = ("From: %s\r\nTo: \r\nData: \r\nSubject: %s\r\n\r\n") % ("469656844@qq.com", subject)
    smtp_server = smtplib.SMTP()
    smtp_server.connect("mail.ourcompany.com", 25)
    smtp_server.sendmail("469656844@qq.com", recipients, headers + str(message))
    smtp_server.close()


# 通知处理程序
def critical_notify(channel, method, header, body):
    EMAIL_RECIPS = ["ops.team@ourcompany.com", ]
    # 将消息从JSON解码
    message = json.loads(body)
    # send_mail(EMAIL_RECIPS, "CRITICAL ALERT", message)
    print ("Send alert via e-mail! Alert Text: %s  Recipients: %s") % (str(message), str(EMAIL_RECIPS))
    # 确认消息
    channel.basic_ack(delivery_tag=method.delivery_tag)


def rate_limit_notify(channel, method, header, body):
    EMAIL_RECIPS = ["api.team@ourcompany.com"]
    # 将消息从JSON解码
    message = json.loads(body)
    # send_mail(EMAIL_RECIPS, "RATE LIMIT ALERT!", message)
    print ("Send alert via e-mail! Alert Text: %s  Recipients: %s") % (str(message), str(EMAIL_RECIPS))
    # 确认消息
    channel.basic_ack(delivery_tag=method.delivery_tag)


# 代理服务器设置
if __name__ == "__main__":

    # 建立到代理的连接
    creds_broker = pika.PlainCredentials("alert_user", "alertme")
    conn_params = pika.ConnectionParameters("192.168.1.11", virtual_host="/", credentials=creds_broker)
    conn_broker = pika.BlockingConnection(conn_params)
    channel = conn_broker.channel()
    # 声明交换器
    channel.exchange_declare(exchange="alerts", type="topic", auto_delete=False)
    # 构造队列，绑定Topic交换器
    channel.queue_declare(queue="critical", auto_delete=False)
    channel.queue_bind(queue="critical", exchange="alerts", routing_key="critical.*")
    channel.queue_declare(queue="rate_limit", auto_delete=False)
    channel.queue_bind(queue="rate_limit", exchange="alerts", routing_key="*.rate_limit")
    # 设置告警处理程序
    channel.basic_consume(critical_notify, queue="critical", no_ack=False, consumer_tag="critical")
    channel.basic_consume(rate_limit_notify, queue="rate_limit", no_ack=False, consumer_tag="rate_limit")
    print "Ready for alerts!"
    channel.start_consuming()
