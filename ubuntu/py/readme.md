## 라즈베리파이 5
: RPi.GPIO는 Pi5에서 직접 지원되지 않기 때문에 libgpiod 가반을 사용한다.
### 1.필수 패키지  
```c
$ sudo apt update
$ sudo apt install python3-libgpiod
// $ python3 -c "import gpiod; print('OK')"          // 확인
$ gpiodetect                                      // gpio 정치 확인(pi5는 rp1 칩 사용)
```
### 2. 권한 문제 해결
```c
$ sudo usermod -aG gpio $USER
또는 sudo 를 붙혀 실행한다.
```
### 3. 가상 환경 설치
```c
$ python3 -m venv --system-site-packages .venv
$ source .venv/bin/activate
$ pip3 install gpiod
$ python3 -c "import gpiod; print('OK')"
```
