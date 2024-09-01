# Find the cube root of perfect cube
x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):
    ans += 1
print("Ans: ", ans)
if ans**3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        # inverse
        ans = -ans
    print(f"Cube root of {x} is {ans}")
