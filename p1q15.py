#check if it is an amstrong number or not
num = int(input("Enter a number: "))
original_num = num
sum_of_cubes = 0
while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** 3
    num = num // 10
if original_num == sum_of_cubes:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")