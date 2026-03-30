#Generate and print a number triangle pattern using nested loops.
n = 5  # You can change this value to generate a larger or smaller triangle
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  # Print a new line after each row