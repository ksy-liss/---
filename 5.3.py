a, b, min = int(input()), int(input()), int(input())
if a >= min and b >= min:
    print("2")
elif a >= min and b < min:
    print("Mike")
elif a < min and b >= min:
    print("Ivan")
elif (a + b) >= min:
    print("1")
else:
    print("0")
