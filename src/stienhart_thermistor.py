################################################################################
#
#   Self-Heating
#   
#   If you have a 10K thermistor + 10K resistor connected between 5V and ground,
#   you'll get about 5V / (10K + 10K) = 0.25mA flowing at all times. 
#   While this isn't a lot of current, it will heat up your thermistor as the 
#   10K thermistor will be dissipating about 0.25mA * 2.5V = 0.625 mW.
#
#   To avoid this heating, you can try connecting the 'top' of the resistor
#   divider to a GPIO pin and set that pin HIGH when you want to read 
#   (thus creating the divider) and then LOW when you are in low power mode
#   (no current will flow from 0V to ground)
#
################################################################################
import sys
import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import math
from services import mongodb_service


# take top of resistor low until measurment is taken
res_top = digitalio.DigitalInOut(board.D26)
res_top.direction = digitalio.Direction.OUTPUT

# for C - F conversion
def celcius_to_fahrenheit(degrees_celcius):
    return (degrees_celcius * 9/5) + 32

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)


# which analog pin to connect
THERMISTORPIN =  AnalogIn(mcp, MCP.P0) 
# resistance at 25 degrees C
THERMISTORNOMINAL = 10000      
# temp. for nominal resistance (almost always 25 C)
TEMPERATURENOMINAL = 25   
# how many samples to take and average, more takes longer
# but is more 'smooth'
NUMSAMPLES =  5
# The beta coefficient of the thermistor (usually 3000-4000)
BCOEFFICIENT = 3892 # Tekmar 070 Outdoor Sensor
# the value of the 'other' resistor
SERIESRESISTOR =  9920 # Measured with Ohmmeter  

# while True:
#     res_top.value = True
#     print('ON')
#     time.sleep(1)
#     print(THERMISTORPIN.value)
#     res_top.value = False
#     print('OFF')
#     time.sleep(60)
#     print(THERMISTORPIN.value)
# take N samples in a row, with a slight delay
while True:

    res_top.value = True
    print('res_top: %d'%(res_top.value))
    samples = []
    average = 0

    print('taking samples...')
    for i in range(NUMSAMPLES):
        samples.append(THERMISTORPIN.value)
        time.sleep(.2)

    # average all the samples out
    for i in range(NUMSAMPLES):
        average += samples[i]
        
    average /= NUMSAMPLES
    print("Average analog reading %.2f"%(average))
    # convert the value to resistance
    average = 65535 / average - 1
    average = SERIESRESISTOR / average

    print("Thermistor resistance %.2f"%(average)); 

    # calculate temperature using steinhart equation

    steinhart = average / THERMISTORNOMINAL;            # (R/Ro)
    steinhart = math.log(steinhart);                    # ln(R/Ro)
    steinhart /= BCOEFFICIENT;                          # 1/B * ln(R/Ro)
    steinhart += 1.0 / (TEMPERATURENOMINAL + 273.15);   # + (1/To)
    steinhart = 1.0 / steinhart;                        # Invert
    steinhart -= 273.15;                                # convert absolute temp to C

    print(celcius_to_fahrenheit(steinhart))
    res_top.value = False
    print('res_top: %d'%(res_top.value))
    time.sleep(60)

