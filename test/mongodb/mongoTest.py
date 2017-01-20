#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time

import pymongo

db = pymongo.MongoClient(host="192.168.105.10", port=27016).irh


def getAllCollections():
    # db.authenticate('username', 'password')
    os.popen("rm -rf /usr/mongodb/data/irh_bak")
    dump_sh = "/usr/mongodb/bin/mongodump -h 192.168.105.10:27016 -d irh -o /usr/mongodb/data/irh_bak"
    os.popen(dump_sh)

    print "start export"
    os.popen("rm -rf /usr/mongodb/bak/*")
    for collection_name in db.collection_names():
        if collection_name.startswith('circle') == 1 and str(collection_name).__len__() > 6:
            export_sh = "/usr/mongodb/bin/mongoexport -h 192.168.105.10:27016 -d irh -c " + collection_name + " -o /usr/mongodb/bak/" + collection_name + ".json"
            os.popen(export_sh)

            print collection_name
    print "finished export success"
    print "start import"

    db.drop_collection('circle')

    ls_str = os.popen("ls /usr/mongodb/bak/").read()
    files = ls_str.split("\n")
    for fileName in files:
        if str(fileName).startswith('circle') == 1 and str(fileName).__len__() > 11 and str(fileName).endswith(".json"):
            import_sh = "/usr/mongodb/bin/mongoimport -h 192.168.105.10:27016 -d irh -c circle --file /usr/mongodb/bak/" + fileName
            os.popen(import_sh)
            print fileName

    print "finished import success"


if __name__ == '__main__':
    conn = pymongo.MongoClient(host='192.168.105.10', port=27016)

    StartTime = time.time()
    # db.drop_collection('circle')
    db.circle.drop()
    # getAllCollections()
    EndTime = time.time()
    print "StartTime : %s" % StartTime
    print "EndTime : %s" % EndTime
    CostTime = round(EndTime - StartTime)
    print "CostTime : %s" % CostTime
