1. mainwindow.ui
  Push Botton 2개를 배치하고 ON 과 OFF 버튼으로 지정한다.
  textEdit 를 가져온다.
  Edit Signals/Slots 
  ON 버튼을 우 클릭하여 Go to slot... 을 클릭한다. > clicked()
2. mainwindow.cpp
  on_onButton_clicked() 와 on_offButton_clicked() 이벤트 함수가 생성되어 있다.
  아래와 같이 작성한다.

void MainWindow::on_onButton_clicked()
{
    ui->textEdit->setText("LED on");
}

void MainWindow::on_offButton_clicked()
{
    ui->textEdit->setText("LED off");
}
  작성이 끝나면 run을 한다.
