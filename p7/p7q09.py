# Print all Perfect numbers between 1 and 1000.
for num in range(1, 1001):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if num == sum_of_divisors:
        print(num)