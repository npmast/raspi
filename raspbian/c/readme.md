### libgpiod  
#### 1. 설치
```c
$ sudo apt update
$ sudo apt install gpiod libgpiod-dev
```
#### 2. GPIO 칩 확인 
```c
$ gpiodetect
gpiodchip0 - 54 lines:
    line  0: ...
$ gpioinfo
```
칩은 gpiochip0 인걸 알 수 있다.
