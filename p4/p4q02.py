#Print all possible pairs (i, j) where both i an j range from 1 to n using nested loops.
n = 5  # You can change this value to generate pairs for different ranges
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"({i}, {j})")