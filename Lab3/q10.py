Celsius = [36.5, 37.0, 39.2, 35.6, 38.7] 
Fahrenheit = list(map(lambda c: c * 9/5 + 32, Celsius)) 
below100F = list(filter(lambda f: f <= 100, Fahrenheit)) 
print("Fahrenheit temperatures:", Fahrenheit) 
print("Temperatures at or below 100°F:", below100F)