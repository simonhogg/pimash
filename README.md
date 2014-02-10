pimash
======

Simon's Raspberry Pi Mash Controller for Brewing

Simons-iMac:~ shogg$ ssh pi@10.0.1.33
pi@10.0.1.33's password:
Linux raspberrypi 3.10.24+ #614 PREEMPT Thu Dec 19 20:38:42 GMT 2013 armv6l

pi@raspberrypi ~ $ sudo modprobe w1-gpio
pi@raspberrypi ~ $ sudo modprobe w1-term

pi@raspberrypi /sys/bus/w1/devices/28-000004a1c1e6 $ cat w1_slave
79 01 4b 46 7f ff 07 10 0a : crc=0a YES
79 01 4b 46 7f ff 07 10 0a t=23562

pi@raspberrypi ~ $ sudo apt-get install python-rpi.gpio


