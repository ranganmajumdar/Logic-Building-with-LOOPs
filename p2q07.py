# print the factorial of every number from 1 to n using for loop
n = int(input("Enter a number: "))
for num in range(1, n + 1):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")