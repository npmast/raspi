import gpiod
import time

LED_GPIO = 17
BUTTON_GPIO = 27

chip = gpiod.Chip("/dev/gpiochip4")

led = chip.get_line(LED_GPIO)
button = chip.get_line(BUTTON_GPIO)

led.request(
    consumer="led",
    type=gpiod.LINE_REQ_DIR_OUT
)

button.request(
    consumer="button",
    type=gpiod.LINE_REQ_EV_BOTH_EDGES,
    flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_UP   # 내부 풀업 사용
)

led_state = 0
led.set_value(led_state)

print("버튼 대기 중... Ctrl+C 종료")

try:
    while True:
        if button.event_wait(sec=1):
            event = button.event_read()
            if event.type == gpiod.LineEvent.FALLING_EDGE:
                led_state = 1 - led_state
                led.set_value(led_state)
                if led_state:
                    print("버튼 눌림 → LED ON")
                else:
                    print("버튼 눌림 → LED OFF")
            elif event.type == gpiod.LineEvent.RISING_EDGE:
                print("버튼 뗌")

except KeyboardInterrupt:
    print("종료")
finally:
    led.set_value(0)
    led.release()
    button.release()
    chip.close()
      

#line.request(): GPIO 라인을 커널에 사용 요청하는 함수
#consumer = "button": GPIO를 사용하는 메타 데이터(라벨) gpioinfo gpiochip4 로 확인
#type = gpiod.LINE__REQ_EV_BOTH_EDGES: 이 라인을 "입력 + 이벤트 감지 모드"로 설정
#  LIND_REQ_EV: 이벤트 요청(인터럽트 기반)
#  BOTH_EDGES: 두 가지 변화 감지
```
