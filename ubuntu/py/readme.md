## 라즈베리파이 5
: RPi.GPIO는 Pi5에서 직접 지원되지 않기 때문에 libgpiod 기반을 사용한다.
#### libgpiod  
리눅스 커널에서 제공하는 최신 GPIO(General Purpose Input/Output) 문자 장치에 유저 스페이스가 접근하여 제어할 수 있도록 해주는 C 라이브러리 및 명령줄 도구 모음.  
새로운 표준, 효율성, 안정성, 명령줄 도구, 다양한 언어를 지원한다.  
최신 임베디드 리눅스 환경에서는 필수적인 GPIO 제어 라이브러리이다.  
* gpiod는 리눅스 환경에서 libgpiod 라이브러리를 사용하여 하드웨어의 GPIO핀을 제어하고 상호 작용하기 위한 명령줄 도구이다.
#### 1.필수 패키지  
```c
$ sudo apt update
$ sudo apt install python3-libgpiod
// $ python3 -c "import gpiod; print('OK')"          // 확인
$ gpiodetect                                      // gpio 정치 확인(pi5는 rp1 칩 사용)
```
#### 2. 권한 문제 해결
```c
$ sudo usermod -aG gpio $USER
또는 sudo 를 붙혀 실행한다.
```
#### 3. 가상 환경 설치
```c
$ python3 -m venv --system-site-packages .venv
$ source .venv/bin/activate
$ pip3 install gpiod
$ python3 -c "import gpiod; print('OK')"
```
#### 4. Interrupt  
* 라즈베리파이5는 GPIO 구조가 바꿨다.  
  SoC 내부 GPIO 에서 RP1 칩이라는 외부 컨트롤러를 사용한다.  
  따라서 libgpiod가 필수로 필요하다.  
Polling 방식: val = read_gpio()  
Int 방식: event_wait() => 커널 인터럽트 큐를 기다린다.  
* 설정  
  line.request(  
      type = gpiod.LINE_REQ_EV_BOTH_EDGES  
  )  
  line.event_wait()  
  line.event_read()  
* 종류  
  RISING_EDGE  
  FALLING_EDGE  
  BOTH  
* 내부 동작  
  전압 변화 -> GPIO 감지 -> IRQ 발생 -> 커널 핸들러 실행  

