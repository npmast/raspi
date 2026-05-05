#### 폴더 구조  
project/  
├── app.py  
└── templates/  
    └── index.html  
#### HTML  
```html
- index.html -
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>LED Control</title>
</head>
<body>
    <h1>Flask LED 제어</h1>

    <p>현재 상태: <b>{{ state }}</b></p>

    <form action="/led/on" method="post">
        <button type="submit">LED ON</button>
    </form>

    <br>

    <form action="/led/off" method="post">
        <button type="submit">LED OFF</button>
    </form>
</body>
</html>
```

#### Flask
```py
- flask.py -
from flask import Flask, render_template, redirect, url_for
from gpiozero import LED

app = Flask(__name__)

led = LED(17)

@app.route("/")
def index():
    state = "ON" if led.is_lit else "OFF"                      // 3항 조건식: A if 조건 else B
    return render_template("index.html", state=state)

@app.route("/led/on", methods=["POST"])
def led_on():
    led.on()
    return redirect(url_for("index"))

@app.route("/led/off", methods=["POST"])
def led_off():
    led.off()
    return redirect(url_for("index"))

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        led.off()
        led.close()
```
