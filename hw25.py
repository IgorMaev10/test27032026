class Car:
    def __init__(self, model: str, age: int):
        self.model = model
        self.age = age
        self.owner = None
        self.fuel = 0

    def __str__(self):
        if self.owner:
            output = f'Автомобіль моделі {self.model} віком {self.age} років з {self.fuel}л пального, власником якого є {self.owner}'
        else:
            output = f'Автомобіль моделі {self.model} віком {self.age} років з {self.fuel}л пального'
        return output

    @property
    def characteristic(self) -> str:
        if self.age <= 5:
            condition = 'нове авто'
        elif self.age <= 10:
            condition = 'середній стан'
        else:
            condition = 'старе авто'
        return condition

    @property
    def refueling_needed(self) -> str:
        if self.fuel < 10:
            return "Потрібна заправка"
        else:
            return "Достатньо бензину"

car1 = Car(model="Ford", age=10)
car2 = Car(model="Toyota", age=3)

print(car1.__dict__)
print(car2.__dict__)
car1.fuel = 50
car2.fuel = 75
car1_property = car1.characteristic
car2_property = car2.characteristic
print(car1_property)
print(car2_property)

if car1.fuel > car2.fuel:
    car_with_more_fuel = car1
elif car2.fuel > car1.fuel:
    car_with_more_fuel = car2
else:
    car_with_more_fuel = None

