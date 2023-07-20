s, con, vow = input(), 0, 0
a1, e1, i1, o1, u1, y1 = 0, 0, 0, 0, 0, 0
sog, gl = "bcdfghjklmnpqrstvwxz", "aoeiuy"
for i in range(len(s)):
    con += s[i] in sog
    vow += s[i] in gl
print("Количество согласных в слове", s, "=", con)
print("Количество гласных в слове", s, "=", vow)
if vow <= 0:
    print("False (гласных букв нет)")
else:
    for i in ["a", "o", "e", "i", "u", "y"]:
        print(f"Буква {i} встречается {s.count(i)} раз")
