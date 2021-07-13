#! C:\Users\s4223\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_file = open("data/" + pageId, "w")
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)
#Redirection 웹서버가 사용자를 다른 서버로 이동시키는 것
print("Location: index.py? id ="+title) # id가 index.py로 이동해서 query string의 id가 title인 곳으로 이동
print()

