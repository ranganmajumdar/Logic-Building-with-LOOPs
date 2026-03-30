# Skip all odd numbers and print only the even numbers using break/continue.
for i in range(1, 101):
    if i % 2 != 0:
        continue
    print(i)