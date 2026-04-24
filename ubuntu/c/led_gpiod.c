#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

#define CHIP_NAME "/dev/gpiochip4"
#define LED_GPIO 17

int main(void)
{
    struct gpiod_chip *chip;            // 컨트롤러
    struct gpiod_line *line;            // 컨트롤러의 핀
    int ret;
    // chip: gpiochip4 의 file descriptor 
    chip = gpiod_chip_open(CHIP_NAME);
    if (!chip) {
        perror("gpiod_chip_open");
        return 1;
    }

    line = gpiod_chip_get_line(chip, LED_GPIO);
    if (!line) {
        perror("gpiod_chip_get_line");
        gpiod_chip_close(chip);
        return 1;
    }

    ret = gpiod_line_request_output(line, "led_test", 0);
    if (ret < 0) {
        perror("gpiod_line_request_output");
        gpiod_chip_close(chip);
        return 1;
    }

    while (1) {
        gpiod_line_set_value(line, 1);
        printf("LED ON\n");
        sleep(1);

        gpiod_line_set_value(line, 0);
        printf("LED OFF\n");
        sleep(1);
    }

    gpiod_line_release(line);
    gpiod_chip_close(chip);

    return 0;
}
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
