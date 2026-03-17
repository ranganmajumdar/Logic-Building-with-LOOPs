#print the number of product of all the digits of a given number using while loop using python
n = int(input("Enter a number: "))
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print(f"The product of all the digits is: {product}")