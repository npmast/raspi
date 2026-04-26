from gpiozero import LED, Button
from signal import pause

led = LED(14)
button = Button(17)

def toggle_led():
    led.toggle()
    print("LED TOGGLE")

button.when_pressed = toggle_led

pause()
