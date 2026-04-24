#### API 연결  
gpiod_chip_open:               GPIO 장치 열기  
gpiod_chip_get_line:           핀 가져오기  
gpiod_line_request_output:     출력 모드 설정  
gpiod_line_set_value:          값 설정  
gpiod_lint_event_wait:         이벤트 대기  
#### 매핑  
chip = gpiod_chip_open("/dev/gpiochip4");  
line = gpiod_chip_get_line(chip, 14);  
