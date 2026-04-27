from gpiozero import LED, Button
from signal import pause

led = LED(14)
button = Button(17)

def button_pressed():
    led.on()
    print("BUTTON PRESSED")

def button_released():
    led.off()
    print("BUTTON RELEASED")

button.when_pressed = button_pressed
button.when_released = button_released

try:
    pause()
except KeyboardInterrupt():
    led.off()
    led.close()
    print("\n exit")
