from abc import ABC, abstractmethod

# abstract class
class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass
class concreteClass(AbstractClassExample):
    def __init__(self, value, zahl):
        super().__init__(value)
        self.zahl = zahl

    def do_something(self):
        return self.value * self.zahl



class dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self, sound):
        return f"{self.name} says {sound}"
    def speak2(self):
        print('wau wau')
    def addthings(self, a, b):
        self.a=a
        self.b=b
        c = self.a + self.b
        return c
    def returningab(self):
        return self.a, self.b

class JackRussellTerrier(dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak2(self):
        print('wau wau wau')







