# pip install keyboard
from gpiozero import Button
import keyboard
import time

# GPIO 2번 핀에 버튼 연결 (핀 번호는 환경에 맞게 변경)
button = Button(2)

def button_pressed():
    print("버튼 눌림 -> Space 키 입력")
    # 스페이스바를 누름
    keyboard.press('space')
    # 약간의 대기 후 뗌
    time.sleep(0.1)
    keyboard.release('space')

# 버튼이 눌릴 때(when_pressed) 함수 호출
button.when_pressed = button_pressed

# 키보드 입력 감지 함수
def on_key(e):
    print(f"[키 입력 감지] {e.name}")

keyboard.on_press(on_key)

print("프로그램 시작... 버튼을 누르세요.")
print("프로그램 시작... 버튼을 누르세요.")
# 프로그램이 종료되지 않도록 유지
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
