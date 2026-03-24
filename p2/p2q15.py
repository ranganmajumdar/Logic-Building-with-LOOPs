# Calculate and print the sum of even digits and the sum of odd digits of the given number separately.
num = int(input("Enter a number: "))
sum_even_digits = 0
sum_odd_digits = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum_even_digits += digit
    else:
        sum_odd_digits += digit
    num //= 10
print(f"The sum of even digits is: {sum_even_digits}")
print(f"The sum of odd digits is: {sum_odd_digits}")