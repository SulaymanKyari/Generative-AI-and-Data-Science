# func(1) accepts a variable length of
# arguments and print their value.

def func1(*args):

    for arg in args:

        print(arg)

func1('Hello', 'my', 'name', 'is', 'Sulayman')
