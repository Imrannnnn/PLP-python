""" Assignment 1: Design Your Own Class! 
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation. """

class SmartPhone:
        color = "white"

        def year(self):
            print("this phone is good")

myphone = SmartPhone()
print(myphone.color)


myphone.year()

class Book:
      def __init__(self, bookName, author):
            self.bookName = bookName
            self.author = author

firstbook = Book("Releasing your potential", 'Dr Myles Munroe')
secondbook  = Book("The law of human nature", "Robert Greene")


#Polymorphism
class Car:
      def tyres(self):
            return "4"
      
class Bike:
      def tyres(self):
            return "2"
      
for vehicle in [Car(), Bike()]:
      print(vehicle.tyres())



#inheritance
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels)  


#encapculation 
class Form:
    def __init__(self, Name, age):
        self.__Name = Name   
        self.__age = age     

    def details(self):
        return self.__Name, self.__age  

form = Form("Imran", 25)
name, age = form.details()
print(f"my name is {name}, and my age is  {age}")


