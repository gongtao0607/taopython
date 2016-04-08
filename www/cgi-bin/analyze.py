#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from time import strftime
import cgitb,cgi
import db
import json
import twitter,watson
cgitb.enable()

print("Content-Type: application/json;charset=utf-8")
print()

query_string = cgi.FieldStorage().getvalue('q').upper()
#case insensitive
if query_string is None:
	print("{'error':'Empty query'}")
else:
	tweets=twitter.search(query_string)
	db.store(query_string,time.time(),tweets,watson.analyze(tweets))
	ret=db.search(query_string)
	result=[]
	for doc in ret:
		result.append({"id":doc["_id"], "time":doc["time"]})
	print(json.dumps(result))
