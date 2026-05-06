# HTTP Method - 서버가 수행할동작지정
# GET - 모든 파라미터를 URL 로 보내는 방식

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get():
	value1 = request.args.get('이름', 'user')
	value2 = request.args.get('지역', '부산')
	return value1 + " : " + value2

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

'''
URL 주소로 접속하면 'uswr : 부산' 이 출력된다.
주소 다음에 ? 파라미너 형식을 사용한다.
xxx.xxx.xxx.xxx:500/?이름=홍길동?지역=서울
