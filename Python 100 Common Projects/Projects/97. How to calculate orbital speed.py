from math import pi

r = float(input("Insert radius of the orbit(million km): "))
v = float(input("Insert orbital speed(km/s): "))

r = r*1000000

yr = 2*pi*r/v

yr = yr/(60*60*24)

print(round(yr))