# Find and print the sum of the Fibonacci series up to the required number of terms
def fibonacci_sum(n):
    a, b = 0, 1
    count = 0
    total_sum = 0
    while count < n:
        total_sum += a
        a, b = b, a + b
        count += 1
    return total_sum
num_terms = int(input("Enter the number of terms: "))
result = fibonacci_sum(num_terms)
print(f"The sum of the Fibonacci series up to {num_terms} terms is: {result}")