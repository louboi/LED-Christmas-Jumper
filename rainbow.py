import plasma
from plasma import plasma2040
import time
from pimoroni import RGBLED, Button, Analog

NUM_LEDS = 42 # Change this to the number of LED's you have

DEFAULT_SPEED = 10

UPDATES = 60

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)

user_sw = Button(plasma2040.USER_SW)
button_a = Button(plasma2040.BUTTON_A)
button_b = Button(plasma2040.BUTTON_B)
led = RGBLED(plasma2040.LED_R, plasma2040.LED_G, plasma2040.LED_B)
sense = Analog(plasma2040.CURRENT_SENSE, plasma2040.ADC_GAIN, plasma2040.SHUNT_RESISTOR)

led_strip.start()

speed = DEFAULT_SPEED
offset = 0.0
count = 0

while True:
    speed = min(255, max(1, speed))
    offset += float(speed) / 2000.0
    for i in range(NUM_LEDS):
        hue = float(i) / NUM_LEDS
        led_strip.set_hsv(i, hue + offset, 1.0, 1.0)
    led.set_rgb(speed, 0, 255 - speed)
    count += 1
    if count >= UPDATES:
        print("Current =", sense.read_current(), "A")
        count = 0
    time.sleep(1.0 / UPDATES)
