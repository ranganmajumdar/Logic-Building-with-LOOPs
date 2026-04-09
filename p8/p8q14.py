# 1
# 2 3
# 4 5 6
# 7 8 9 0
# 1 2 3 4 5
# 6 7 8 9 0 1
# 2 3 4 5 6 7 8

n = 7
num = 1
for i in range(1, n + 1): 
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
        if num > 9:  # Reset to 1 after reaching 9
            num = 1
    print()  # Move to the next line after each row of numbers  