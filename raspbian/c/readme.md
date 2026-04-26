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
칩은 gpiochip0 인걸 알 수 있다.
```
#### 3. V2 API
최신 버전을 libgpiod v2 라이브러리 사용한다.  
* 전체 구조  
```c
chip (/dev/gpiochipN)
   └─ request (한 번의 점유/설정 단위)
         └─ lines (GPIO 번호들: 17, 18, ...)
               └─ settings (입출력, 바이어스, 엣지 등)
```
* 주요 타입
  ```c
  gpiod_chip                      /dev/gpiochipN` 핸들
  gpiod_line_settings             방향/바이어스/엣지/액티브 로우 등
  gpiod_line_config               “어떤 라인들에 어떤 설정을 적용할지”
  gpiod_request_config            consumer 이름 등 메타정보   
  gpiod_line_request              실제 점유된 라인 묶음(핵심 객체) 
  ```
* 흐름 패턴
  > 1. chip 열기
  > 2. settings 생성 (output)
  > 3. config 에 라인 등록
  > 4. request 생성 (라인 점유)
  > 5. 값 set (ON/OFF)
  > 6. release
