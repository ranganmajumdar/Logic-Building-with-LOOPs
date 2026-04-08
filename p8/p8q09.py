# Print a Centered Pyramid of Stars
n = 5
for i in range(n):
    # Print spaces before stars
    print(" " * (n - i - 1), end="")
    # Print stars
    print("*" * (2 * i + 1))