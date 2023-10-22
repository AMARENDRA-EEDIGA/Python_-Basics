# The function accepts a "given_number" variable through its parameters.
def addition_table(given_number):
 
    # The "iterated_number" and "my_sum" variables are initialized with the value of 1. 
    my_sum = 1
 
    # The while loop will run while it is True that the "iterated_number" is less than or equal to 5.
    while iterated_number <= 5:
 
        # The "my_sum" variable is assigned the value of the "given_number" plus the "iterated_number" variables.
        my_sum = given_number + iterated_number
 
        # Test to see if the "my_sum" variable is greater than 20.
        if my_sum > 20:
            # If True, then use the break keyword to exit the loop. 
            break
        # If False, the Python interpreter will move to the next line 
    
      
        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
 
        # Increment the "iterated_number" before the while loop starts over again to print a new "my_sum" value.
        iterated_number += 1
 
 
addition_table(5)
addition_table(17)
addition_table(30)

# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None
