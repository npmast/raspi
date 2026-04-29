from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(                    // 객체 생성
    i2c_expander='PCF8574',       // i2c 확장 칩
    address=0x27,                 // i2c 장치 주소
    port=1,                       // i2c 버스 주소
    cols=16,                      // 한 줄 크기
    rows=2,                       // 줄 크기
    charmap='A00'                 // 문자 인코딩(기본)
)

try:
    lcd.clear()
    lcd.write_string("Raspberry Pi 5")          // 현재 위치에 문자열 출력
    lcd.crlf()                                  // 줄 바꿈
    lcd.write_string("1602 LCD OK")
    time.sleep(20)

finally:
    lcd.clear()                                 // 화면 지움
    lcd.close(clear=True)
# lcd.cursor_pos = (1, 0):    커서 위치 지정
# lcd.display_enabled = False / True:    디스플레이 오프/온
# lcd.backlight_enabled = True / False:  백라이트 제
