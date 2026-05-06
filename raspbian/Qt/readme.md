## Qt Creator

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
#### Qt Creator 프로젝트 생성
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
#### 생성 파일  
Qt Widgets  프로젝트를 생성하면 기본적으로 여러 파일이 자동 생성된다.
이 파일들을 각각 역할이 다르며, Qt의  GUI 구조를 이루는 핵심 요소이다.
1. main.cpp  
   프로그램 시작점
```c++
#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    MainWindow w;
    w.show();

    return a.exec();
}
```
* QApplication 생성  
* MainWindow 객체 생성  
* GUI 실행 루프 시작  
2. mainwindow.h  
   메인 윈도우 클래스 선언 파일. 헤더파일이다. *함수 선언*
```c++
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;                                // 전방 선언
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow            // Qt Widgets 메인 창 클래스 QMainWindow
{
    Q_OBJECT                   // Qt의 Meta-Object System 활성화 매크로로 Qt 기능을 담당한다.
                                // signal/slot, RTTI확장, 자동 슬롯 연결
public:
    MainWindow(QWidget *parent = nullptr);            // 생성자
    ~MainWindow();

private:
    Ui::MainWindow *ui;        // Qt Designer가 만든 UI 객체를 가리키는 포인터
};
#endif // MAINWINDOW_H
```
* 클래스 구조 선언
* 함수 선언
* 슬롯(signal/slot) 선언
* UI 객체 포인터 보관
3. mainwindow.cpp  
  메인 윈도우 실제 동작. *핵심 로직*
```c++
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)        // 생성자
    : QMainWindow(parent)            // 부모 클래스 QMainWindow 생성자 호출
    , ui(new Ui::MainWindow)        // 초기화 리스트에서 멤버 ui 객체 생성
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}
```
* 버튼 클릭 동작 작성
* signal/slot 연결
* 실제 로직 구현
* 예:
```c++
connect(ui->pushButton, &QPushButton::clicked,
        this, &MainWindow::onButtonClicked);
```
4. mainwindow.ui  
   GUI 디자인 파일. XML 형식. Qt Designer 가 사용하는 파일. *GUI 디자인*  
* 버튼 배치  
* 라벨 배치  
* 창 크기 설정  
*  GUI 시각적 설계
5. ui_mainwindow.h  
   Qt가 .ui 파일을 컴파일해서 build 폴더 내부에 자동 생성된다.
```c
ui->pushButton
ui->label
```

