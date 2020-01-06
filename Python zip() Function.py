'''

Python’s zip() function creates an iterator that will aggregate elements from two or more iterables. You can use the resulting iterator to quickly and consistently solve common programming problems, like creating dictionaries. In this tutorial, you’ll discover the logic behind the Python zip() function and how you can use it to solve real-world problems.
zip() is available in the built-in namespace. If you use dir() to inspect __builtins__, then you’ll see zip() at the end of the list:

>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', ..., 'zip']

You can see that 'zip' is the last entry in the list of available objects.

According to the official documentation, Python’s zip() function behaves as follows:

    Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. (Source)

You’ll unpack this definition throughout the rest of the tutorial. As you work through the code examples, you’ll see that Python zip operations work just like the physical zipper on a bag or pair of jeans. Interlocking pairs of teeth on both sides of the zipper are pulled together to close an opening. In fact, this visual analogy is perfect for understanding zip(), since the function was named after physical zippers!
Python’s zip() function is defined as zip(*iterables). The function takes in iterables as arguments and returns an iterator. This iterator generates a series of tuples containing elements from each iterable. zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.

'''

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
zipped  # Holds an iterator object

type(zipped)

list(zipped)