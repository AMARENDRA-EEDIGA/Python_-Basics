def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds

# Calling the function and storing it into the a variable called result
result = convert_seconds(5000)
# Printing the result
print(result)

OUTPUT:
(1, 23, 20)

# Here these 3 elements( hours, minutes, seconds ) are stored into the result
hours, minutes, seconds =result
# printing the elements using normal print method
print(hours, minutes, seconds)

OUTPUT:
1 23 20

# Here we are calling the function with giving the new seconds value
hours, minutes, seconds = convert_seconds(1000)
# printing the result
print(hours, minutes, seconds)

OUTPUT:
0 16 40
