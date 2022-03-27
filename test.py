import weather
import math

def convert(TheStream):
    global temp, celcius, Cstream
    for temp in TheStream:
        celcius = rount((temp - 32) / 1.8)
        Cstream.append(celcius)

Cstream = []
Fstream = weather.get_forecasts('Blacksburg, VA')

print(Fstream)
convert(Fstream)
print(Cstram)
