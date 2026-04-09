# Print Repeated Numbers per Row (Same Number Repeated)
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()  # Move to the next line after each row of numbers