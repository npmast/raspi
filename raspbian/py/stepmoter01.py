from gpiozero import OutputDevice
import time

IN1 = OutputDevice(17)
IN2 = OutputDevice(18)
IN3 = OutputDevice(27)
IN4 = OutputDevice(22)

pins = [IN1, IN2, IN3, IN4]

# half-step sequence
seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

def set_pins(values):
    for pin, val in zip(pins, values):
        pin.value = val

def stop():
    set_pins([0, 0, 0, 0])

def rotate(steps, delay=0.002, direction=1):
    sequence = seq if direction == 1 else list(reversed(seq))

    for _ in range(steps):
        for pattern in sequence:
            set_pins(pattern)
            time.sleep(delay)

    stop()

try:
    print("정방향 1회전")
    rotate(512, delay=0.002, direction=1)

    time.sleep(1)

    print("역방향 1회전")
    rotate(512, delay=0.002, direction=-1)

except KeyboardInterrupt:
    pass

finally:
    stop()
