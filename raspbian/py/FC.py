import smbus
import time

bus = smbus.SMBus(1)

ADDR = 0x48
CHANNEL = 0

# 자동 캘리브레이션용 초기값
min_val = 255
max_val = 0

def read_cds(channel):
    bus.write_byte(ADDR, 0x40 | channel)
    bus.read_byte(ADDR)      # dummy read
    return bus.read_byte(ADDR)

def read_cds_avg(channel, count=5):
    total = 0
    for _ in range(count):
        total += read_cds(channel)
        time.sleep(0.02)
    return total // count

def normalize(value, min_value, max_value):
    if max_value == min_value:
        return 0
    result = (value - min_value) / (max_value - min_value) * 100
    # 0~100 범위 제한
    if result < 0:
        result = 0
    elif result > 100:
        result = 100
    return int(result)

try:
    print("CDS 자동 캘리브레이션 시작")
    print("센서에 어두운 상태와 밝은 상태를 모두 한번씩 만들어 주세요.")
    print("Ctrl + C 로 종료합니다.")
    while True:
        # 안정화된 평균값 읽기
        val = read_cds_avg(CHANNEL, count=5)
        # 자동 캘리브레이션
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
        # 0~100 변환
        percent = normalize(val, min_val, max_val)
        print(
            f"CDS raw: {val}, "
            f"min: {min_val}, "
            f"max: {max_val}, "
            f"level: {percent}%"
        )

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n종료")
finally:
    bus.close()
