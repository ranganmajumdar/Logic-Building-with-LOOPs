# Take 5 numbers as input, skip any number that is 0 using continue, and
# calculate the sum of the remaining numbers using break / continue logic.
total = 0
for _ in range(5):
    num = int(input("Enter a number: "))
    if num == 0:
        continue
    total += num
print(f"The sum of the remaining numbers is: {total}")