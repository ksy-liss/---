# рекрусивный вывод бинарного представления числа
def bin_rep(num):
    if num > 0:
        bin_rep(num // 2)
        print(num % 2, end="")


# bin_rep(10) #1010


# рекурсивное умножение
def mult(x, y):
    if y == 0:
        return 0
    elif y > 0:
        return x + mult(x, y - 1)
    else:
        return -mult(x, -y)


# result = mult(5, 3)
# print(result) # 15


# рекурсивное возведение в степень
def power(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * power(base, exp - 1)
    else:
        return 1 / power(base, -exp)


# result = power(2, 3)
# print(result)  # 8
