#Class Car
class Car:
    #Contructor to create Car objects
    def __init__(self, Brand, Model, Year, IsAvailable):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.IsAvailable = IsAvailable
    #Method to rent a car
    def RentCar(self):
        self.IsAvailable = False
        #Print car object and status
        print(f"{self.Brand} car model: {self.Model} year: {self.Year} is: NOT AVALIABLE")
    #Method to return a car
    def ReturnCard(self):
        self.IsAvailable = True
        #Print car object and status
        print(f"{self.Brand} car model: {self.Model} year: {self.Year} is: AVALIABLE")
#Car Object 1
car1 = Car("BMW", "M3", "2024", True)
#Car Object 2
car2 = Car("Toyota", "Sequoia", "2025", True)
#Styling
print("=======================================")
#Title
print("MY CARS")
#Styling
print("=======================================")
print(f"* {car1.Brand} {car1.Model} {car1.Year}")
print(f"* {car2.Brand} {car2.Model} {car2.Year}")
#Styling
print("=======================================")
print("AFTER RENTING")
#Styling
print("=======================================")
#Call the rent a car method
car1.RentCar()
car2.RentCar()
#Styling
print("=======================================")
print("AFTER RETURNED")
#Styling
print("=======================================")
#Call the return car method
car1.ReturnCard()
car1.ReturnCard()

#Pushed to GitHub wk12ex3 repo.