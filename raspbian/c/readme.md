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
* 중요한 함수들  
  GPIO 칩 열기-> GPIO 설정 생성 -> GPIO request 생성 -> GPIO 값 읽기/쓰기 -> GPIO 반환  
  - gpiod_chip_open()                    GPIO 컨트롤러 장치 염
  ```c
  struct gpiod_chip* chip;
  chip = gpiod_chip_open("/dev/gpiodchip0")
  ```
  - gpiod_line_settings_new()            GPIO 동작 설정 객체 생성
  ```c
  struct gpiod_line_settings* settings
  settings = gpiod_line_settings_new();
  출력 또는 입력 설정
  gpiod_line_settings_set_direction(
    settings,
    GPIOD_LINE_DIRECTION_OUTPUT or GPIOD_LINE_DIRECTION_INPUT
  );
  ```
  - gpiod_line_config_new()                GPIO 라인 설정들을 묶는 객체
  ```c
  struct gpiod_line_config *config;
  config = gpiod_line_config_new();
  ```
  - gpiod_chip_request_lines()            GPIO 사용 요청 생성(핵심 햠수)
  ```c
  struct gpiod_line_request* request
  request = gpiod_chip_request_lines(
    chip,
    NULL,
    config
  );
  ```
  - gpiod_line_request_set_value()                GPIO 출력 값 설정
  ```c
  gpiod_line_request_set_value(
    request,
    21,
    GPIOD_LINE_VALUE_ACTIVE or GPIOD_LINE_VALUE_INACTIVE
  );
  ```
  - gpiod_line_request_get_value()                GPIO 입력 값 읽기
  ```c    
  int value;
  value = gpiod_line_request_get_value(
    request,
    17
  );
  ```
  - gpiod_line_request_release()                사용 해제
  ```c
  gpiod_line_request_release(request);
  ```

* 흐름 패턴
  > 1. chip 열기
  > 2. settings 생성 (output)
  > 3. config 에 라인 등록
  > 4. request 생성 (라인 점유)
  > 5. 값 set (ON/OFF)
  > 6. release
#### 4. easy_led.c  
pintctl 방식  
```c
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
    while (1) {
        system("pinctrl set 14 dh");
        sleep(1);

        system("pinctrl set 14 dl");
        sleep(1);
    }

    return 0;
}
```
