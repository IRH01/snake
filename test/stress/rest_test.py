#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

# url = 'http://192.168.105.66:8111/gj/order/test?orderNo=XX20161128191631853904708'
url = 'http://192.168.105.66:8111/gj/order/details?token=auc_jsession_33d8749702b0a7732b3003648a95596b1abb2754&' \
      'params={"orderNo":"XX20161128191631853904708"}'
response = requests.get(url)
print response.content
