# Write a program that asks the user to input 10 integers, and then
# prints the largest odd number that was entered. If no odd number was
# entered, it should print a message to that effect
print("Largest Absolute Odd")
print("Input 10 numbers")
n = 1
res = 0
while n < 11:
    ans = abs(int(input(f"Enter number {n}/10: ")))
    if ans > res and ans % 2 != 0:
        res = ans
    n += 1
if res == 0:
    print("There is no odd number was entered")
else:
    print(f"Result: {res}")
