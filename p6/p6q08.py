# Calculate and print the value of the series 1² + 2² + 3² + … + n².
def sum_of_squares(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 2
    return total_sum
num_terms = int(input("Enter the number of terms: "))
result = sum_of_squares(num_terms)
print(f"The sum of the series 1² + 2² + ... + {num_terms}² is: {result}")