# Keep taking numbers from the user and print them until a negative number
#appears, then stop the loop using break / continue logic.
while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    print(f"You entered: {num}")