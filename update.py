#! C:\Users\s4223\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
#form은 url query string을 만들어주는 역할 수행
#
print("Content-Type: text/html")
print()
import cgi, view
 
form = cgi.FieldStorage() #Cgi.fieldstorage는 url의 querystring부분을 반환하는 함수
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href = "create.py">create</a>
  <form action = "process_update.py" method = "post"> 
    <input type= "hidden" name = "pageId" = value = "{form_default_title}">
    <p><input type = "text" name = "title" placeholder = "title" value= {form_default_title}></p>
    <p><textarea rows = "4" name = "description" placeholder = "description">{form_default_description}</textarea></p>
    <p><input type = "submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.get_list, form_default_title = pageId, form_default_description = description))

""" form은 입력받은 데이터를 처리하기 위한 태그, action-> 보낼 주소
method -> get: 데이터를 가져오는 경우에는 get을 사용, 그러나 사용자가 정보를 수정 추가 하는 등의 작업을 할 때 서버쪽으로
query string을 사용하면 클라이언트가 서버 정보를 변경할 수도 있어서 보안상 문제! 
method -> post: query string을 사용하지 않아 url에 표시가 되지않고 다른 방식으로 전달됨. """