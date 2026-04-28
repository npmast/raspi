from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=23, trigger=24)        # m(미터): 0m ~ 1m

try:
  while True:
    print('Distance: ', sensor.distance, 'm')
    sleep(1)
except KeyboardInterrupt:
  sensor.close()

# Trigger -> 초음파 발사 -> 반사 -> Echo -> 시간을 거리로 변환
# S = vt. v = 343m/s
# DistanceSensor(echo, trigger, queue_len=3, max_distance=1, threshold_distance=0.3,
# partial=False): max_di...: 최대 즉정 거리, thres...: 이벤트 발생 기준 거리
