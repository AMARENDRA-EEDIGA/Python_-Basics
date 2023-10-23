def is_palindrome(input_string):

    # Two variables are initialized as string date types using empty 
    new_string = input_string.replace(" ","").upper()
    reverse_string = new_string[::-1]

   
    # compare the "new_string" to the "reverse_string". 
    if new_string==reverse_string:

        # If True, the "input_string" contains a palindrome.
        return True
    
		
    # Otherwise, return False.
    return False


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


Expected Output.....
True
False
True
