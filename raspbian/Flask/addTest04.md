#### 폴더 구조  
project/  
├── app.py  
└── templates/  
    └── index.html  
templates 폴더를 만들고 그 안에 html 파일을 저장한다.
#### html
```html
- index.html

<!DOCTYPE html>
<html>
<head>
  <title>사용자 정보</title>
</head>
<body>
  <p>이름: {{ name }}</p>
  <p>나이: {{ age }}</p>
</body>
</thml>
```
#### flask
```py
- flask.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/user/')
def user_profile():
  user = '홍길동'
  age = 50
  return render_template('index.html', name=user, age=user_age)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, use_reloader=False)
```
