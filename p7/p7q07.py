# Find & print the sum of odd digits & the sum of even digits of the given number
num = int(input("Enter a number: "))
sum_odd = 0
sum_even = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit
    num //= 10
print("Sum of odd digits:", sum_odd)
print("Sum of even digits:", sum_even)