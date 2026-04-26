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
#### 3. 한글 설치  
```c
$ sudo apt install fonts-nanum fonts-nanum-extra     // 폰트 설치
$ sudo apt install fonts-unfonts-core                // 폰트 등록
$ sudo apt install ibus                              // 입력기 설치
$ sudo apt install ibus-hangul                       // ibus 패키지 설치
$ ibus-setup
```
input Method > Add > kroean 검색 > Korean - Hangul 선택 > Preferences > Add > Key 등록
