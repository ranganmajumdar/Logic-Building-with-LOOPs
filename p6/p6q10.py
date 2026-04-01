#  Calculate and print the value of the series 1 + 1/2 + 1/3 + … + 1/n.
def harmonic_series(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += 1 / i
    return total_sum
num_terms = int(input("Enter the number of terms: "))
result = harmonic_series(num_terms)
print(f"The value of the series 1 + 1/2 + ... + 1/{num_terms} is: {result}")