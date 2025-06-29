class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        if price > 0:
            self.price = price
        else:
            self.price = None
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.price is not None and self.price <= money and self.owner is None:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif self.owner is not None:
            return "Car already sold"
        elif self.price is not None and self.price > money:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"

vehicle_type = "car"
model = "BMW"
price = 1000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(1300, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)