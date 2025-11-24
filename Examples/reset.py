import plasma
import machine

LEDS = 50
i = 0

led_strip = plasma.WS2812(LEDS, 0, 0, machine.Pin("PLASMA_DAT"))

led_strip.start()

while i < 50:
    led_strip.set_rgb(i, 0, 0, 0)
    print(i)
    i += 1