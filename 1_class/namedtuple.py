"""
Convenient and secure way to store constants using key-value structure is to use 'namedtuple'.
This creates class that store constants by key, and is defined by 'namedtuple(classname, fieldstring)'.
"""
from collections import namedtuple

# Define namedtuple named Item as object named Item
Item = namedtuple('Item', 'item, age, price')

# Check defined fields of Item class
print(Item._fields)

# Ways to define instance of Item class
# 1. Basic(Best when combined with list comprehension)
pen1 = Item('uniball black', 0, 2500)
# 2. Unpacking dictionary
label = {'item':'uniball red', 'age':0, 'price':2500}
pen2 = Item(**label)
# 3. From list using _make method
label = ['monami green', 8, 1500]
highlighter = Item._make(label)

# Call values by key
print(pen1.item)
print(pen2.age)
print(highlighter.price)

# namedtuple -> dictionary
print(pen1._asdict())
