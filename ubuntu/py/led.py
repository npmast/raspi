import gpiod
import time

CHIP = "gpiochip4"   # Pi5 핵심
LINE = 17            # GPIO17

chip = gpiod.Chip(CHIP)
line = chip.get_line(LINE)

line.request(consumer="led", type=gpiod.LINE_REQ_DIR_OUT)

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
