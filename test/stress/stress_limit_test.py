#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import random
import sys
import thread
import time
import traceback

import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test_limit.log',
                    filemode='w')


def log_uncaught_exceptions(exception_type, exception, tb):
    logging.critical(''.join(traceback.format_tb(tb)))
    logging.critical('{0}: {1}'.format(exception_type, exception))


sys.excepthook = log_uncaught_exceptions

# 网关地址
addr = '172.16.1.135'
port = str(8150)
uri = '/activity/test.do'
token = 'auc_jsession_306995609284b36213c1008c0c36a8c879b99de4'
params = 'sysType=2&activityId=1039&num=1'
thread_count = 500  # 单次并发数量
requst_interval = 0  # 请求间隔(秒)
test_count = sys.maxsize  # sys.maxsize  # 指定测试次数
user_list = [10001, 10002, 10003, 10004, 10005.10006, 10007, 10008, 10009, 10010]

sku_id_list = [
    791256, 791257, 791258, 791259, 791260, 791261, 791262, 791263, 791264, 791265,
    791266, 791267, 791268, 791269, 791270, 791271, 791272, 791273, 791313, 791314,
    791315, 791316, 791317, 791318, 791319, 791320, 791321, 791322, 791323, 791324,
    791325, 791326, 791327, 791328, 791329, 791330, 791348, 791349, 791350, 791351,
    791352, 791353, 791354, 791355, 791356, 791357, 791358, 791359, 791360, 791361,
    791362, 791392, 791393, 791394, 791395, 791396, 791397, 791398, 791399, 791400,
    791401, 791402, 791403, 791404, 791405, 791406, 791436, 791437, 791438, 791439,
    791440, 791441, 791442, 791443, 791444, 791445, 791446, 791447, 791509, 791510,
    791511, 791512, 791513, 791514, 791515, 791516, 791517, 791518, 791519, 791520,
    791521, 791522, 791523, 791591, 791592, 791593, 791594, 791595, 791596, 791597,
    791598, 791599, 791600, 791601, 791602, 791603, 791604, 791605, 791606, 791607,
    791608, 791614, 791615, 791616, 791617, 791618, 791619, 791620, 791621, 791622,
    791623, 791624, 791625, 791626, 791627, 791628, 791629, 791630, 791631, 791635,
    791636, 791637, 791638, 791639, 791640, 791641, 791642, 791643, 791644, 791645,
    791646, 791647, 791648, 791649, 791650, 791651, 791652, 794856, 794857, 794858,
    794859, 794860, 794861, 794862, 794863, 794864, 794865, 794866, 794867, 794868,
    794869, 794870, 794871, 794872, 794873, 794936, 794937, 794938, 794939, 794940,
    794941, 794942, 794943, 794944, 794945, 794946, 794947, 794948, 794949, 794950,
    794951, 794952, 794953, 795015, 795016, 795017, 795018, 795019, 795020, 795021,
    795022, 795023, 795024, 795025, 795026, 795027, 795028, 795029, 795030, 795031,
    795032, 795097, 795098, 795099, 795100, 795101, 795102, 795103, 795104, 795105,
    795106, 795107, 795108, 795109, 795110, 795111, 795112, 795113, 795114, 916573,
    916574, 916576, 916577, 916578, 916580, 916581, 916582, 916584, 916585, 916586,
    916588, 916589, 916590, 916592, 916593, 916594, 916596, 917522, 917523, 917524,
    917525, 917526, 917527, 917528, 917529, 917530, 917531, 917532, 917533, 917534,
    917535, 917536, 917537, 917538, 917539, 917540, 917541, 917542, 917543, 917544,
    917545, 918825, 918826, 918827, 918828, 918829, 918830, 918831, 918832, 918833,
    918834, 918835, 918836, 918837, 918838, 918839, 929414, 929415, 929416, 929417,
    929419, 929420, 929421, 929422, 929424, 929425, 929426, 929427, 929429, 929430,
    929431, 929432, 929434, 929435, 929436, 929437, 1073942, 1073943, 1073944, 1073945,
    1073946, 921933, 921934, 921935, 921936, 921937, 921938, 921939, 921940, 921941,
    921942, 921943, 921944, 921945, 921946, 921947, 921948, 921949, 921950, 921951,
    921952, 921953, 921954, 921955, 921956, 921013, 921014, 921015, 921016, 921018,
    921019, 921020, 921021, 921023, 921024, 921025, 921026, 921028, 921029, 921030,
    921031, 921033, 921034, 921035, 921036, 1025901, 1025902, 1025903, 1025904, 1025905,
    1005805, 1005806, 1005807]

# 字段说明,必须一一对应
# login为空表示使用随机用户名

now_count = 0
lock_obj = thread.allocate()


def send_http():
    global now_count
    try:
        user_index = random.randint(0, (len(user_list) - 1))
        sku_id_index = random.randint(0, (len(sku_id_list) - 1))
        user = str(user_list[user_index])
        sku_id = str(sku_id_list[sku_id_index])
        url = 'http://' + addr + ':' + port + uri + '?token=' + token + '&' + params + '&userId=' + user + '&skuId=' + sku_id
        response = requests.get(url)

        #print '发送数据: ' + url
        #print '返回码: ' + str(response.status_code)
        #print '返回数据: ' + response.content

        logging.info('用户' + user + ' 商品skuId:' + sku_id)
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
        #print ''
        #print '***************************请求次数:' + str(now_count) + '*******************************'
        #print 'Thread:(%d) Time:%s\n' % (thread.get_ident(), time.ctime())

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
    time.sleep(100000)
