/* gpiod v2 - led on/off */
#include <gpiod.h>                           // libgpiod API
#include <unistd.h>
#include <stdio.h>

#define CHIP "/dev/gpiochip0"                // gpiodetect 확인. 사용칩 확인

int main(void)
{
    struct gpiod_chip *chip;
    struct gpiod_line_settings *settings;    // GPIO 설정
    //struct gpiod_line_config *config;        // GPIO 동작 설정
    struct gpiod_request_config *req_cfg;    // 요정 메타 정보
    struct gpiod_line_request *req;          // 실제 GPIO 객체

    unsigned int lines[] = {17};             // ← 반드시 배열/변수

    chip = gpiod_chip_open(CHIP);            // CHIP 을 열어 디스크립트를 얻는다(GPIO 드라이버 연결)

    settings = gpiod_line_settings_new();    // 빈 객체 생성
    gpiod_line_settings_set_direction(
       settings,
       GPIOD_LINE_DIRECTION_OUTPUT            // 출력 모드 설정
    );
    config = gpiod_line_config_new();        // 빈 객체 생성
    gpiod_line_config_add_line_settings(    // 17번핀 settings 적용
       config,
       lines,
       1,
       settings
    );                                       
    req = gpiod_chip_request_lines(        // GPIO 17을 현재 프로세스가 점유
       chip,
       NULL,
       config
    );                                       

    while (1) {
        gpiod_line_request_set_value(req, 17, 1);
        sleep(1);
        gpiod_line_request_set_value(req, 17, 0);
        sleep(1);
    }
    gpiod_line_request_release(req);         // 점유 해제
    gpiod_chip_close(chip);                  // 디바이스 닫기
}

