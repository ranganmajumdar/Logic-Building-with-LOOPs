#Calculate and print the value of the series
#1! + 2! + 3! + … + n!.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter the value of n: "))
series_sum = 0
for i in range(1, n + 1):
    series_sum += factorial(i)
print("The value of the series is:", series_sum)