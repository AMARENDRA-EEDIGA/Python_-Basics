# This function counts the number of integer factors for a 
# "given_number" 

def count_factors(given_number):
 
  # To include the "given_number" variable as a "factor", initialize the "factor" variable with the value 1 
  
  factor = 1
  count = 1
 
  # This "if" block will run if the "given_number" equals 0.
  if given_number == 0:
    # If True, the return value will be 0 factors. 
    return 0
 
  # The while loop will run while the "factor" is still less than the "given_number" variable.
  while factor < given_number:
     # The modulo operator % is used to test for a remainder.
    if given_number % factor == 0:
    
      count += 1
    # When exiting the if block, increment the "factor" variable by 1
   
    factor += 1
 
  # it will return the value of the "count" variable.
  return count
 
print(count_factors(0)) # Count value will be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8,
# and 4x6). 


# Expected Output is...
0
2
4
8
