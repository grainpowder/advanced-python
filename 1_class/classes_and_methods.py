class Car:
    """
    Any class inherits 'object' as default unless specified.
    Car.__doc__ contains string defined in this comment block.
    """
    # Class variable : variable that all instances of a class shares(defined between comment block and __init__)
    car_count = 0

    def __init__(self, company, details):
        # Instance variable : variable that is assigned to that instance only(so defined as self._varname)
        self._company = company # Underbar in front of variable name indicates that this is instance variable.
        self._details = details # In fact, leading single underscore itself implies 'internal use' by convention.
        self._id = company[0] + details.get('id')
        Car.car_count += 1
    
    def modify(self, company, details):
        """
        Instance method : method which takes instance(which is 'self') as first input.
        Used to deal with data contained in an instance's namespace.
        Note : Not only class but also method can contain its own __doc__ variable.
        """
        if isinstance(company, str) and isinstance(details, dict):
            new_company = company.lower().capitalize()
            self._company = new_company
            self._details = details
            self._id = new_company[0] + details.get('id')
            return True
        else:
            raise ValueError("Input values are not in expected format")

    @classmethod
    def modify_count(cls, value):
        """
        Class method : method which takes class(which is 'cls') as first input.
        Used to modify, delete, define class variable.
        Note : Requires 'classmethod' decorator in advance.
        """
        if value < 0 or not isinstance(value, int):
            raise ValueError("This method only accepts positive integer")
        else:
            cls.car_count = value

    @staticmethod
    def compare_cars(car1, car2):
        """
        Static method : method which doesn't expect cls or self as first input.
        Used to make function that is somehow related to this class so wrapping it is much neater.
        Note : Requires 'staticmethod' decorator in advance.
        """
        hp_per_price1 = car1._details.get('horsepower') / car1._details.get('price')
        hp_per_price2 = car2._details.get('horsepower') / car2._details.get('price')
        if hp_per_price1 > hp_per_price2:
            return [car1._id, car2._id]
        else:
            return [car2._id, car1._id]

car1 = Car('Ferrari', {'color':'White', 'horsepower':400, 'price':8000, 'id':'SC110'})
print("\n# __class__ variable -------------------------------------------")
# Information on class by which instance is defined
print("\n>>> print(car1.__class__)")
print(car1.__class__)

print("\n# dir function and dir(object) ---------------------------------")
# dir() : returns names of all methods, properties of the object(default: current module)
print("\n>>> print(dir())")
print(dir())
# object : class of built-in methods, properties for defining class
print("\n>>> print(dir(object))")
print(dir(object))

print("\n# dir(class) and its __dict__ variable -------------------------")
# Every class inherits names of 'object' class unless specified otherwise
print("\n>>> print(dir(Car))") 
print(dir(Car))
# Namespace of Car class(class variable included)
print("\n>>> print(Car.__dict__)")
print(Car.__dict__)

print("\n# dir(instance) and its __dict__ variable ----------------------")
# Every instance inherits names of its parent class
print("\n>>> print(dir(car1))") 
print(dir(car1))
# Namespace of car1 instance(class variable excluded)
print("\n>>> print(car1.__dict__)")
print(car1.__dict__)
# So if class variable is called by instance, this variable is searched from inherited names
print("\n>>> print(car1.car_count)")
print(car1.car_count)