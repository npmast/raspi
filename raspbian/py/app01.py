from flask import Flask, render_template_string, redirect, url_for
from gpiozero import LED
from signal import pause

app = Flask(__name__)

led = LED(17)            # gpio 17

html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>LED Control</title>
</head>
<body>
    <h1>Raspberry Pi LED Control</h1>

    <p>LED 상태: {{ state }}</p>

    <form action="/on" method="post">
        <button type="submit">LED ON</button>
    </form>

    <form action="/off" method="post">
        <button type="submit">LED OFF</button>
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    state = "ON" if led.is_lit else "OFF"
    return render_template_string(html, state=state)

@app.route("/on", methods=["POST"])
def led_on():
    led.on()
    return redirect(url_for("index"))

@app.route("/off", methods=["POST"])
def led_off():
    led.off()
    return redirect(url_for("index"))

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=False)
    finally:
        led.off()
        led.close()
