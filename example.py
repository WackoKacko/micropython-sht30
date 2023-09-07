from sht30 import SHT30
import utime

sensor = SHT30()

if sensor.is_present():
    print("Sensor is present!")
else:
    print("SHT30 not connected! Error!")

# Initialize the variable to store the last time a measurement was taken (for non-blocking printing)
last_time = utime.ticks_ms()

while True:
    current_time = utime.ticks_ms()

    # Check if 500ms has elapsed since the last measurement
    if utime.ticks_diff(current_time, last_time) >= 500:
        last_time = current_time  # Update the last_time variable
        temperature, humidity = sensor.measure()

        # Format the temperature and humidity to one decimal place
        print(f'Temperature: {temperature:.1f}C, RH: {humidity:.1f}%')
