"""
< Closure : A function that remembers namespace of enclosing scope >
    That is, for a function to be a closure, it must satisfy following:
        1. It is nested function of another function
        2. It uses variable defined in namespace of enclosing scope(i.e. free variable in nonlocal scope)
        3. It is returned as an output of enclosing function
"""

import random


def WLLN(round_at):
    numbers = []
    def average_in_action(value):
        numbers.append(value)
        return round(sum(numbers) / len(numbers), round_at)
    return average_in_action


"""
In the code below, 'average_in_action' is executed 320 times.
At each iteration, random number from Unif(0,1) is generated and stored in 'numbers' defined in nonlocal scope.
Since it returns sample mean of them, user can observe that it indeed converges in probability to 0.5

Note that there are two free variables in the nonlocal scope: numbers, round_at.
Names and their values can be observed by using specific methods written below.
"""

random.seed(1234)
averager = WLLN(round_at=4)
for iter in range(320):
    result = averager(random.random())
    if (iter+1) % 40 == 0:
        print(f"| iteration : {str(iter+1).rjust(3)} | sample mean : {str(result).ljust(6,'0')} |")

print(averager.__code__.co_freevars)
print(len(averager.__closure__[0].cell_contents))
print(averager.__closure__[1].cell_contents)
