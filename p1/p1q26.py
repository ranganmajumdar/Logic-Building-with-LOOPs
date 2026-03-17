# print the HCF of two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
hcf = 1  # Initialize HCF to 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i  # Update HCF to the current common factor
print("The HCF of", num1, "and", num2, "is:", hcf)