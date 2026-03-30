#Print the Fibonacci pattern row by row, where each row prints the next Fibonacci numbers using nested loops.
n = 10  # You can change this value to print more or fewer rows of the Fibonacci pattern
a, b = 0, 1
for i in range(n):
    for j in range(i + 1):
        print(a, end=' ')
        a, b = b, a + b  # Update to the next Fibonacci numbers
    print()  # Print a new line after each row