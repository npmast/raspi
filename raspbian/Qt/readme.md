#### 설치
```c
$ sudo apt update
$ sudo apt upgrade -y
$ sudo apt install -y build-essential cmake gdb
$ sudo apt install -y qt6-base-dev qt6-base-dev-tools
$ sudo apt install -y \
    qt6-tools-dev \
    qt6-tools-dev-tools \
    qml6-module-qtquick \
    qml6-module-qtquick-controls
$ sudo apt install -y qtcreator
$ qmake --version
```
#### Qt Creator  
menu > Programming > Qt Creator  
Create Project... > Appplication(Qt) > Qt Widgets Application > Choose...  
Name 와 Create in 을 설정한다. > build system 을 설정한다. qmake 는 qt 의 전용 빌드시스템이다.  
Class Information 은 Next 로 넘어가고 설정이 끝나면 maic.cpp 가 만들어 진다.
```c
- main.cpp
#include "mainwindow.h"                    // 사용자 정의 클래스 Mainwindow 선언

#include <QApplication>                    // Qt GUI 애플리케이션의 핵심 클래스

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);          // Qt GUI 초기화, 이벤트 생성, OS 와 연결, 반드시 GUI 프로그램에 1개 존재
    MainWindow w;                        // 사용자 정의 윈도우 객체 생성(화면에 표시될 GUI 객체)
    w.show();                            // 윈도우 객체 화면에 띄움
    return a.exec();                     // 동작 시작, 종료 시 까지 블로킹 상태
}
```
Build > Build Project "..." > 좌측 하단의 run 클릭
