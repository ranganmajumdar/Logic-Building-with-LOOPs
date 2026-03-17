#reverse the given number and print the reversed value
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print("Reversed number:", reversed_num)