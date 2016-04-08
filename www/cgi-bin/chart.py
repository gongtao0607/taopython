#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgitb,cgi
import db
cgitb.enable()

print("Content-Type: application/json;charset=utf-8")
print()

id = cgi.FieldStorage().getvalue('id')
if id is None:
	print("{'error':'Empty id'}")
else:
	ret=db.load(id)
	print(ret["analysis"])
