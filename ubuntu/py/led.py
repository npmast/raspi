import gpiod
import time

CHIP = "/dev/gpiochip4"   # Pi5 핵심
LED_GPIO = 14            # GPIO14

chip = gpiod.Chip(CHIP)
led = chip.get_line(LED_GPIO)

led.request(consumer="led", 
            type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        print("LED ON")
        line.set_value(1)
        time.sleep(1)

        print("LED OFF")
        line.set_value(0)
        time.sleep(1)

except KeyboardInterrupt:
    print("종료")
finally:
    line.release()

# consumer: 식별 이름
# DIR_OUT: 출력 모드  
