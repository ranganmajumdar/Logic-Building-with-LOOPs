#Find and print the sum of the Fibonacci series using loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1
fib_sum = 0
for i in range(n):
    fib_sum += a
    a, b = b, a + b
print("The sum of the Fibonacci series is:", fib_sum)
