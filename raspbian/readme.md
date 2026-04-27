### Raspberry Pi OS
#### 1. 고정 IP
* GUI
```c
WiFi > Edit Connections > 현재 WiFi 선택하고 하단의 Edit 클릭
IPv4 Setting > Mehtod: Manual / Address: ADD / Netmask / Gateway / DNS servers 
```
#### 2. update & upgrade
```c
$ sudo apt update
$ sudo aup upgrade
```
#### 3. VNC
```c
$ sudo raspi-config
3. Interface Option
I3 VNC
```
#### 4. 한글 설치  
```c
$ sudo apt install fonts-nanum fonts-nanum-extra     // 폰트 설치
$ sudo apt install fonts-unfonts-core                // 폰트 등록
$ sudo apt install ibus                              // 입력기 설치
$ sudo apt install ibus-hangul                       // ibus 패키지 설치
$ ibus-setup
```
input Method > Add > kroean 검색 > Korean - Hangul 선택 > Preferences > Add > Key 등록  
#### 4. Raspberry Pi 5
Pi 5에서는 예전 RPi.GPIO, wiringPi, raspi-gpio 방식이 잘 맞지 않다.  
Raspberry Pi OS Bookworm 기준으로 Python 은 gpiozero 가 권장되고, Pi 5 는 GPIO 하드웨어 구조가 바뀌어서 기존 라이브러리들이 동작하지 않을 수 있다.
* C/C++
```c
$ sudo apt install libgpiod-dev gpiod -y  
# include <gpiod.h>
gcc compile 시 -lgpiod 옵션 추가
```
* Python
```c
//$ sudo apt install python3-libgpiod -y
$ sudo apt install python3.12-venv
$ mkdir -p ~/venvs
$ cd ~/venvs
$ python3 -m venv --system-site-packages .venv
$ soucre .venv/bin/activate
$ deactivate
```
* 두 언어를 모두 사용할 때는 패키지 둘 다 설치를 한다.  
* 터미널 제어
```c
$ pinctrl set 14 op
$ pinctrl set 14 dh
$ pinctrl set 14 dl
```
