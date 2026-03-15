#check wether the given number is prime or not using while loop
num = int(input("Enter a number: "))
if num <= 1:
    print("The number is not prime.")
else:
    is_prime = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")