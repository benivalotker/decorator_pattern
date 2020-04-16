from abc import abstractmethod, ABC

# car interface
class Car(ABC):
    @abstractmethod
    def operation(self):
        pass


# decorator inteface
class Decorator(Car):
    def __init__(self, car):
        self._car = car

    @abstractmethod
    def operation(self):
        self._car.operation()


# Cars object
class BasicCar(Car):
    def operation(self):
        print("Basic Car")


class SportCar(Decorator):
    def __init__(self, car):
        super(SportCar, self).__init__(car)

    def operation(self):
        super(SportCar, self).operation()
        print("Adding features of Sports Car.")


class LuxuryCar(Decorator):
    def __init__(self, car):
        super(LuxuryCar, self).__init__(car)

    def operation(self):
        super(LuxuryCar, self).operation()
        print("Adding features of Luxury Car.")