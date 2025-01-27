# wisenc2025
Materials for the Mechatronics 101 workshop at the 2025 WISE National Conference. See the [workshop slides](https://docs.google.com/presentation/d/17NoBU563knMwBu_dEoikSRJojj2nbHyHuLxpcGSuef4/edit?usp=sharing) for activity details.

## Module description

Each activity module shows you how to use a sensor or actuator component. For each module, a box houses the circuit for the component (e.g., the photoresistor box shown below), and the power (Vin), ground (GND), and data (DATA) wires coming out of the box are used to connect the component circuit to the microcontroller board. The code used for each module is available in [the modules folder](/modules/).

![Picture of plywood box that houses the circuit for the photoresistor, with the photoresistor mounted at the top of the box.](/figs/box_photo.jpg)

## List of available modules

The following *actuator* activity modules are available:

 - [A0_blink](/modules/A0_blink/) (*used in microcontroller setup*) contains script(s) to control the brightness of the microcontroller board LED.
 - [A1_vibrate](/modules/A1_vibrate/) contains script(s) to control the vibrating of a mini vibration motor.
 - [A2_spin](/modules/A2_spin/) contains script(s) to control the rotation speed of a motor shaft.
 - [A3_buzz](/modules/A3_buzz/) contains script(s) to control the sound volume and frequency of a buzzer.

The following *sensor* activity modules are available:

 - [S0_tactile](/modules/S0_tactile/) contains script(s) to read and print the state (pressed or unpressed) of a pushbutton.
 - [S1_dial](/modules/S1_dial/) contains script(s) to read and print the approximate voltage drop across a rotary potentiometer.
 - [S2_light](/modules/S2_light/) contains script(s) to read and print the approximate voltage drop across a photoresistor.
 - [S3_temperature](/modules/S3_temperature/) contains script(s) to read and print the approximate voltage drop across a thermistor.
 - [S4_motion](/modules/S4_motion/) contains script(s) to read and print the state (motion detected or no motion detected) of a PIR (infrared) sensor. (*See [this Adafruit article](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work) for more on PIR sensors!*)

## Microcontroller setup activity

The setup activity in this workshop generally follows [this guide](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/) from the Raspberry Pi Foundation.

1. Download the **Thonny Python IDE** from [the Thonny website](https://thonny.org).
2. Plug your **Raspberry Pi Pico microcontroller** into a USB-A port in your computer using the provided micro-USB to USB-A cable.
3. Open Thonny. Verify that the **Shell** panel at the bottom of the editor indicates that you are using a Raspberry Pi Pico with the MicroPython interpreter.

![Screenshot of Thonny IDE Shell showing that a Pico microcontroller is being used with MicroPython.](/assets/repl-connected.png)


## Mechatronics activities

### Downloading activity code

You can download files from this repository as a zip file.

![Screenshot of code menu in GitHub showing zip download option](/assets/github_download.png)

To avoid downloading the entire repository, you can also navigate to individual module scripts in the [modules directory](/modules/) and download specific files.

### Running activity code

To run an activity module:

1. Connect the wires from the module box to your microcontroller board in the appropriate pin locations (GND wire to a GND pin, Vin wire to the 3V3 (Vin) pin, and DATA wire to a GPIO pin).
2. Plug the microcontroller into a USB-A port in your computer.
3. If you have not already done so, download the module script files.
4. Open a module script in Thonny.
5. Change the pin number in the script to match the GPIO pin number to which you connected the DATA wire.
6. Run the script.
