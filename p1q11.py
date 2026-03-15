#count and print the total number of digit in a given number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Total number of digits:", count)