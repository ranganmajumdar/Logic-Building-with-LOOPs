#print this the number is armstrong or not using do while loop
n = int(input("Enter a number: "))
temp = n
sum = 0
while True:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    if temp == 0:
        break
if sum == n:
    print(f"{n} is an Armstrong number.")
else:    
    print(f"{n} is not an Armstrong number.")