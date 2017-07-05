#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 pip install elasticsearch
'''
from datetime import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch([
    {'host': '172.19.1.21', 'port': 9200},
    {'host': '172.19.1.22', 'port': 9200},
    {'host': '172.19.1.23', 'port': 9200},
])

es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
