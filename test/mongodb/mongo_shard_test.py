#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 随即写MongoDB Shard 测试

import time
from random import Random

import pymongo


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
        return str


def inc_data(conn):
    db = conn.dba
    #    db = conn.test
    collection = db.account
    for i in range(1000):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(15):
            str += chars[random.randint(0, length)]
            string = str
        collection.insert({"name": string, "age": 123 + i, "address": "hangzhou" + string})


if __name__ == '__main__':
    conn = pymongo.MongoClient(host='192.168.105.9', port=27016)

    StartTime = time.time()
    print "===============$inc==============="
    print "StartTime : %s" % StartTime
    inc_data(conn)
    EndTime = time.time()
    print "EndTime : %s" % EndTime
    CostTime = round(EndTime - StartTime)
    print "CostTime : %s" % CostTime
