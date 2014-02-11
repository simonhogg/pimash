pimash
======

#Simon's Raspberry Pi Mash Controller for Brewing

##Assumptions

###Hardware

Assumes that you have a DS18B20 1-Wire digital temperature sensor connected to GPIO4 and a relay connected to GPIO1.

The relay controls a heat source that will cause the temperature to rise. I use an eBIAB setup where the relay is an SSR connected to an electric heating element.

###Software

Right now, I require a web client to continually ping the server to keep the control loop alive.

The following code was necessary during initial setup. You'll likely want to add the two kernel modules to some more permanent location.

```
Linux raspberrypi 3.10.24+ #614 PREEMPT Thu Dec 19 20:38:42 GMT 2013 armv6l

pi@brewery~ $ sudo modprobe w1-gpio
pi@brewery ~ $ sudo modprobe w1-term

pi@brewery /sys/bus/w1/devices/28-000004a1c1e6 $ cat w1_slave
79 01 4b 46 7f ff 07 10 0a : crc=0a YES
79 01 4b 46 7f ff 07 10 0a t=23562

pi@brewery ~ $ sudo apt-get install python-rpi.gpio

```
