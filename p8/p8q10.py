# Print Stars and Spaces Alternating. (Stars and blank spaces) (b = blank space here)
# Simple alternating pattern on one line
n = 10
for i in range(n):
    if i % 2 == 0:
        print("*", end=" ")
    else:
        print(" ", end=" ")
print() 