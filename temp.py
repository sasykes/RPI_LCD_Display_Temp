import lcddriver
import time
import commands

display = lcddriver.lcd()

def get_cpu_tempC():
        tempFile = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = tempFile.read()
        tempFile.close()
        return float(cpu_temp)/1000

def get_gpu_tempC():
        gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
        return float(gpu_temp)


while True:
        cpu_tempC = get_cpu_tempC()
        gpu_tempC = get_gpu_tempC()

        cpuT = "CPU temp: %.2f" % cpu_tempC

        gpuT = "GPU temp: %.2f" % gpu_tempC

        display.lcd_display_string(cpuT + "C", 1)
        display.lcd_display_string(gpuT + "C", 2)
        time.sleep(10) # change this number to change seconds between updates
