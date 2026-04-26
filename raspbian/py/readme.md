### gpiozero
260427
- 가장 쉽다.
```c
$ sudo apt update
$ sudo apt install python3-gpiozero python3-lgpio
```
- 라즈비안 구조:  
  libgpiod(c) 최신, python gpiod 혼합 버전으로 버전 문제  
  Python gpiod는 버전이 통일되지 않아 Pi5 에서는 끼지기 쉽고 gpiozero가 가장 안정적이다.  
