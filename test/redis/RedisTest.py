#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import unittest

import redis

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
pool = redis.ConnectionPool(host='192.168.1.10', port=6379)
client = redis.Redis(connection_pool=pool)


def add_data():
    client.set("key-str", "value")
    print client.get("key-str")
    client.hset("key-hash", "key", "value")
    print client.hgetall("key-hash")
    client.lpush("key-list", "value")
    print client.lrange("key-list", 0, 100)
    client.sadd("key-set", "value")
    print client.smembers("key-set")


def operate_string():
    # SET key value                   设置key=value
    print client.set("name", "任欢")
    print client.set("age", 10)
    print client.set("addr", "湖南省常德市")
    print client.set("English_name", "Iritchie.ren")
    print client.set("desc", "Hello, my name is renhuan, I'm come from shenzhen of china!")
    print client.set("expire", "到期时间设置")
    # GET key                         或者键key对应的值
    print client.get("name")
    # GETRANGE key start end          得到字符串的子字符串存放在一个键
    print client.getrange("English_name", 0, 3)
    # GETSET key value                设置键的字符串值，并返回旧值
    print client.getset("name", "Iritchie.ren")
    # GETBIT key offset               返回存储在键位值的字符串值的偏移
    print client.getbit("addr", 2)
    # MGET key1 [key2..]              得到所有的给定键的值
    print client.mget(["age", "name"])
    # SETBIT key offset value         设置或清除该位在存储在键的字符串值偏移
    print client.setbit("addr", 2, "z")
    # SETEX key seconds value         键到期时设置值
    print client.setex("expire", "时间到", 5)
    time.sleep(6)
    client.set("expire", "到期时间设置")
    # SETNX key value                 设置键的值，只有当该键不存在
    print client.setnx("name", "李华")
    # SETRANGE key offset value       覆盖字符串的一部分从指定键的偏移
    print client.setrange("desc", 10, "haha")
    # STRLEN key                      得到存储在键的值的长度
    print client.strlen("name")
    # MSET key value [key value...]   设置多个键和多个值
    print client.mset({"中国": "我的家乡", "湖南": "我的故乡"})
    # MSETNX key value [key value...] 设置多个键多个值，只有在当没有按键的存在时
    # PSETEX key milliseconds value   设置键的毫秒值和到期时间
    print client.psetex("expire", 5, "又一个时间")
    time.sleep(6)
    client.set("expire", "到期时间设置")
    # INCR key                        增加键的整数值一次
    print client.incr("age")
    # INCRBY key increment            由给定的数量递增键的整数值
    print client.incrby("age")
    # INCRBYFLOAT key increment       由给定的数量递增键的浮点值
    print client.incrbyfloat("age")
    # DECR key                        递减键一次的整数值
    print client.decr("age")
    # DECRBY key decrement            由给定数目递减键的整数值
    # APPEND key value                追加值到一个键
    print client.append("name", "努力")
    print client.expire("name", 5)
    time.sleep(6)
    client.set("name", "任欢")


def operate_memory():
    start = time.time()
    print start
    for i in range(0, 100000000):
        client.lpush("list_name", "Hello, my name is renhuan, I'm come from shen zhen of china! " + str(i))
    end = time.time()
    print end
    print end - start


def operate_query_memory():
    start = time.time()
    print start
    print client.lrange("list_name", 0, 10000)
    end = time.time()
    print end
    print end - start


def operate_pop_memory():
    start = time.time()
    print start
    for i in range(0, 100000):
        print client.lpop("list_name")
    end = time.time()
    print end
    print end - start


class Test01(unittest.TestCase):
    # def test_add_data(self):
    #     add_data()

    # def test_operate_string(self):
    #     operate_string()
    #
    # def test_operate_memory(self):
    #     operate_memory()

    # def test_operate_query_memory(self):
    #     operate_query_memory()
    #
    def test_operate_pop_memory(self):
        # client.flushall()
        operate_pop_memory()


if __name__ == '__main__':
    unittest.main
