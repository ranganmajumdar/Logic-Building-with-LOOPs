#print numbers in an Increasing Sequence (1, 12, 123, 1234, 12345)
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Move to the next line after each row of numbers