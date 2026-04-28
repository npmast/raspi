from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(17, hold_time=2)
shutdown_btn.when_held = shutdown

try:
    pause()                // 종료 시그널까지 기다림
except KeyboardInterrupt:
    button.close()
