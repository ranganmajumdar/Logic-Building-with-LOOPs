# print all palindrome numbers between 1 and 500
def is_palindrome(num):
    return str(num) == str(num)[::-1]

for i in range(1, 501):
    if is_palindrome(i):
        print(i)