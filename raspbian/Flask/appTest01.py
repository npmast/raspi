# 단순 페이지나 데이터 처리

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Flask Server Test"

@app.route('/user/')	                    # /user - ok 200
def user():
	return "admin"

@app.route('/pw')		                      # /pw/ - not found 404
def pw():
	return '1111'

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

'''
Flask 프레임워크 자체는 사용자의 요청을 기다리는 거대한 '메인 루프' 역할을 한다.
특정 URL로 요청이 들어오면, Flask는 해당 경로에 연결된 뷰 함수(View Function)를 호출하여 실행한다.
'''
