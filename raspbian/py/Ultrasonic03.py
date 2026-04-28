# 보정(평균값 적용)
from gpiozero import DistanceSensor
from time import sleep
import statistics

sensor = DistanceSensor(echo=24, trigger=23)

def get_distance_cm(samples=5):                 # 5회 측정 평균
    values = []                                 # 측정값 저장할 버퍼 
    for _ in range(samples):
        values.append(sensor.distance * 100)    # 100 -> cm로 변환
        sleep(0.05)                             # 측정 지연
    return statistics.mean(values)              # 평균 계산

try:
    while True:
        dist = get_distance_cm()
        print(f"거리(평균): {dist:.2f} cm")
        sleep(0.5)

except KeyboardInterrupt:
    pass

finally:
    sensor.close()
