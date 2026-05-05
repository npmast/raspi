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
