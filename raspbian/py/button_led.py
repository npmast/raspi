from gpiozero import LED, Button
form signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

try:
    pause()                // 종료 시그널까지 기다림
except KeyboardInterrupt:
    led.off()
    led.close()
