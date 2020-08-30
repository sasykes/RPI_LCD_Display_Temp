# RPI_LCD_Display_Temp
Python Scripts to show CPU and GPU temp on a 16x2 LCD with i2c module.

There are three python scripts needed to display your Raspberry Pi CPU and GPU temp on a 16x2 LCD display, lcddriver.py i2c_lib.py and temp.py. I am using an i2c module soldered to my LCD display. You can watch Fuzz The Pi Guy's excellent video walk through, direct link - https://youtu.be/2DLv_0hqErE and my video showing my setup here - https://youtu.be/CwawPmiWfbk for visual details.

Put the scripts in /home/pi/ directory. Make sure the i2c address matchesline5 in lcddriver.py...

open console and run the following command:

i2cdetect -y 1

Mine shows...

pi@raspberrypi:~ $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --   

This matches line 5 in lcddriver.py...

ADDRESS = 0x27     #Update Address For LCD Here

Connect LCD i2c Pins to RPI:
SCL - GPIO 3 (pin no 5)
SDA - GPIO 2 (pin no 3)
VCC - 5V     (pin no 2)  (my fan power in on pin 4)
GND - Ground (pin no 14) (my fan ground is on pin 6)

Edit Crontab:

sudo crontab -e

Add the following to your crontab:

@reboot python /home/pi/temp.py &

Reboot your Pi to enable display
