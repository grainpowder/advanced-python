"""
< Generator : simple and powerful tool for creating iterator >

    1. Iteration, Iterable, Iterator
      a. Iteration
        To take item of something consecutively(i.e. one after another)
      b. Iterable
        An object that has __iter__ method, which returns an iterator and executed when iter() is called on this object.
        (in fact, this is what 'for' loop initially does when making iteration over elements of iterable)
      c. Iterator
        An object that has __next__ method, which defines way to access elements in a container and executed when next() is called on this object.
        (in fact, this is what 'for' loop does on returned iterable in every iteration)

    2. To define iterator is to define __next__ method(i.e. how data is being accessed at each iteration). Generator is useful tool for this job.
      a. In generator, __next__ is executed when 'yield' keyword is met, and it emits object that comes next to 'yield' command.
      b. Moreover, 'yield' in generator does not terminate the process of a function like 'return' does.
        It remembers the location where the latest emission has been made.

Example code below shows how __iter__, __next__ works. 'while' statement is what exactly 'for' statement above it does.
Then, a function 'read5' that creates generator that emits data in particular way when called with iterable container is defined.
The convenience of generator is evident when compared with while loop implementation, which manually explicitly calls '__next__' and hanldles 'StopIteration'.
"""

hello = 'world'

for letter in hello:
    print(letter)

iterator = iter(hello)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


def read5(input_list):
    container = []
    for element in input_list:
        container.append(element)
        if len(container) == 5:
            yield container
            container = []

    if container:
        yield container

read5_generator = read5([i for i in range(13)]) # Creates generator.
for v in read5_generator:                       # Internally, iterator where '__next__' is defined to emit object next to 'yield' is defined.
    print(v)                                    # So result becomes [0,1,2,3,4], [5,6,7,8,9], [10,11,12].
