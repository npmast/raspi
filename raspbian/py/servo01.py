from gpiozero import Servo
from time import sleep

servo = Servo(17)

try:
  while True:
    servo.min()                  # 최소
    sleep(2)
    servo.mid()                  # 중간
    sleep(2)
    servo.max()                  # 최대
    sleep(2)
except KeyboardInterrupt:
  servo.close()
