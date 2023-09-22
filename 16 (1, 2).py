# 1


class CashRegister:
    def __init__(self):
        self.balance = 0

    def top_up(self, amount):
        self.balance += amount

    def count_1000(self):
        return self.balance // 1000

    def take_away(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно денег в кассе")


# cash_register = CashRegister()
# print(cash_register.count_1000())

# cash_register.top_up(3000)
# print(cash_register.count_1000())

# cash_register.take_away(2000)
# print(cash_register.count_1000())

# cash_register.take_away(5000)


# 2


class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            print("Невозможно уменьшить s ниже 1")

    def count_moves(self, x2, y2):
        x_diff = abs(x2 - self.x)
        y_diff = abs(y2 - self.y)
        return x_diff // self.s + y_diff // self.s


# turtle = Turtle()
# turtle.go_right()
# turtle.evolve()
# turtle.go_up()
# print(turtle.x, turtle.y)

# turtle.go_right()
# turtle.degrade()
# turtle.go_down()
# print(turtle.x, turtle.y)

# print(turtle.count_moves(4,2))
