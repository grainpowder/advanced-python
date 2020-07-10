"""
Convenient and secure way to store constants using key-value structure is to use 'namedtuple'.
(Different from dictionary in that namedtuple is immutable)
This creates class that store constants by key.


1. Definition
object_name = namedtuple(class_name, fieldstring).


2. 3 ways to create instance 
    
    1) Plain insertion of values
        instance_name = object_name(value1, value2, ...)
    
    2) Unpack dictionary
        value = {field1:value1, field2:value2, ...}
        instance_name = object_name(**value)
    
    3) Use _make method with list
        value = [value1, value2, ...]
        instance_name = object_name._make(value)
"""


from collections import namedtuple

Item = namedtuple('Itemmaker', 'item, age, price')
print(Item._fields) # ('item', 'age', 'price')


pen1 = Item('uniball black', 0, 2500)
print(pen1.item)

label = {'item':'uniball red', 'price':2500, 'age':0}
pen2 = Item(**label)
print(pen2.age)

label = ['monami green', 8, 1500]
pen3 = Item._make(label)
print(pen3.price)


# namedtuple -> dictionary
print(pen1._asdict()) # {'item': 'uniball black', 'age': 0, 'price': 2500}
