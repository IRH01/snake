#!/usr/bin/env python
# coding=utf8
import datetime
import os
import urllib2

urlTemplate = "http://qa002.retailchannel.blissmall.net/eleme/compensate/history/order?date={}"

dateStart = '2018-08-15'
dateEnd = '2018-10-10'
dateTemp = dateStart

filePath = 'eleme_compensate.log'

if (os.path.exists(filePath)):
    os.remove(filePath)

files = open(filePath, "a")

files.writelines('饿了么的补偿订单处理\n\n')
dateAdd = datetime.timedelta(days=1)
while dateTemp <= dateEnd:
    url = urlTemplate.format(dateTemp)
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print dateTemp
    files.writelines(dateTemp + '\n')
    strRequest = '请求参数为：{}'
    print strRequest.format(url)
    files.writelines(strRequest.format(url) + '\n')
    strResponse = '响应结果为：{}'
    print strResponse.format(res)
    files.writelines(strResponse.format(res) + '\n')
    files.writelines('\n\n')

    date = datetime.datetime.strptime(dateTemp, '%Y-%m-%d') + dateAdd
    dateTemp = date.strftime('%Y-%m-%d')

files.close()
print "请求执行完成"
