#!/usr/bin/python
#coding=utf-8
import os
import subprocess
import argparse

projects = ["CVP"]

parser = argparse.ArgumentParser(description="客户版本问题导出工具")
parser.add_argument('-u', action="store", dest="user")
parser.add_argument('-p', action="store", dest="password")
parser.add_argument('-a', action="store", dest="assignee")

results = parser.parse_args()
if results.user == None or results.password == None:
  parser.print_usage()
  exit(-1)

if not os.path.exists("./output"):
  os.mkdir("./output")

print "user = %s " % results.user
print "password = %s " % results.password
print "assignee = %s " % results.assignee

cmd = "java -jar ./razor.jar -Dproject=%s -Dprovider=CVE -Duser=%s -Dpassword=%s -Dexcelpath=./output/客户版本问题汇总.xlsx -Dsheetname=test1 -Duri=http://192.168.8.250:8081 -Dissuestatus=TODO,DOING"
hasAssignee = False
if results.assignee != None and len(results.assignee) != 0:
  hasAssignee = True;
  cmd = cmd + " -Dassignee=%s"

for project in projects:
  print "-" * 100;
  if(hasAssignee):
    cmd = cmd % (project, results.user, results.password, results.assignee)
  else:
    cmd = cmd % (project, results.user, results.password)

  print "CMD: [%s]" % cmd
  subprocess.call(cmd, shell=True);
