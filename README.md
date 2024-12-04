# LED-Christmas-Jumper

A DIY, led filled, Christmas jumper that is fully customisable and can be hacked to your hearts content.

## Warning!

**The Led strip may get hot in use. Do not wrap tightly or attach to anything that acn be extremely flamable**

## Authors

- [@louboi](https://github.com/louboi)

## Honourable mentions

- [Pimoroni](https://github.com/pimoroni) Maker of the Plasma2040 and the LED strip
- [Raspberry Pi](https://github.com/raspberrypi) Maker of teh RP2040 and many other wonderfull things
- [@paulober](https://github.com/paulober) Maker of the MicroPico extension for VS

## Demo

<p align="center">
    <img width="450" height="800" src="https://github.com/user-attachments/assets/d29a71b4-ea97-493b-b4d2-2bde60be2931" >
</p>

## Prerequisites:
### Kit-List:
- Led string lights
    - I used [these string lights](https://shop.pimoroni.com/products/5m-flexible-rgb-led-wire-50-rgb-leds-aka-neopixel-ws2812-sk6812?variant=40384556171347)
- A controller that is RP2040 based
    - I used a Pimoroni [Plasma 2040](https://shop.pimoroni.com/products/plasma-2040?variant=39410354847827)
- A method of powering them
    - I just used a usb battery bank, however you can just plug it into the wall

## Installation
### Part 1 - Preparing the Plasma2040
#### Part 1.1 - Download the firmware
Go to the [Pimoroni repository](https://github.com/pimoroni/pimoroni-pico) and download the correct image.

Downlad the file with the name that resembles the example below:
```text
pico-v1.xx.x-pimoroni-micropython.uf2
```
#### Part 1.2 - Flash the firmware
- Plug the Plasma2024 in using a usb-c cable
- Press and hold the boot button, and then press the reset button
- Copy the downloaded .uf2 file onto the drive that has appeared labeled "RPI-RP2"
    - Note: Do not add it into any folders just paste it into the root folder
#### Part 1.3 - Connect the LED strip
- Connect the wire with the black dots to the terminal labeled 5V
- Connect the middle wire to the terminal labeled DA
- Connect the final wire to the terminal labeled -

### Part 2 - Start running code on the Plasma2040
#### Method 1 - Thonny
- Download Thonny from [here](https://thonny.org/)
- Open Thonny and click in the bottom right to change interpreter and select "MicroPython (Raspberry Pi Pico)"
    - If this doesn't work then refer to the [wiki](https://github.com/louboi/LED-Christmas-Jumper/wiki) for more help

#### Method 2 - VS Code (My preferred method - and the one used in example images)
- Download VS from [here](https://code.visualstudio.com/)
- Open VS and go to the extension tab and search for "MicroPico" and install it
    - Also ensure you have the python extensions installed
- Plug your Plasma2040 in and it should automatically install
    - If this doesn't work then refer to the [wiki](https://github.com/louboi/LED-Christmas-Jumper/wiki) for more help
