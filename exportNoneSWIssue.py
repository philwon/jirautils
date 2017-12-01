#!/usr/bin/python
#coding=utf-8
import os
import subprocess
import argparse

projects = ["A1000M","A708N", "C86VK", "H802N", "K116L", "K116S", "K707L",
            "K960NN", "R706N", "W801MN", "W802MN", "W807MN", "W960MN", "W960TN"]

parser = argparse.ArgumentParser(description="基线外协问题导出工具")
parser.add_argument('-u', action="store", dest="user")
parser.add_argument('-p', action="store", dest="password")

results = parser.parse_args()
if results.user == None or results.password == None:
    parser.print_usage()
    exit(-1)

print "user = %s " % results.user
print "password = %s " % results.password

if not os.path.exists("./output"):
  os.mkdir("./output")

for project in projects:
    print "-" * 100;
    subprocess.call("java -jar ./razor.jar -Dproject=%s -Dprovider=CLE -Duser=%s -Dpassword=%s "
                    "-Dexcelpath=./output/基线外协问题汇总.xlsx -Dsheetname=test1 -Duri=http://192.168.8.250:8081 "
                    "-Dissuestatus=TODO,DOING -Dassignee=wangxuguang" % (project, results.user, results.password), shell=True);