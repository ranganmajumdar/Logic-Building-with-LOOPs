#Find and print the sum of all factors of the given number using for loop
num = int(input("Enter a number: "))
factor_sum = 0
for i in range(1, num + 1):
    if num % i == 0:
        factor_sum += i
print("The sum of factors of", num, "is:", factor_sum)