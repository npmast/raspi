import gpiod

CHIP = "gpiochip4"
LINE = 17

chip = gpiod.Chip(CHIP)
line = chip.get_line(LINE)

line.request(
    consumer="button",
    type=gpiod.LINE_REQ_EV_BOTH_EDGES
)

state = False   # 초기 상태 (OFF)

print("버튼 대기중...")

try:
    while True:
        if line.event_wait(sec=5):
            event = line.event_read()

            # 👉 눌림 순간만 처리 (중요)
            if event.type == gpiod.LineEvent.RISING_EDGE:
                state = not state   # 토글

                if state:
                    print("ON")
                else:
                    print("OFF")

except KeyboardInterrupt:
    print("종료")
finally:
    line.release()
