#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

import pymongo

db = pymongo.MongoClient(host="192.168.105.9", port=27016).irh


def getAllCollections():
    # db.authenticate('username', 'password')

    for colle in db.collection_names():
        if str(colle).startswith('circle') == 1:

            print colle


if __name__ == '__main__':
    conn = pymongo.MongoClient(host='192.168.105.9', port=27016)

    StartTime = time.time()
    getAllCollections()
    EndTime = time.time()
    print "StartTime : %s" % StartTime
    print "EndTime : %s" % EndTime
    CostTime = round(EndTime - StartTime)
    print "CostTime : %s" % CostTime
