# First week resources (Basic python introduction)

## Examples
Different examples similar to those seen during the course can be found in the [examples folder](https://github.com/dschurholz/mpi-python-course/first_week/examples/). They are meant to help you read python code with the new concepts learned through the course. You can go through them and understand what each line does and what the expected output will be. Later on execute it and compare the output.

## Exercises
Exercises for testing those concepts learnt during the course can be found in the [exercises folder](https://github.com/dschurholz/mpi-python-course/first_week/exercises/).

## Cheatsheet

### Data types

Python offers the following basic data types:

1. Boolean:
    * `True`: also represented by 1
    * `False`: also represented by 0

2. Numeric:
    * Integer (natural numbers): `8`
    * Float or Floating point number (real numbers): `15.293`
    * Complex number (imaginary numbers): `4+3j`
    * e = 10 shortcut for large or tiny numbers: `10e2` or `10E2` (this equals 1000)

3. Strings:
    * Single quoted: `'Hello "World"!'`
    * Double quoted: `"Hello 'World'!"`
    * Triple quoted: `""" "Hello" 'World'! """`

4. Collections:
    * List: `[1 , 2, 2, [5, "Hello"], "world"]`, ordered, mutable.
    * Tuple: `("apple", "apple", "banana", ["World", 5], 1)`, ordered, inmutable.
    * Range: `range(a,b,s)`, returns an iterator over all values between `[a, b[` with step `s`. 
    * Set: `{1, 5, 6, "doggo"}`, distinct values only, inmutable, unordered 
    * Dictionary: {"doggo": "man's best friend", 5: [2, 3], "cat": "indifferent"}, key: value pairs, unordered, mutable.

5. Null:
    * `None` is a reserved word used to represent a NULL value.

### Assignment

Variables allow us to save a value under a name of our choosing.

Note: The name can't be a *built-in* value of the python language (example: True, int, return, etc.) and can't start with a number.

```python
"""
Variable assignment:
    <name of variable> = <value>
"""
bool_true = True
bool_false = False
integer_a = 8
integer_b = 5
float_a = 13.982
float_b = 26.5
string_one = "This is a first string"
string_two = 'This is a second string'
string_third = """This is a third string"""
list_example = [1, 2, ["dog", 5], True]
tuple_example = (1, 2, ["dog", 5], True)
range_example = list(range(1, 10, 2))  # This is [2, 4, 6, 8]
set_example = {16, 2, 4, "dog", 9}
dictionary_example = {"doggo": "man's best friend", 5: [2, 3], "cat": "indifferent"}

"""
Indexing assignment
    <name of indexable collection>[index position] = <new value>
"""
list_example[1] = "new value"
list_example[-1] = "new last value"  # negative indexes start from the end of the list
dictionary_example["cat"] = "wants food, not so indifferent now"
dictionary_example["new key"] = "new value"

"""
Indexing assignment of a collection inside a collection
    <name of indexable collection>[index in first collection][index in second collection] = <new value>
"""
list_example[2][2] = "new value"
dictionary_example[5][1] = "new value"

"""
Assignment with index slicing for lists
    <name of indexable collection>[index start:index end:index step] = <new value>
"""
list_example[0:2] = ["new value", "new second value"]

```

### Operators
Operators allow us to combine or make values and variables interact.

```python
# Operators on numeric data types
a = 8
b = 5
a + b   # Addition
a - b   # Subtraction
a * b   # Multiplication
a / b   # Division (answer is always a float number (decimal))
a // b  # Floored division (answer is always an integer)
a**2    # Exponentiation
a % b   # Remainder of a division (better known as 'modulo' in programming)
a += b  # Shortcut for a = a + b
a -= b  # shortcut for a = a - b
a *= b  # shortcut for a = a * b
a /= b  # shortcut for a = a / b
a //= b  # shortcut for a = a // b

# Operators on strings
"hat" * 3     # gives us "hathathat"
"big" + " " + "hat" # gives us "big hat"

# Operators on lists
["dog", "cat"] * 2  # gives us ["dog", "cat", "dog", "cat"]
[1, 2] + [3, 4]     # gives us [1, 2, 3, 4]

# Logical operators
a = True
b = False
not a    # logical negation: gives us False
a and b  # logical and: gives us False
a or b   # logical or: gives us True

# Comparison operators
a = 8
b = 5
a == b  # equal to: gives us False
a != b  # does not equal to: gives us True 
a > b   # greater than: gives us True
a >= b  # greater equal than: gives us True
a < b   # less than: gives us False
a <= b  # less equal than: gives us False
a is b  # check if the identities of a and b are the same: gives us True (but for integers higher than 100 it would give False)

# Membership operator
4 in [1, 2, 3, 4]      # check if value in the collection: gives us True
4 not in [1, 2, 3, 4]  # check if value is not in the collection: gives us False
```

### Conditionals
Conditionals are used to check logical statements and execute a different set of steps according the value of the statement.

```python
"""
Syntax:
    if <condition1>:
        do only this
    elif <condition2>:
        do only this, only if <condition2> was False
        you can have any number of elif statements 
    else:
        do this if all other conditions failed
"""
a = 8
b = 5

if a > b:  # This condition will succeed and only the a + b line will be executed
    a + b
elif a < b:
    a - b
else:
    a * b
```

### Loops
Loops allow us to repeat an operation many times, until a condition is satisfied. We went over two types of loops:

1. *For* loop: iterate over a collection of values until reaching their end.
```python
"""
Syntax:
    for <item(s)_variable_name> in <collection>:
        do something
"""
l = [1, 6, 9, "dog"]
for item in l:
    print(item)

d = {"dog": 4, "cat": "brown"}
for key in d:
    print(key)  # this will print "dog" and "cat"

for key, value in d.items():
    print(key, value)  # this will print "dog 4" and "cat brown"

r = range(1, 10, 2)
for i in r:
    print(i)  # Will print 2, 4, 6, 8
```

2. *While* loop: iterate until a given condition returns False.
```python
"""
Syntax:
    while <condition>:
        do this
"""
x = 10
while x > 0:   # This will exit when x == 0
    print(x)   # We will print 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    x = x - 1
```

Special loop commands:
`break`: exit the loop completely
`continue`: go to the next iteration skipping code block inside the loop after this line

```python
"""
Syntax:
    while <condition>:
        do this
        if <condition2>:
            break
        if <condition3>:
            continue
        do something only if condition2 and condition3 are False
"""
x = 10
while True:   # This loop will never exit on its own
    x = x - 1
    if x == 0:
        break  # This will exit the loop
    if x % 2 == 0:
        continue  # This will go to the next iteration
    print(x)   # We will print 9, 7, 5, 3, 1
```

### Special built-in functions
Some reserved words are functions that come in handy to inspect our code. A complete list of these reserved functions can be found at [this link](https://docs.python.org/3/library/functions.html).

```python
"""
Inspection commands
"""
a = 8
type(a)    # will return int, meaning it is an integer
dir(a)     # will return all attributes and methods of the variable a
help(a)    # will open a manual to the variable a
globals()  # will return all globally available variables
locals()   # will return all locally available variables
dir?       # the ? will prompt a small documentation of the variable
hasattr(a, 'attr_name')  # check if a has attribute 'attr_name'
getattr(a, 'attr_name')  # get the attribute 'attr_name' value of a
setattr(a, 'attr_name', value)  # set the attribute 'attr_name' to value in a

"""
Transformation commands
"""
int(a)   # will try to transform the variable into an integer
float(a) # will try to transform the variable into a float
str(a)   # will try to transform the variable into a string
list(a)  # will try to transform the variable into a list
tuple(a) # will try to transform the variable into a tuple
set(a)   # will try to transform the variable into a set

"""
Creation commands
"""
dict()  # will create a new empty dictionary
list()  # will create a new empty list
set()  # will create a new empty set
tuple()   # will create a new empty tuple

"""
Checking a variable type
"""
a = 8
type(a) is int  # check if 'a' is an integer, you can use str, tuple, list, etc.

"""
File handling
"""
filename = "file.txt"
f = open(filename)  # Open file in read-only mode
f.read()  # Read the whole file at once.
f.close()  # Close the file

filename = "file.txt"
f = open(filename)  # Open file in read-only mode
for line in f.readline():  # Read file, line by line
    print(line)
f.close()
```

### Functions
Functions allow us to encapsulate blocks of code to be reused multiple times.

```python
"""
Defining a function.

Syntax:
    def <name of function>(<parameter1>, <paremeter2>=<default value>, ... ):
        do something here

The <default value> is used if the function is called without the parameter.
"""
def add(a, b=0):
    return a + b

"""
Calling a function.

Syntax:
    <name of the function>(<parameter1>, <paremeter2>, ... )
"""
add(8, 6)     # will return 14
add(8, b=10)  # will return 18, we specifically set 10 to b
add(8)        # we can leave the second parameter, since b has a default value as 0, the output will be 8

"""
Defining a function with *args and **kwargs.

Syntax:
    def <name of function>(*args, **kwargs):
        do something here

`*args` is a tuple that contains parameters that have no key, example, a
`**kwargs` is a dictionary that contains parameters that have a keyname, example, b=8 
"""
def add(*args, **kwargs):
    a = args[0]
    b = kwargs['b']
    return a + b
```

### Modules
Modules are a big benefit of using python. They encapsulate variables defined in a file (or module) and export them to be used in other files.

`file1.py` implements the following function:
```python
def multiply(a, b)
    return a * b
```

`file2.py` uses the function from `file1.py`
```python
"""
Import the module

Syntax:
    import <module name>
"""
import file1

file1.multiply(8, 8)

"""
Import the module and rename it

Syntax:
    import <module name> as <new name>
"""
import file1 as f1

f1.multiply(8, 8)

"""
Import the function we want directly

Syntax:
    from <module name> import <variable name>
"""
from file1 import multiply

multiply(8, 8)

"""
Import the function we want directly and rename it

Syntax:
    from <module name> import <variable name> as <new variable name>
"""
from file1 import multiply as f1_mult

f1_mult(8, 8)
```

### Raising errors
Python suggests to always show an error when something is wrong. There are built-in errors that can be raised with the `raise` word. A list of exceptions (errors) available in python can be found [here](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).

```python
"""
If we have a program that should divide a number a by b, we should not allow division by zero

Syntax:
    raise <error class>(<error message>)
"""
a = 8
b = 0

if b == 0:
    raise ValueError("Division by zero is not possible.")  # the program will exit here and return the error

a / b
```
