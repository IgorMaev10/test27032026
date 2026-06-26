class Transport:
    def __init__(self, fuel: float, condition: int):
        self.fuel = fuel
        self.condition = condition

    @property
    def is_working(self) -> bool:
        if self.condition < 40:
            return False
        else:
            return True

    def __str__(self) -> str:
        if self.is_working:
            return f'Пальне: {self.fuel}л, задовільний технічний стан'
        else:
            return f'Пальне: {self.fuel}л, незадовільний технічний стан'

    def move(self, distance: float):
        if not self.is_working or self.fuel == 0:
            print ("movement is impossible")
        self.condition -= 1
        self.fuel -= distance * 0.1
        if self.fuel < 0:
            raise ValueError ("fuel can`t be less than 0")

class Car (Transport):
    def __init__(self, model: str):
        super().__init__(fuel=50, condition=100)
        self.model = model

class Truck (Transport):
    def __init__(self, name: str):
        super().__init__(fuel=120, condition=100)
        self.name = name

class Motorcycle (Transport):
    def __init__(self, brand: str):
        super().__init__(fuel=20, condition=100)
        self.brand = brand

car = Car(model="Volkswagen")
truck = Truck(name="Volvo")
motorcycle = Motorcycle(brand="Honda")

car.move(distance=50)
print(car)
print(truck.is_working)
print(motorcycle.__dict__)
truck.condition = 10
truck.move(distance=100)
motorcycle.fuel = 1
motorcycle.move(distance=200)
print(motorcycle.__dict__)

class ServiceStation:
    def __init__(self):
        pass
    def repair(transport_unit: Transport):
        transport_unit.condition = 100

ServiceStation.repair(transport_unit=truck)
print(truck.__dict__)