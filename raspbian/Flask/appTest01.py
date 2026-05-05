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
