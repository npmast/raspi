#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

#define CHIP_NAME   "/dev/gpiochip4"
#define LED_GPIO    14
#define BUTTON_GPIO 15

int main(void)
{
    struct gpiod_chip *chip;
    struct gpiod_line *led_line;
    struct gpiod_line *button_line;
    struct gpiod_line_event event;

    int ret;
    int led_state = 0;

    chip = gpiod_chip_open(CHIP_NAME);
    if (!chip) {
        perror("gpiod_chip_open");
        return 1;
    }

    led_line = gpiod_chip_get_line(chip, LED_GPIO);
    if (!led_line) {
        perror("gpiod_chip_get_line LED");
        gpiod_chip_close(chip);
        return 1;
    }

    button_line = gpiod_chip_get_line(chip, BUTTON_GPIO);
    if (!button_line) {
        perror("gpiod_chip_get_line BUTTON");
        gpiod_chip_close(chip);
        return 1;
    }

    ret = gpiod_line_request_output(led_line, "led", 0);
    if (ret < 0) {
        perror("gpiod_line_request_output");
        gpiod_chip_close(chip);
        return 1;
    }
    // 입력 인터럽트 설정 - 눌림 이벤트 발생
    ret = gpiod_line_request_falling_edge_events_flags(
        button_line,
        "button",
        GPIOD_LINE_REQUEST_FLAG_BIAS_PULL_UP
    );

    if (ret < 0) {
        perror("gpiod_line_request_falling_edge_events_flags");
        gpiod_line_release(led_line);
        gpiod_chip_close(chip);
        return 1;
    }

    printf("버튼 입력 대기 중... Ctrl+C 종료\n");

    while (1) {
        ret = gpiod_line_event_wait(button_line, NULL);        // 커널 이벤트 대기

        if (ret < 0) {
            perror("gpiod_line_event_wait");
            break;
        }

        if (ret == 0) {
            continue;
        }

        ret = gpiod_line_event_read(button_line, &event);        // 이벤트 읽기
        if (ret < 0) {
            perror("gpiod_line_event_read");
            break;
        }

        if (event.event_type == GPIOD_LINE_EVENT_FALLING_EDGE) {
            led_state = !led_state;
            gpiod_line_set_value(led_line, led_state);

            printf("버튼 눌림 → LED %s\n",
                   led_state ? "ON" : "OFF");
        }
    }

    gpiod_line_set_value(led_line, 0);

    gpiod_line_release(button_line);
    gpiod_line_release(led_line);
    gpiod_chip_close(chip);

    return 0;
}
