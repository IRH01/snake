#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
import thread
import time
import traceback

import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')


def log_uncaught_exceptions(exception_type, exception, tb):
    logging.critical(''.join(traceback.format_tb(tb)))
    logging.critical('{0}: {1}'.format(exception_type, exception))


sys.excepthook = log_uncaught_exceptions

# 网关地址
addr = '192.168.105.66'
port = 8150
restful = '/gj/order/details'
token = 'auc_jsession_33d8749702b0a7732b3003648a95596b1abb2754'
params = 'params={"orderNo":"XX20161128191631853904708"}'
thread_count = 500  # 单次并发数量
requst_interval = 1  # 请求间隔(秒)
test_count = sys.maxsize  # sys.maxsize  # 指定测试次数

# 字段说明,必须一一对应
# login为空表示使用随机用户名

now_count = 0
lock_obj = thread.allocate()


def send_http():
    global now_count
    try:
        url = 'http://' + addr + ':' + str(port) + restful + '?token=' + token + '&' + params
        response = requests.get(url)

        print '发送数据: ' + url
        print '返回码: ' + str(response.status_code)
        print '返回数据: ' + response.content

        logging.info('发送数据: ' + url)
        logging.info('返回码: ' + str(response.status_code))
        logging.info('返回数据: ' + response.content)
        sys.stdout.flush()
        now_count += 1
    except Exception, e:
        print e
        logging.info(e)


def test_func(run_count):
    global now_count
    global requst_interval
    global lock_obj
    cnt = 0
    while cnt < run_count:
        lock_obj.acquire()
        print ''
        print '***************************请求次数:' + str(now_count) + '*******************************'
        print 'Thread:(%d) Time:%s\n' % (thread.get_ident(), time.ctime())

        logging.info(' ')
        logging.info('***************************请求次数:' + str(now_count) + '*******************************')
        logging.info('Thread:(%d) Time:%s\n' % (thread.get_ident(), time.ctime()))
        cnt += 1
        send_http()
        sys.stdout.flush()
        lock_obj.release()
        time.sleep(requst_interval)


def test(ct):
    global thread_count
    for i in range(thread_count):
        thread.start_new_thread(test_func, (ct,))


if __name__ == '__main__':
    global test_count
    test(test_count)
    while True:
        time.sleep(100)
