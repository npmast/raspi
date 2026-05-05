# route 데코레이터 입력

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "Web LED Control"

@app.route('/led/on')
def ledOn():
  return '<h1> Led On </h1>'

@app.route('/led/off')
def ledOf():
  return '<h1> Led Off </h1>'

@app.routhe('/led/clean')
def gpioCleanup():
  return '<h1> GPIO CLEANUP </h1>'

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)
