import plasma
import machine
import time

LEDS = 50
i = 0
x = 0

led_strip = plasma.WS2812(LEDS, 0, 0, machine.Pin("PLASMA_DAT"))

led_strip.start()

while True:
    while i != 49:
        x = i + 6
        led_strip.set_rgb(x, 0, 0, 80)
        x = i + 5
        led_strip.set_rgb(x, 0, 0, 100)
        x = i + 4
        led_strip.set_rgb(x, 0, 0, 120)
        x = i + 3
        led_strip.set_rgb(x, 0, 0, 140)
        x = i + 2
        led_strip.set_rgb(x, 0, 0, 160)
        x = i + 1
        led_strip.set_rgb(x, 0, 0, 180)
        led_strip.set_rgb(i, 0, 0, 200)
        i += 1
        led_strip.set_rgb(i, 0, 0, 200)
        x = i - 1
        led_strip.set_rgb(x, 0, 0, 180)
        x = i - 2
        led_strip.set_rgb(x, 0, 0, 160)
        x = i - 3
        led_strip.set_rgb(x, 0, 0, 140)
        x = i - 4
        led_strip.set_rgb(x, 0, 0, 120)
        x = i - 5
        led_strip.set_rgb(x, 0, 0, 80)
        x = i - 6
        led_strip.set_rgb(x, 0, 0, 0)
        time.sleep(0.05)
    i = 0
    led_strip.set_rgb(49, 0, 0, 160)
    time.sleep(0.02)
    led_strip.set_rgb(48, 0, 0, 140)
    time.sleep(0.02)
    led_strip.set_rgb(47, 0, 0, 120)
    time.sleep(0.02)
    led_strip.set_rgb(46, 0, 0, 100)
    time.sleep(0.02)
    led_strip.set_rgb(45, 0, 0, 80)
    time.sleep(0.02)
    led_strip.set_rgb(44, 0, 0, 0)

    time.sleep(0.02)
    led_strip.set_rgb(49, 0, 0, 140)
    time.sleep(0.02)
    led_strip.set_rgb(48, 0, 0, 120)
    time.sleep(0.02)
    led_strip.set_rgb(47, 0, 0, 100)
    time.sleep(0.02)
    led_strip.set_rgb(46, 0, 0, 80)
    time.sleep(0.02)
    led_strip.set_rgb(45, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(44, 0, 0, 0)

    time.sleep(0.02)
    led_strip.set_rgb(49, 0, 0, 120)
    time.sleep(0.02)
    led_strip.set_rgb(48, 0, 0, 100)
    time.sleep(0.02)
    led_strip.set_rgb(47, 0, 0, 80)
    time.sleep(0.02)
    led_strip.set_rgb(46, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(45, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(44, 0, 0, 0)

    time.sleep(0.02)
    led_strip.set_rgb(49, 0, 0, 100)
    time.sleep(0.02)
    led_strip.set_rgb(48, 0, 0, 80)
    time.sleep(0.02)
    led_strip.set_rgb(47, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(46, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(45, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(44, 0, 0, 0)

    time.sleep(0.02)
    led_strip.set_rgb(49, 0, 0, 80)
    time.sleep(0.02)
    led_strip.set_rgb(48, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(47, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(46, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(45, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(44, 0, 0, 0)

    time.sleep(0.02)
    led_strip.set_rgb(49, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(48, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(47, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(46, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(45, 0, 0, 0)
    time.sleep(0.02)
    led_strip.set_rgb(44, 0, 0, 0)