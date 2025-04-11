class Car:
    
    def __init__(self, Brand, Model, Year, IsAvailable):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.IsAvailable = IsAvailable
        
    def RentCar(self):
        self.IsAvailable = False
        print(f"{self.Brand} car model: {self.Model} year: {self.Year} is: NOT AVALIABLE")
    
    def ReturnCard(self):
        self.IsAvailable = True
        print(f"{self.Brand} car model: {self.Model} year: {self.Year} is: AVALIABLE")
        
car1 = Car("BMW", "M3", "2024", True)
car2 = Car("Toyota", "Sequoia", "2025", True)

print("=======================================")
print("MY CARS")
print("=======================================")
print(f"* {car1.Brand} {car1.Model} {car1.Year}")
print(f"* {car2.Brand} {car2.Model} {car2.Year}")

print("=======================================")
print("AFTER RENTING")
print("=======================================")
car1.RentCar()
car2.RentCar()

print("=======================================")
print("AFTER RETURNED")
print("=======================================")
car1.ReturnCard()
car1.ReturnCard()