# Find the LCM (Least Common Multiple) of the given number using for loop
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
lcm = max(num1, num2)
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        print("The LCM of", num1, "and", num2, "is:", lcm)
        break
    lcm += 1