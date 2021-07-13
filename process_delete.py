#! C:\Users\s4223\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
import os, cgi
form = cgi.FieldStorage()
pageId = form['pageId'].value
os.remove('data/'+pageId)
#Redirection
print("Location: index.py")
print()