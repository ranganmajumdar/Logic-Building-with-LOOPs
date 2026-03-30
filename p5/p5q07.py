# Continuously add numbers in a loop and stop the loop when the sum becomes
# greater than 100 using break / continue logic.
total = 0
while True:
    num = int(input("Enter a number: "))
    total += num
    if total > 100:
        print("Total exceeded 100. Stopping the loop.")
        break