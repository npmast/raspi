### ubuntu 시작하기
#### 1. setting  
* wifi 설정  
* openssh-server 설치  
```c
$ sudo apt install openssh-server -y
$ sudo apt update
$ sudo apt upgrade -y
```
* terminator 설치  
```c
$ sudo apt install terminator -y
```
* vncserver 설치
* 가상환경 설치
```c
$ sudo apt install python3.12-venv
$ mkdir -p ~/venvs
$ cd ~/venvs
$ python3 -m venv .venv
$ soucre .venv/bin/activate
$ deactivate
 ```
* jupyter lab 설치  
 

#### 2. libgpiod 설치  
* C
```c
$ sudo apt install libgpiod-dev gpiod -y
# include <gpiod.h>
gcc compile 시 -lgpiod 옵션 추가
```
* Python
  가상환경 사용
```py
$ sudo apt install python3-dev -y
$ pip install gpiod
```
#### 3. 매핑  
```c
chip = gpiod_chip_open("/dev/gpiochip4");      // 먼저 gpiochip4 의 fd를 구하고
line = gpiod_chip_get_line(chip, 14);          // 구한 fd 의 핀을 사용한다.
```
#### 4. API 연결  
gpiod_chip_open:               GPIO 장치 열기  
gpiod_chip_get_line:           핀 가져오기  
gpiod_line_request_output:     출력 모드 설정  
gpiod_line_set_value:          값 설정  
gpiod_lint_event_wait:         이벤트 대기  


