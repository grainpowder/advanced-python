"""
< Decorator : Enclosing function of a closure which takes a function as an input >

    1. Problem(a.k.a. when to use)
        There is an additional feature, denoted as A, that has to be added to each of implemented function, F1, F2, ..., F100

    2. Possible Solution
        a. Modify each of F1, F2, ..., F100 or create another 100 functions G1, G2, ..., G100
            - Unarguably inefficient.
        b. Make a function B that takes function and required argument as input and operates A
            - Only efficient when A is simple enough to be implemented in a single function.

    3. Solution
        Make a function B that operates A using functions defined in distinct namespace given input function Fi, i = 1, ..., 100
        - Defining functions in distinct namespace is beneficial in that it avoids ambiguity caused by function of same name defined in global scope.
        - This can be implemented by using closure function, since it can use nonlocal scope which is distinct from global scope.

    4. Template for defining decorator

        def B(func):
            def feature1:
                ...
            def feature2:
                ...
            ...
            def main(*args):
                result = func(*args)
                ... operate A using functions defined in this scope and result from input function 'func' ...
                return final_result_to_be_returned
            return main

    5. Usage of decorator
        Simply attach 'at' sign with the name of a decorator to execute function defined right after in the nonlocal namespace

        @B
        def hello(parameters):
            ...

        Attaching multiple decorators is also possible. 
        Function is first executed in the nonlocal scope of decorator right above, and then decorator above it, ... etc.
        Stacking order of decorator matters!

        ...
        @decorator3
        @decorator2
        @decorator1
        def function(parameters):
            ...

    6. Example
        a. Ridiculous sqrt function is defined in global scope, but this is not referred by main function inside get_l2norm thanks to scoping rule.
            -> Ambiguity of 'sqrt' is avoided!
        b. To understand how main function works in each decorator, note that meaning of asterisks in...
             - parameter : makes a function to pack input(s) into a single tuple.
             - argument  : unpacks the input.
"""

def sqrt(x):
    return 0


def get_l2norm(func):
    def sqrt(scalar, tol=1e-8):
        current = 100
        diff = 1e8
        while diff > tol:
            previous = current
            current = (scalar / current + current)/2
            diff = abs(current - previous)
        return current

    def main(*args):
        result = func(*args)
        return sqrt(sum([element ** 2 for element in result]))

    return main


def as_numeric(func):

    def main(*args):
        boollist = func(*args)
        converted = []
        for idx in range(len(boollist)):
            if boollist[idx]:
                converted.append(idx)
        return converted

    return main


def eratosthenes(n):
    quotient, remainder = divmod(n, 2)
    result = [False] + [True, False] * quotient + [True] * remainder
    result[1], result[2] = result[2], result[1]

    for unit in range(3, n//2, 2):
        for idx in range(2*unit, n+1, unit):
            result[idx] = False

    return result


@as_numeric
def primelist(n):               # This defines new function named 'primelist' where
    return eratosthenes(n)      #  1. 'primelist' is stored as value for free variable 'func' in 'as_numeric' decorator
                                #  2. and this free variable is remembered so refer 'func' to 'primelist' whenever new function 'primelist' is called.

@get_l2norm
@as_numeric
def l2norm_primes_upto(n):
    return eratosthenes(n)

print(eratosthenes(13))         # [False, False, True, True, False, ..., True]
print(primelist(13))            # 'converted' of main function in as_numeric : [2, 3, 5, 7, 11, 13]
print(l2norm_primes_upto(13))   # applies 'sqrt' function defined in nonlocal scope of 'l2norm_primes_upto' when returning final result.
