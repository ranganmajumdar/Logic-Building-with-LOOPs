# print the value of the factorial using do while loop
n = int(input("Enter a number: "))
factorial = 1
temp = n
while True:
    factorial *= temp
    temp -= 1
    if temp <= 0:
        break
print(f"The factorial of {n} is {factorial}")