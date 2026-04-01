# Print the series of powers of two: 1 + 2 + 4 + 8 + … + 2ⁿ.
def powers_of_two(n):
    total_sum = 0
    for i in range(n + 1):
        total_sum += 2 ** i
    return total_sum
num_terms = int(input("Enter the number of terms: "))
result = powers_of_two(num_terms)
print(f"The sum of the series 1 + 2 + 4 + ... + 2^{num_terms} is: {result}")