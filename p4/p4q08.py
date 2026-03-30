#Print all Pythagorean triplets whose values are less than or equal to n using nested loops.
n = 20  # You can change this value to find Pythagorean triplets up to different limits
print(f"Pythagorean triplets with values less than or equal to {n}:")
for a in range(1, n + 1):
    for b in range(a, n + 1):  # Start from a to avoid duplicates
        c = (a**2 + b**2)**0.5
        if c.is_integer() and c <= n:
            print(f"({a}, {b}, {int(c)})")