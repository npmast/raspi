# 버튼 누르면 90도 회전
from gpiozero import DigitalOutputDevice, Button
import time

# 스텝모터 핀
pins = [
    DigitalOutputDevice(17),
    DigitalOutputDevice(27),
    DigitalOutputDevice(22),
    DigitalOutputDevice(23),
]

# 버튼 (GPIO18, 풀업 사용)
button = Button(18, pull_up=True, bounce_time=0.05)

# Half-step 시퀀스
SEQ = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1],
]

def rotate_90():
    steps = 512  # 90도
    for _ in range(steps):
        for pattern in SEQ:
            for pin, val in zip(pins, pattern):
                pin.value = val
            time.sleep(0.002)

    # 모터 전류 차단 (발열 방지)
    for pin in pins:
        pin.off()

def on_button_pressed():
    print("버튼 눌림 → 90도 회전")
    rotate_90()

# 이벤트 등록
button.when_pressed = on_button_pressed

print("버튼 대기중... (Ctrl+C 종료)")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("종료")

finally:
    for pin in pins:
        pin.off()
