import gpiod
import select
import time

CHIP = "gpiochip4"
BUTTON_LINE = 17

chip = gpiod.Chip(CHIP)
button = chip.get_line(BUTTON_LINE)

button.request(
    consumer="button",
    type=gpiod.LINE_REQ_EV_BOTH_EDGES
)

# GPIO 이벤트의 fd 얻기
button_fd = button.event_get_fd()

# epoll 객체 생성
ep = select.epoll()

# GPIO fd를 epoll에 등록
ep.register(button_fd, select.EPOLLIN)

state = False
last_time = 0
DEBOUNCE = 0.2

print("epoll 기반 버튼 대기중...")

try:
    while True:
        events = ep.poll(5)
        if not events:
            print("대기중...")
            continue
        for fd, event_mask in events:
            if fd == button_fd:
                gpio_event = button.event_read()
                if gpio_event.type == gpiod.LineEvent.RISING_EDGE:
                    now = time.time()
                    if now - last_time > DEBOUNCE:
                        state = not state
                        if state:
                            print("ON")
                        else:
                            print("OFF")

                        last_time = now

except KeyboardInterrupt:
    print("종료")

finally:
    ep.unregister(button_fd)
    ep.close()
    button.release()

# event_wait(): gpio 이벤트를 기다림
# event_get_fd(): GPIO 이벤트를 fd로 얻음
# epoll.register(): fd를 감시 목록에 등록
# epoll.poll(): 여러 fd 대기
# event_read(): 이벤트 읽기
