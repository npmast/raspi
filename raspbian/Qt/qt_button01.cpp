// mainwindow 이름의 ui, cpp, h 3개의 파일을 수정한다.
// connect() 로 연결하기
1. mainwindow.ui  
  Forms 폴더에 있다.
  Push Button 과 Label 을 Widget Box에서 가져와 비치한다.
  
2. mainwindow.cpp
  Sources 폴더에 있다.
#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->pushButton, &QPushButton::clicked,
        this, &MainWindow::onButtonClicked);
  /* 람다함수를 사용하면 onButtonClicked()를 별도로 작성할 필요가 없다.
    connect(ui->pushButton, &QPushButton::clicked, this, [=]() {
        ui->label->setText("Hello Qt");    
    });
  */
}

void MainWindow::onButtonClicked() {
  ui->label->setText("Hello Qt");
}

MainWindow::~MainWindow()
{
    delete ui;
}

3. mainwindow.h 
헤더 파일에 slots 를 선언해야 된다.
private slots:
    void onButtonClicked();
*/

/*
람다 함수 사용
connect(ui->pushButton, &QPushButton::clicked, this, [=]() {
    ui->label->setText("Hello Qt");    
});
버튼을 클릭하면 label의 텍스트를 "Hello Qt"로 변경한다.
시그널-슬롯 연결을 람다로 구현한다.
connect(보낸쪽, 시그널, 받는쪽, 처리코드): 이벤트 연결
ui->pushButton: 이벤트를 발생시키는 객체
&QPushButton::clicked: 시그널로 버튼 클릭시 이벤트 발생(함수 포인터 형태). 트리거
this: 이벤트 받는 객체, 현재 MainWindow 객체
[=]() {...}: 람다 함수, [=] 외부 변수들을 값 복사로 캡처
*/
