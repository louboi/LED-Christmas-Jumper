import plasma
from plasma import plasma2040

LEDS = 50
i = 0

led_strip = plasma.WS2812(LEDS, 0, 0, plasma2040.DAT)

led_strip.start()

while i < 50:
    led_strip.set_rgb(i, 0, 0, 0)
    print(i)
    i += 1