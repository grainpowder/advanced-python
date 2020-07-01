"""
< First class function >
 - It is a term to specify the nature of certain programming language, not individual function.
    ex. Python has first class function, but C or Java does not.
 1. A language is said to have first class function if it treats a function as first class citizen.
 2. An object is said to be treated as first class citizen if
    1) It can be assigned to a variable.
    2) It can be used as input of a function.
    3) It can be returned as output of a function.
 3. So it's basically general characteristic of typical variables like int, float, etc.,.
    -> Thus, to have first class function basically means that function is treated as typical variable.
 - This is important trait of certain language which enables functional programming.
 * Note : A function that takes one or more function as input and returns function is called Higher Order Function(HOF)
"""

# Proof that Python has first class function
# 1) Function can be assigned to a variable.

def eratosthenes(n):
    """
    Find prime numbers up to n(inclusive)
    """
    indices = [False, False] + [True] * (n-1)
    for step in range(2, n // 2 + 1):
        for idx in range(step*2, n+1, step):
            indices[idx] = False
    return indices

findprime = eratosthenes
print(sum(findprime(11)))


# 2) Function can be used as input of a function
# Common built-in function that takes function as input : map, reduce, filter

from functools import reduce

print([sum(indices) for indices in map(findprime, range(1,11))])
print(reduce(lambda x, y: x*y, range(1, 6)))
print([n for n in filter(lambda x: x % 2, range(20))])


# 3) Function can be returned as output of a function
# To be covered in closure.py