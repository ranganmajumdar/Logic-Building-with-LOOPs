#Calculate and print the value of the series
#1 + x + x² + x³ + … + xⁿ.
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
series_sum = 0
for i in range(n + 1):
    series_sum += x ** i
print("The value of the series is:", series_sum)