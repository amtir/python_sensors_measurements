# Data-logger for sensors
# ADS1x15 ADC Converter 12 bits - FFF  4095.
#
# Pressure Sensor : 0 - 15 Bar (0 - 5 V)
# Plot the sensors measurements
#
# @Date:11.12.2018
# 

# Author: 
# License: Public Domain

import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15
import matplotlib.pyplot as plt


channel = 2  # Channel number
time_period_Sec = 1 # Time period in Seconds [S]
time_freq = 0.01 # 10 ms

measrADC = {'temp':[], 'adcHex':[]}

# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# Start continuous ADC conversions on channel 2 using the previously set gain
# value.  Note you can also pass an optional data_rate parameter.
adc.start_adc(channel, gain=GAIN)
# Once continuous ADC conversions are started you can call get_last_result() to
# retrieve the latest result, or stop_adc() to stop conversions.

# Note you can also call start_adc_difference() to take continuous differential
# readings.  See the read_adc_difference() function in differential.py for more
# information and parameter description.

# Read channel for time_period_Sec seconds and print out its values.
print('Reading ADS1x15 channel ' + str(channel) +  ' for '+ str(time_period_Sec) +' seconds...')
start = time.time()
count=0
while (time.time() - start) <= time_period_Sec:
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    # WARNING! If you try to read any other ADC channel during this continuous
    # conversion (like by calling read_adc again) it will disable the
    # continuous conversion!
    #print(time.time())
    print('{0} | Channel 2: {1}'.format(time.time(), value))
    print('{0} , {1}'.format(time.time(), value)) # CSV format
    count = 1 + count
    #t.append( count )
    (measrADC['temp']).append( count )
    #sens.append(value)
    (measrADC['adcHex']).append( value )
    
    # Sleep for 10 milliseconds.
    time.sleep(time_freq)

# Stop continuous conversion.  After this point you can't get data from get_last_result!
adc.stop_adc()

plt.plot(measrADC['temp'], measrADC['adcHex'], 'bo', measrADC['temp'], measrADC['adcHex'], 'k')
plt.show()



