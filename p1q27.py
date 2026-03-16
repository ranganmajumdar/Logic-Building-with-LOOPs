# print the LCM of two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
lcm = max(num1, num2)  # Start with the maximum of the two numbers
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break  # Found the LCM
    lcm += 1  # Increment lcm to check the next number
print("The LCM of", num1, "and", num2, "is:", lcm)