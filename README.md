# LED-Christmas-Jumper

A DIY, led filled, Christmas jumper that is fully customisable and can be hacked to your hearts content.

## Warning!

**The Led strip may get hot in use. Do not wrap tightly or attach to anything that can be extremely flamable**

## IMPORTANT NOTICE!
**VSC MAY NOT WORK ON YOUR DEVICE IF IT USES WINDOWS ON ARM. I AM AWARE AND WORKING TO FIX THIS.**

## Authors

- [@louboi](https://github.com/louboi)

## Honourable mentions

- [Pimoroni](https://github.com/pimoroni) Maker of the Plasma2040 and the LED strip
- [Raspberry Pi](https://github.com/raspberrypi) Maker of the RP2040 and many other wonderfull things
- [@paulober](https://github.com/paulober) Maker of the MicroPico extension for VS

## Demo

<p>
    <img width="337" height="600" src="https://github.com/user-attachments/assets/d29a71b4-ea97-493b-b4d2-2bde60be2931" >
    <img width="471" height="600" src="https://github.com/user-attachments/assets/f3a6f59b-0886-4add-82b6-390fbecde55c" >
</p>

## Prerequisites:
### Kit-List:
- Led string lights
    - I used [these string lights](https://shop.pimoroni.com/products/5m-flexible-rgb-led-wire-50-rgb-leds-aka-neopixel-ws2812-sk6812?variant=40384556171347)
- A controller that is RP2040 based
    - I used a Pimoroni [Plasma 2040](https://shop.pimoroni.com/products/plasma-2040?variant=39410354847827)
- A method of powering them
    - I just used a usb battery bank, however you can just plug it into the wall (just remember to unplug it when you move!)

## Installation
### Part 1 - Preparing the Plasma2040
#### Part 1.1 - Download the firmware
Go to the new dedicated [Plasma repository](https://github.com/pimoroni/plasma) and download the correct image.

Downlad the file with the name that resembles the example below:
```
plasma_2040-Vx.x.x-micropython[-with-filesystem].uf2
```
#### Part 1.2 - Flash the firmware
- Plug the Plasma2024 in using a usb-c cable
- Press and hold the boot button, and then press the reset button
- Copy the downloaded .uf2 file onto the drive that has appeared labeled "RPI-RP2"
    - Note: Do not add it into any folders just paste it into the root folder
#### Part 1.3 - Connect the LED strip
- Connect the wire with the black dots to the terminal labeled **"5V"**
- Connect the middle wire to the terminal labeled **"DA"**
- Connect the final wire to the terminal labeled **"-"**

### Part 2 - Prepare to start running code on the Plasma2040
#### Editor 1 - Thonny
- Download Thonny from [here](https://thonny.org/)
- Open Thonny and click in the bottom right to change interpreter and select "MicroPython (Raspberry Pi Pico)"
    - If this doesn't work then refer to the [wiki](https://github.com/louboi/LED-Christmas-Jumper/wiki) for more help

#### Editor 2 - VS Code (My preferred editor - and the one used in example images)
- Download VS from [here](https://code.visualstudio.com/)
- Open VS and go to the extension tab and search for "Raspberry Pi Pico" and install it
    - Ensure the all dependencies are installed
- Plug your Plasma2040 in -I dont know what happens next yet-
    - If this doesn't work then refer to the [wiki](https://github.com/louboi/LED-Christmas-Jumper/wiki) for more help

### Part 3 - Actually run code on the Plasma2040
#### Editor 1 - Thonny
- Just write your code and press run at the top, or press F5

#### Editor 2 - VS Code (My preferred editor - and the one used in example images)
- Make a new folder and open it in VS
- Open the file explorer tab and click on create pico project
- Make a python file and code away
- Optionally, delete the pre-existing blink.py file

### Part 3 (Optional) - Make code run on the Plasma2040 automatically when power is connected
- Make a new python file using one of the methods described above
- Save the file as main.py on your computer
    - It is important to save it as main.py as this is will be the only file automatically run
- Upload the file to the Plasma2040
    - In Thonny click save as and then select the "MicroPython device" box
    - In VS Right Click on the main.py file and then select "upload file to Pico"
