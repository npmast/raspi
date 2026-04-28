from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

def toggle_led():
    led.toggle()
    print("LED TOGGLE")

button.when_pressed = toggle_led

try:
    pause()                // 종료 시그널까지 기다림
except KeyboardInterrupt:
    led.off()
    led.close()
