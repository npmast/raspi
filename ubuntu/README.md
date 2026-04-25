### ubuntu 시작하기
#### 1. setting  
* wifi 설정
* openssh-server 설치  
``` c
$ sudo apt install openssh-server -y
$ sudo apt update
$ sudo apt upgrade -y
```
* 고정 IP 설정
```c
$ nmcli con show
nmcli con mod "WiFi_id" \
ipv4.addresses 172.30.1.10/24 \
ipv4.gateway 172.30.1.254 \
ipv4.dns "168.126.63.1" \
ipv4.method manual
$ nmcli con down "WiFi_id"
$ nmcli con up "WiFi_id"
$ sudo reboot                         // ssh 경우
$ ip a
```
* vncserver 설치
 ```c
ros2/00_setup_docs/pi_ubuntu.md
```
* terminator 설치  
```c
$ sudo apt install terminator -y
```
#### 2. GPIO
* C/C++
```c
$ sudo apt install libgpiod-dev gpiod -y  
# include <gpiod.h>
gcc compile 시 -lgpiod 옵션 추가
```
* Python
```py
$ sudo apt install python3-libgpiod -y
$ sudo apt install python3.12-venv
$ mkdir -p ~/venvs
$ cd ~/venvs
$ python3 -m venv --system-site-packages .venv
$ soucre .venv/bin/activate
$ deactivate
```
* 두 언어를 모두 사용할 때는 패키지 둘 다 설치를 한다.
* jupyter lab 설치
```c
ros2/00_setup_docs/pi_ubuntu.md
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


