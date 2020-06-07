"""
Magic methods are methods surrounded by dunder that adds useful built-in functionalities to a class.
In this module, really basic elements of them are covered just to show how this works.
https://docs.python.org/3/reference/datamodel.html#specialnames provides full list of magic methods.
"""


class GreenSlime:
    """
    Imagine a creature GreenSlime whose mass can be calculated as (height) * (weight) / 2.
    Also, it can be compounded with other GreenSlime by certain rule.
    Following magic methods can be used to define how they interact with each other.
    """
    environment = 0.9

    def __init__(self, height, weight):
        self._height = height
        self._weight = weight
        self._mass = (height * weight) / 2

    @classmethod
    def modify_environment_constant(cls, value):
        if value < 0 or value > 1:
            raise ValueError("Real value between 0 and 1 is expected")
        else:
            cls.environment = value

    def __add__(self, greenslime):
        """
        Two slimes can compound to become one slime.
        Size of resulting slime is affected by surrounding environment.
        """
        new_height = round((self._height + greenslime._height) * GreenSlime.environment, 4)
        new_weight = round((self._weight + greenslime._weight) * GreenSlime.environment, 4)
        return {'height':new_height, 'weight':new_weight}

    def __mul__(self, n):
        """
        Resulting slime when same n-1 slime of same height, weight are compunded.
        """
        new_height = round((self._height * n) * GreenSlime.environment, 4)
        new_weight = round((self._weight * n) * GreenSlime.environment, 4)
        return {'height':new_height, 'weight':new_weight}

    def __lt__(self, greenslime):
        return self._mass < greenslime._mass
    
    def __le__(self, greenslime):
        return self._mass <= greenslime._mass

    def __gt__(self, greenslime):
        return self._mass > greenslime._mass

    def __ge__(self, greenslime):
        return self._mass >= greenslime._mass
        
GreenSlime.modify_environment_constant(0.57)
slime1 = GreenSlime(100, 30)
slime2 = GreenSlime(50, 70)
print(slime1 + slime2)
print(slime1 * 2)
print(slime1 >= slime2)
