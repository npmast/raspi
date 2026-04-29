# pip install adafruit-circuitpython-dht
import time
import board
import adafruit_dht

# DATA 핀: GPIO4 = board.D4 = 물리핀 7번
dht = adafruit_dht.DHT11(board.D4)

try:
    print("DHT11 온습도 측정 시작...")

    while True:
        try:
            temp = dht.temperature
            hum = dht.humidity

            if temp is not None and hum is not None:
                print(f"Temp: {temp:.1f}°C / Hum: {hum:.1f}%")
            else:
                print("Faild to measure")

        except RuntimeError as e:
            # DHT11은 가끔 읽기 실패가 정상적으로 발생함
            print("Failed, restart:", e)

        time.sleep(2)

except KeyboardInterrupt:
    print("exit")

finally:
    dht.exit()
