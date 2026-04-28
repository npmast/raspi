from gpiozero import Servo
from time import sleep

servo = Servo(17)

try:
  while True:
    servo.min()
    sleep(2)
    servo.mid()
    sleep(2)
    servo.max()
    sleep(2)
except KeyboardInterrupt:
  servo.close()
