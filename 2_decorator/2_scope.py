"""
< Scope : Specific region that certain name is visible >
    1. There are certain types of scope such as:
    # global scope
    ...
    def outer():
        # nonlocal scope
        ...
        def inner():
            # local scope
            ...

    2. Rule of thumb when
        reading : variable is searched from the current scope to shallower scope.
        writing : writing on the variable at current scope is allowed only.

        So, if user tries to write on variable defined in namespace of other scope, user must declare that fact with certain keyword.
        ex) global x    : command to enable writing on x in global scope
            nonlocal x  : command to enable writing on x in nonlocal scope
"""

x = 10
def x_times2_plus1_is_y():
    global x
    x *= 2
    y = x + 1
    def minus_y_plus2_is_z():
        nonlocal y
        y *= -1
        z = y + 2
        print(f'x : {x}') # 20  : Read from global scope, Modified at nonlocal scope
        print(f'y : {y}') # -21 : Read from nonlocal scope, Modified at local scope
        print(f'z : {z}') # -19 : Read from local scope. 
    minus_y_plus2_is_z()
x_times2_plus1_is_y()
