#! C:\Users\s4223\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
#api = Application Programming Interface 애플리케이션을 구현하기 위해 시간 순서에 따라 배치해야할 기능

print("Content-Type: text/html")
print()
import  os, cgi, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    #description = description.repalce('<','&lt') 보안을 위해 사용할 수 있는 코드, 소스를 그대로 보여줌
    #description = description.repalce('>','&gt')
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
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
  <a href="create.py">create</a>
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=title, desc=description, listStr=view.get_list(), update_link=update_link, delete_action=delete_action))
