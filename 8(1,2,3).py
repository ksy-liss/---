# Задание №1
print(*[int(input()) for _ in range(int(input()))][::-1])


# Задание №2
def mass(brr):
    return brr[-1:] + brr[:-1]


input()
print(*mass(input().split()))


# Задание №3
m_kg, n_rb, coun = int(input()), int(input()), 0
t = sorted([int(input()) for _ in range(n_rb)], reverse=True)
if t[0] > m_kg:
    print("Задача не имеет решения")
    exit()
while len(t):
    coun += 1
    k = m_kg - t.pop(0)
    for i in range(len(t)):
        if t[i] <= k:
            t.pop(i)
            break
print(coun)
