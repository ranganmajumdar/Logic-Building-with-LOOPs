#Print all prime numbers up to n using nested loops checking.
n = 20  # You can change this value to find prime numbers up to different limits
print(f"Prime numbers up to {n}:")
for num in range(2, n + 1):
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)