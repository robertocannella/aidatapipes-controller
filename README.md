# Main Micro-Controller Software for A.I. Datpipes



### Summary:
***A.I. Datapipes*** is a software and hardware suite created to aid in heating/cooling system monitoring.  Sensors are strategically placed throughout the system to allow for continued analysis of operations.  Data collected is stored and fed into a Machine Learning model which normalizes the behavior of each component in the system.  These components include pumps, blowers and valves (among others).   Any deviation from the learned normal behavior will trigger an alert.  In most cases, components will sub perform prior to failing completely.  ***A.I. Datapipes*** is a preventative maintenance tool. 

This portion of the ***A.I. Datapipes*** suite is **The Main Controller** for the system.  Other components are maintained separately. They include:
* The DashBoard (live updating)
* Machine Learning Portal 
* Backend API (historic retrieval)

### Purpose of this modules: 

Read and push data from sensors installed near heating/cooling equipment.

### Hardware:
[RaspberryPi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

### Communication
A 1 Wire Network, typically communicating through I2C protocol through a bus master:

### Devices:
For Digital Sensors:
* [1-Wire Plus](https://www.abelectronics.co.uk/p/60/1-wire-pi-plus) (on board [DS2482-100](https://www.abelectronics.co.uk/docs/pdf/ds2482s.pdf): 1-wire bus master)
* [DS19B20](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf): 1-Wire Temperature Sensor
* [DS2438](https://datasheets.maximintegrated.com/en/ds/DS2438.pdf): Repurposed 1-Wire Battery Monitor (on board temp sensor for true humidity calc)
* [HIH-4000-001](https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/en-us/products/sensors/humidity-with-temperature-sensors/hih-4000-series/documents/sps-siot-hih4000-series-product-sheet-009017-5-en-ciid-49922.pdf?download=false): Humidity Sensor

For Analog Sensors:
* [MPC3008](https://ww1.microchip.com/downloads/en/DeviceDoc/21295d.pdf): Analog to Digital Converter
* 10kΩ resistor at 25 °C (outdoor temperature sensor)

Linux Libraries/Drivers:






