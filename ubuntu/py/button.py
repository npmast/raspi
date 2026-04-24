import gpiod
import time

CHIP = "gpiochip4"   # Pi5 핵심
LINE = 17            # GPIO17

chip = gpiod.Chip(CHIP)
line = chip.get_line(LINE)

# 이벤트(입력 + 이벤트 감지(양쪽 엣지 감지))
line.request(
    consumer = "button",
    type = gpiod.LINE_REQ_EV_BOTH_EDGES
)

print("버튼 대기중...")

try:
    while True:
        event = line.event_wait(sec=5)
        if event:
            ev = line.event_read()
            if ev.type == gpiod.LineEvent.RISING_EDGE:
                print("ON")   # 버튼 눌림
            elif ev.type == gpiod.LineEvent.FALLING_EDGE:
                print("OFF")  # 버튼 뗌
        else:
            print("대기중...")
          
except KeyboardInterrupt:
    print("종료")
finally:
    line.release()


#line.request(): GPIO 라인을 커널에 사용 요청하는 함수
#consumer = "button": GPIO를 사용하는 메타 데이터(라벨) gpioinfo gpiochip4 로 확인
#type = gpiod.LINE__REQ_EV_BOTH_EDGES: 이 라인을 "입력 + 이벤트 감지 모드"로 설정
#  LIND_REQ_EV: 이벤트 요청(인터럽트 기반)
#  BOTH_EDGES: 두 가지 변화 감지
```
