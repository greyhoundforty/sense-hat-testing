from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

# Get humidity
humidity = sense.get_humidity()
print(f"Humidity: {humidity:.1f}%")

# Get pressure
pressure = sense.get_pressure()
print(f"Pressure: {pressure:.1f} millibars")

# Get temperature in Celsius
temp_c = sense.get_temperature()
# Convert to Fahrenheit
temp_f = (temp_c * 9/5) + 32

# Print both temperature readings
print(f"Temperature: {temp_c:.1f}°C / {temp_f:.1f}°F")
