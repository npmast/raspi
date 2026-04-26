import gpiod
import time

CHIP = "/dev/gpiochip4"
LINE = 17

chip = gpiod.Chip(CHIP)
line = chip.get_line(LINE)

line.request(
    consumer="led",
    type=gpiod.LINE_REQ_DIR_OUT
)

try:
    while True:
        line.set_value(1)
        time.sleep(1)

        line.set_value(0)
        time.sleep(1)

finally:
    line.release()
    chip.close()
