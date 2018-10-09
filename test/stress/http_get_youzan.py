#!/usr/bin/env python
# coding=utf8
import datetime
import os
import urllib2

urlTemplate = 'http://qa002.retailchannel.blissmall.net/youzan/compensate/history/order?startTime={}&endTime={}'

dateStart = '2018-09-01 00:00:00'
dateEnd = '2018-09-12 00:00:00'
dateTemp = dateStart

filePath = 'youzan_compensate.log'

if (os.path.exists(filePath)):
    os.remove(filePath)

files = open(filePath, "a")
files.writelines('有赞的补偿订单处理\n\n')
dateAdd = datetime.timedelta(hours=4)

while dateTemp <= dateEnd:
    date = datetime.datetime.strptime(dateTemp, '%Y-%m-%d %H:%M:%S') + dateAdd
    url = urlTemplate.format(dateTemp, date.strftime('%Y-%m-%d %H:%M:%S'))

    req = urllib2.Request(url.replace(' ', '%20'))
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print dateTemp + "——" + date.strftime("%Y-%m-%d %H:%M:%S")
    files.write(dateTemp + "——" + date.strftime("%Y-%m-%d %H:%M:%S") + '\n')
    strRequest = '请求参数为：{}'
    print strRequest.format(url)
    files.writelines(strRequest.format(url) + '\n')
    strResponse = '响应结果为：{}'
    print strResponse.format(res)
    files.writelines(strResponse.format(res) + '\n')
    files.writelines('\n\n')

    dateTemp = date.strftime("%Y-%m-%d %H:%M:%S")

files.close()
print "请求执行完成"
