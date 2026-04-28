import smbus
import time

bus = smbus.SMBus(1)
ADDR = 0x48

def read_analog(channel):
    # channel: 0~3
    bus.write_byte(ADDR, 0x40 | channel)
    bus.read_byte(ADDR)  # dummy read
    return bus.read_byte(ADDR)

while True:
    x = read_analog(0)  # VRX
    y = read_analog(1)  # VRY

    print(f"X: {x}, Y: {y}")

    if x > 200:
        print("RIGHT")
    elif x < 50:
        print("LEFT")
    if y > 200:
        print("UP")
    elif y < 50:
        print("DOWN")
    if 110 < x < 140:              # 안정화(데드존 필요)
    print("CENTER")
  
    time.sleep(0.2)
