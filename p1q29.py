# print the largest digit of a given number
n = int(input("Enter a number: "))
largest_digit = 0  # Initialize largest digit to the smallest possible digit
while n > 0:
    digit = n % 10  # Get the last digit
    if digit > largest_digit:
        largest_digit = digit  # Update largest digit if current digit is larger
    n //= 10  # Remove the last digit
print("The largest digit in the number is:", largest_digit)