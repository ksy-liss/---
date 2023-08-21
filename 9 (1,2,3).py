# 9.1
n = int(input())
s = list(input().split())[:n]
print(len(set(s)))

# 9.2
print(len(set(input().split()) & (set(input().split()))))

# 9.3
numbers = [int(i) for i in input().split()]
myset = set()

for i in numbers:
    if i in myset:
        print("YES")
    else:
        print("NO")
        myset.add(i)
