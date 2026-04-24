#### API 연결  
gpiod_chip_open:               GPIO 장치 열기  
gpiod_chip_get_line:           핀 가져오기  
gpiod_line_request_output:     출력 모드 설정  
gpiod_line_set_value:          값 설정  
gpiod_lint_event_wait:         이벤트 대기  
#### 매핑  
```c
chip = gpiod_chip_open("/dev/gpiochip4");      // 먼저 gpiochip4 의 fd를 구하고
line = gpiod_chip_get_line(chip, 14);          // 구한 fd 의 핀을 사용한다.
```
#### libgpiod 설치
```c
$ sudo apt install libgpiod_dev -y
# include <gpiod.h>
gcc compile 시 -lgpiod 옵션 추가
```
