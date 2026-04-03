# Calculate and print the value of the series
# x − x²/2! + x³/3! − x⁴/4! + ...
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
series_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        series_sum -= x ** i / factorial(i)
    else:
        series_sum += x ** i / factorial(i)
print("The value of the series is:", series_sum)