# Print Stars and Spaces Alternating. (Stars and blank spaces) (b = blank space here)
n = 10
for i in range(n):
    if i % 2 == 0:
        print("*", end="")
    else:
        print(" ", end="")
print()  # Move to the next line after printing stars and spaces