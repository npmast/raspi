from gpiozero import LED
from time import sleep

led = LED(14)   # BCM GPIO17

try:
    while True:
        led.on()
        sleep(1)

        led.off()
        sleep(1)
except KeyboardInterrupt:
    print("\n program exit \n")
    led.off()
