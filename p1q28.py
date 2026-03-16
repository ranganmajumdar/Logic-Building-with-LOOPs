#find the smallest digit of a given number
n = int(input("Enter a number: "))
smallest_digit = 9  # Initialize smallest digit to the largest possible digit
while n > 0:
    digit = n % 10  # Get the last digit
    if digit < smallest_digit:
        smallest_digit = digit  # Update smallest digit if current digit is smaller
    n //= 10  # Remove the last digit
print("The smallest digit in the number is:", smallest_digit)