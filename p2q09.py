# calculate and print the factorial of a number using while loop
n = int(input("Enter a number: "))
factorial = 1
temp = n
while temp > 0:
    factorial *= temp
    temp -= 1
print(f"The factorial of {n} is {factorial}")