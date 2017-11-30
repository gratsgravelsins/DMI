Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
[GCC 6.3.0 20170118] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> type(vars())
<type 'dict'>
>>> __builtins__.in
SyntaxError: invalid syntax
>>> __bui

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    __bui
NameError: name '__bui' is not defined
>>> __builtins__.input
<built-in function input>
>>> __builtins__.input
<built-in function input>
>>> __builtins__.input.__doc

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    __builtins__.input.__doc
AttributeError: 'builtin_function_or_method' object has no attribute '__doc'
>>> __builtins__.input.__doc__
'input([prompt]) -> value\n\nEquivalent to eval(raw_input(prompt)).'
>>> __builtins__.input.__do

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    __builtins__.input.__do
AttributeError: 'builtin_function_or_method' object has no attribute '__do'
>>> __builtins__.input.__doc__
'input([prompt]) -> value\n\nEquivalent to eval(raw_input(prompt)).'
>>> print __builtins__.input.__doc__
input([prompt]) -> value

Equivalent to eval(raw_input(prompt)).
>>> sin(0.56)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sin(0.56)
NameError: name 'sin' is not defined
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> from math import sin
>>> sin(0.56)
0.5311861979208834
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>}
>>> print sin.__doc__
sin(x)

Return the sine of x (measured in radians).
>>> sin(x)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sin(x)
NameError: name 'x' is not defined
>>> from cmath import sin
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>}
>>> print sin.__doc

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print sin.__doc
AttributeError: 'builtin_function_or_method' object has no attribute '__doc'
>>> sin>__doc__
True
>>> sin.__doc__
'sin(x)\n\nReturn the sine of x.'
>>> from math import sin as sinuss
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, 'sinuss': <built-in function sin>, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>}
>>> print sinuss.__doc__
sin(x)

Return the sine of x (measured in radians).
>>> import math
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, 'sinuss': <built-in function sin>, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>}
>>> math.cos(0.56)
0.8472551110134161
>>> import as matemaatika
SyntaxError: invalid syntax
>>> import math as matemaatika
>>> matemaatika.cos(0.56)
0.8472551110134161
>>> from math import *
>>> vars()
{'exp': <built-in function exp>, 'pow': <built-in function pow>, 'fsum': <built-in function fsum>, 'cosh': <built-in function cosh>, 'ldexp': <built-in function ldexp>, 'hypot': <built-in function hypot>, 'acosh': <built-in function acosh>, 'tan': <built-in function tan>, 'matemaatika': <module 'math' (built-in)>, 'asin': <built-in function asin>, 'isnan': <built-in function isnan>, 'log': <built-in function log>, 'fabs': <built-in function fabs>, 'floor': <built-in function floor>, 'atanh': <built-in function atanh>, 'sqrt': <built-in function sqrt>, '__package__': None, 'frexp': <built-in function frexp>, 'factorial': <built-in function factorial>, 'degrees': <built-in function degrees>, 'pi': 3.141592653589793, 'log10': <built-in function log10>, '__doc__': None, 'math': <module 'math' (built-in)>, 'asinh': <built-in function asinh>, 'fmod': <built-in function fmod>, 'atan': <built-in function atan>, '__builtins__': <module '__builtin__' (built-in)>, 'copysign': <built-in function copysign>, 'cos': <built-in function cos>, 'ceil': <built-in function ceil>, 'atan2': <built-in function atan2>, 'isinf': <built-in function isinf>, 'sinh': <built-in function sinh>, '__name__': '__main__', 'trunc': <built-in function trunc>, 'expm1': <built-in function expm1>, 'e': 2.718281828459045, 'tanh': <built-in function tanh>, 'radians': <built-in function radians>, 'sinuss': <built-in function sin>, 'lgamma': <built-in function lgamma>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'modf': <built-in function modf>, 'sin': <built-in function sin>, 'acos': <built-in function acos>, 'log1p': <built-in function log1p>, 'gamma': <built-in function gamma>}
>>> acos(0.56
     )
0.9764105267938343
>>> 
