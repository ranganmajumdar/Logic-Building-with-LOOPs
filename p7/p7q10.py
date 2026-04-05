# Find the number between 1 and n that has the maximum digit sum, and print that number along with its digit sum.
n = int(input("Enter the value of n: "))
max_digit_sum = 0
number_with_max_sum = 0

for num in range(1, n + 1):
    digit_sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10

    if digit_sum > max_digit_sum:
        max_digit_sum = digit_sum
        number_with_max_sum = num

print("Number with maximum digit sum:", number_with_max_sum)
print("Maximum digit sum:", max_digit_sum)
