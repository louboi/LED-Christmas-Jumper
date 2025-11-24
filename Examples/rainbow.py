import plasma
import machine
import time
from pimoroni import RGBLED #, Analog

NUM_LEDS = 42 # Change this to the number of LED's you have

DEFAULT_SPEED = 10

UPDATES = 60

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, machine.Pin("PLASMA_DAT"))

user_sw = machine.Pin("USER_SW")
button_a = machine.Pin("BUTTON_A")
button_b = machine.Pin("BUTTON_B")
led = RGBLED("LED_R", "LED_G", "LED_B")
# sense = Analog(plasma2040.CURRENT_SENSE, plasma2040.ADC_GAIN, plasma2040.SHUNT_RESISTOR)

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
        # print("Current =", sense.read_current(), "A")
        count = 0
    time.sleep(1.0 / UPDATES)
