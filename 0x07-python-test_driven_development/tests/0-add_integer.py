"""
>>> from 0-add_integer import add_integer
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
TypeError: b must be an integer
>>> add_integer(None)
Traceback (most recent call last):
TypeError: a must be an integer
>>> add_integer()
Traceback (most recent call last):
TypeError: missing 1 required argument a
>>> add_integer(1000e1000)
Traceback (most recent call last):
OverflowError: cannot convert float infinity to integer
>>> add_integer("Hello", "World")
Traceback (most recent call last):
TypeError: a must be an integer
>>> add_integer(float('nan'))
Traceback (most recent call last):
ValueError: cannot convert float NaN to integer
"""
