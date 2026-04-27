from gpiozero import LED, Button
from time import sleep

led = LED(14)          # GPIO14
button = Button(18)    # GPIO18, 기본 pull_up=True

try:
    while True:
        if button.is_pressed:
            led.on()
            print("BUTTON ON")
        else:
            led.off()
            print("BUTTON OFF")

        sleep(0.1)
except KeyboardInterrupt:
    led.close()
    print("\nprogram exit")
