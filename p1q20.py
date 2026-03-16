#find and print the sum of fibonacci series up to n terms
n = int(input("Enter the number of terms: "))
a, b = 0, 1
sum_of_fibonacci = 0
for _ in range(n):
    sum_of_fibonacci += a
    a, b = b, a + b
print("Sum of Fibonacci series up to", n, "terms:", sum_of_fibonacci)