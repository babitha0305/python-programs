class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand  # Encapsulation: private attribute
        self._model = model
        self._year = year

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def display_info(self):
        print(f"{self._brand} {self._model} ({self._year})")

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self._fuel_type = fuel_type

    def get_fuel_type(self):
        return self._fuel_type

    def set_fuel_type(self, fuel_type):
        self._fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"- Fuel: {self._fuel_type}")

    def start_engine(self):
        print("Car engine started!")

class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self._engine_capacity = engine_capacity

    def get_engine_capacity(self):
        return self._engine_capacity

    def set_engine_capacity(self, engine_capacity):
        self._engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"- Engine: {self._engine_capacity}cc")

    def start_engine(self):
        print("Bike engine started!")

# Example usage
car = Car("Toyota", "Corolla", 2022, "Petrol")
bike = Bike("Yamaha", "R15", 2021, 155)

car.display_info()
car.start_engine()

bike.display_info()
bike.start_engine()