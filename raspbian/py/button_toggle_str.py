from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

button = Button(2)

button.when_pressed = say_hello
button.when_released = say_goodbye

try:
    pause()                // 종료 시그널까지 기다림
except KeyboardInterrupt:
    led.off()
    led.close()
