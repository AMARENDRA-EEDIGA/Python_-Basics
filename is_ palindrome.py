1.
# Using a function called palindrome for a input String,................,,,,,,

def palindrome(input_string):

    # Two variables are initialized as string date types using empty 
    new_string = input_string.replace(" ","").upper()
    reverse_string = new_string[::-1]
    # compare the "new_string" to the "reverse_string". 
    if new_string==reverse_string:
        # If True, the "input_string" contains a palindrome.
        return True
    # Otherwise, return False.
    return False

print(palindrome("Never Odd or Even")) # Should be True
print(palindrome("abc")) # Should be False
print(palindrome("kayak")) # Should be True

Expected Output.....
True
False
True

2.
# For the numerical value checking is_palindrome..........,,,,,

# Taking the input by the user and converting into intiger
n=int(input("Enter some numbers: "))
# Taking an empty reverse variable with initalizing '0'
reverse=0
# Storing input into a temp variable 
temp=n
# While loop starts form 0 to maximum length of given input
while temp>0:
    # finding remainder means last digit in the value. When dividing with 10 for the value we can get the right-first element in the value
    remainder=temp%10
    # First multiplies reverse with 10 and adds with remainder for to get the value 
    reverse=(reverse*10)+remainder
    # Floor-division with temp to get without decimals
    temp=temp//10
    # comparing the reverse vs input(n)
if reverse==n:
    # Condition is True 
    print("Pallindrome Number is:",n)
else:
    # If Condition is False 
    print("This is not a Pallindrome number. Please try again")


OUTPUT:
Enter some numbers: 16461
Pallindrome Number is: 16461

Enter some numbers: 164352
This is not a Pallindrome number. Please try again


3.
# Without using a function directly checking if is palindrome for a input String.....,,,,,

# Taking an input String
text=input("Enter a string = ")

# First replacing white_spaces by the without_spaces and converting into lower case(Becase python is a case sensitive language) of an given string and storing it into a rev variable
rev=text.replace(" ","").lower()
# Reversing the input by using slicing 
new=rev[::-1]

# Comparing rev vs new Strings
if rev==new:
    print("Palindrom")
else:
    print("Not a palindrom")


OUTPUT:
Enter a string = pop
Palindrom
Enter a string = push
Not a palindrom
