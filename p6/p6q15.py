#Check whether the given number is a Strong number, where the number equals the
# sum of factorials of its digits.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number: "))
temp = number
strong_sum = 0
while temp > 0:
    digit = temp % 10
    strong_sum += factorial(digit)
    temp //= 10
if strong_sum == number:
    print(number, "is a Strong number.")
else:   
    print(number, "is not a Strong number.")