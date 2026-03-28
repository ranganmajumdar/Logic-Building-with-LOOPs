# Find the HCF (Highest Common Factor) of the given numbers using for loop.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
hcf = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("The HCF of", num1, "and", num2, "is:", hcf)