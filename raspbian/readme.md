### Raspberry Pi OS
#### 1. 고정 IP
* 부팅 전  
cmdline.txt 을 열어 마지막 줄에 한 칸 띄우고 작성한다.  
ip=<고정IP>::<게이트웨이>:<넷마스크>::<인터페이스>:off  
ex)  
ip=192.168.0.100::192.168.0.1:255.255.255.0::rpi:wlan0:off  
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
