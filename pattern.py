from abc import ABC, abstractmethod

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = "Старт"
        return cls._instance

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class TV(Device):
    def turn_on(self):
        return "телевизор включен"

class Radio(Device):
    def turn_on(self):
        return "Радио включено"

class Remote:
    def __init__(self, device):
        self.device = device

    def press_button(self):
        return self.device.turn_on()

class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_fruit(self, fruit):
        pass

class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Book(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)

class Fruit(Item):
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price

    def accept(self, visitor):
        return visitor.visit_fruit(self)

class PriceCalculator(Visitor):
    def visit_book(self, book):
        return book.price * 0.9 
    
    def visit_fruit(self, fruit):
        return fruit.weight * fruit.price
