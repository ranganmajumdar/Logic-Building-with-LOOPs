# Print the Fibonacci series up to the required number of terms

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
num_terms = int(input("Enter the number of terms: "))
fibonacci(num_terms)