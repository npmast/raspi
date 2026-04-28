 import smbus
 import time
 
 bus = smbus.SMBus(1)
 ADDR = 0x48
 channel = 0

 def read_cds(channel):
     bus.write_byte(ADDR, 0x40 | channel)        # AIN0
     bus.read_byte(ADDR)             # dummy
     return bus.read_byte(ADDR)

 try:
     while True:
         val = read_cds()
         print("CDS:", val)
         time.sleep(0.5)

 except KeyboardInterrupt:
     print("종료")

# 범위 변환
# new = (현재값 - 최소값) / (최대값 - 최소값) * 새범
