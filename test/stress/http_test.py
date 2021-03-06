#!/usr/bin/env python
# coding=utf8

import httplib
import urllib

httpClient = None

try:
    params = urllib.urlencode({"orderNo": "XX20161128191631853904708"})
    httpClient = httplib.HTTPConnection('192.168.105.66', 8111, timeout=5000)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    httpClient.request('GET', '/gj/order/test?orderNo=1234', params, headers)

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
