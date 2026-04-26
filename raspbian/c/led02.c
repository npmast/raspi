$ nano led01.c
```c
#include <gpiod.h>
#include <unistd.h>
#include <stdio.h>

#define CHIP "/dev/gpiochip4"

int main(void)
{
    struct gpiod_chip *chip;
    struct gpiod_line_settings *settings;
    struct gpiod_line_config *config;
    struct gpiod_request_config *req_cfg;
    struct gpiod_line_request *req;

    unsigned int lines[] = {17};   // ← 반드시 배열/변수

    chip = gpiod_chip_open(CHIP);

    settings = gpiod_line_settings_new();
    gpiod_line_settings_set_direction(settings, GPIOD_LINE_DIRECTION_OUTPUT);

    config = gpiod_line_config_new();
    gpiod_line_config_add_line_settings(config, lines, 1, settings);

    req_cfg = gpiod_request_config_new();
    gpiod_request_config_set_consumer(req_cfg, "led");

    req = gpiod_chip_request_lines(chip, req_cfg, config);

    while (1) {
        gpiod_line_request_set_value(req, 17, 1);
        sleep(1);
        gpiod_line_request_set_value(req, 17, 0);
        sleep(1);
    }
}
```
/*
    strcut gpiod_chip {
        int fd;
        char name[32];
        unsigned int num_line;
    };
    사용 code: chip = gpiod_chip_open("/dev/gpiochip4"); 
    
    struct gpiod_line {        // GPIO 개별 핀
        struct gpiod_chip* chip;
        unsigned int offset;
    };
    사용 code: line = gpiod_chip_get_line(chip, 14);
*/
```
