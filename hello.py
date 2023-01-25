
from dogclasses import dog, JackRussellTerrier, concreteClass
import numpy as np



def main():
    a = np.arange(0, 20)
    print('a', a)
    pinky = dog('pinky', 10)
    print(pinky.age, pinky.name)
    pinky.speak2()
    print(pinky.addthings(a=2, b=3))
    print(pinky.returningab())
    jacky = JackRussellTerrier('jacky', 2)
    jacky.speak2()


    cnc = concreteClass(value=3, zahl=-4)
    print('do smth', cnc.do_something())

if __name__ == "__main__":
    main()