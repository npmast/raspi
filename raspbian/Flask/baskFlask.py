'''
외부접속, port : 5000
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')	                    # route 데코레이터가 함수와 url을 연결시켜준다.
def hello_world():
	return 'Hello World'

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)


'''
* flack 패키지에서 Flask 모듈 import
* __name__ 이름 속성을 가진 Flask 객체 app 생성
* 라우팅을 위한 뷰 함수 등록
  클라이언트가 URI로 ("/") 요청하면 route 데코레이터 아래의 뷰 함수가 호출된다.
* 뷰 함수는 return을 반드시 가지고 있어야 한다.
* 터미널에서 직접 실행하면 파일 이름이 __main__으로 바뀐다.
  직접 실행을 위한 명령문이다.(import는 __maim__)으로 바뀌지 않는다.
'''
