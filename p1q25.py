# find and print the sum of all factor of given numbers
n = int(input("Enter a number: "))
sum_of_factors = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum_of_factors += i
print("Sum of factors of", n, "is:", sum_of_factors)