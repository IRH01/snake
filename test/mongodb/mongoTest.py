#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
mongodb数据迁移备份操作
'''

import os
import time

import pymongo

# 安装python mongodb 依赖
# 修改配置信息
# su root & easy_install pymongo
host = "192.168.105.10:27016"
database_name = "irh"
collection_name = "circle"
mongodb_bin_path = "/usr/mongodb/bin/"
db = pymongo.MongoClient(host=host)[database_name]


# db.authenticate('username', 'password')


def getAllCollections():
    os.popen("rm -rf tmp/data/" + database_name + "_bak")
    dump_sh = mongodb_bin_path + "/mongodump -h " + host + " -d " + database_name + \
              " -o tmp/data/" + database_name + "_bak"
    os.popen(dump_sh)

    print "start export"
    os.popen("rm -rf tmp/output/*")
    for item in db.collection_names():
        if item.startswith(collection_name) == 1 and str(item).__len__() > 6:
            export_sh = mongodb_bin_path + "/mongoexport -h " + host + " -d " + database_name + " -c " + item \
                        + " -o tmp/output/" + item + ".json"
            os.popen(export_sh)

            print item

    print "finished export success"
    print "start import"

    db.drop_collection(collection_name)

    ls_str = os.popen("ls tmp/output/").read()
    files = ls_str.split("\n")
    for fileName in files:
        if str(fileName).startswith(collection_name) == 1 and str(fileName).__len__() > 11 and str(fileName).endswith(
                ".json"):
            import_sh = mongodb_bin_path + "/mongoimport -h " + host + \
                        " -d " + database_name + " -c " + collection_name + " --file tmp/output/" + fileName
            os.popen(import_sh)
            print fileName

    print "finished import success"


if __name__ == '__main__':
    StartTime = time.time()
    getAllCollections()
    EndTime = time.time()
    print "StartTime : %s" % StartTime
    print "EndTime : %s" % EndTime
    CostTime = EndTime - StartTime
    print "CostTime : %s" % CostTime
