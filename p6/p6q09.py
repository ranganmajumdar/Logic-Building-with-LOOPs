# Calculate and print the value of the series 1³ + 2³ + 3³ + … + n³.
def sum_of_cubes(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 3
    return total_sum
num_terms = int(input("Enter the number of terms: "))
result = sum_of_cubes(num_terms)
print(f"The sum of the series 1³ + 2³ + ... + {num_terms}³ is: {result}")