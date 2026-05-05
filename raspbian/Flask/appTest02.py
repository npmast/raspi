# route 데코레이터 입력

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Flask Server Test"

#변수규칙
@app.route('/user/<username>')                    	# URL에서 <username>을 매개변수로 받는다
def user_profile(username):
	return "User %s" % username						# 클라이어트에게 보낸다.

@app.route('/pw/<int:pw_num>')
def show_pw(pw_num):
	return 'pw %d' % pw_num

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

'''
가변적인 데이터를 뷰 함수로 전달받는다.
'''
