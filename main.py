'''
with decorator can we add methods to object without inherited from other object.
'''
import decorator_

if __name__ == "__main__":
    # create basic car with sport car attribute.
    sports_car = decorator_.SportCar(decorator_.BasicCar())
    sports_car.operation()
    print("-----")

    # create basic car with sport car attribute, and luxury car with sport car attribute that include the basic car attribute.
    sports_luxury_car = decorator_.SportCar(decorator_.LuxuryCar(decorator_.BasicCar()))
    sports_luxury_car.operation()


'''
NOTE: the "super' in operation methods make the all prints.
basic --> super --> luxury
'''