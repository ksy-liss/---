class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seatint_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


autobus = Transport("Renault Logan", 180, 12)

print(
    f"Название атомобиля: {autobus.name}. Скорость: {autobus.max_speed}. Пробег: {autobus.mileage}."
)
print(autobus.seatint_capacity(50))
