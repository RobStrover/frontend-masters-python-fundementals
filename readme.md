
# Front End Masters Python Course

## REPL
REPL - Read, Evaluate Print Loop
How we interact with the Pyton interpreter.

Just type `python` in your terminal to access the repl. Commands such as `1 + 7` will show the correct output.

Works a lot like the console in JS

`Ctrl` + `l` clears the REPL

`>>>` is the indicator of a result in the console

define variables like this:
`name = "Rob"`

and then see the value:
`name` -> 'Rob'

see the type of a variable:
`type(name)` -> '<class 'str'>'

There is built in help for type classes:
`help(str)`

and get help for particular methods
`help(str.upper)`

see the method directory (similar to prototype) for the type of a variable:
`dir(name)` -> 
`['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']`

## Variables

None is nothing/null in python:
`x = none` -> will give empty space. It has a type of 'NoneType'

Variables cannot start with a number:
`1test = 'blahh'` -> `>>> 1test = 'blahh'
  File "<stdin>", line 1
    1test = 'blahh'
        ^
SyntaxError: invalid syntax`

Be careful when creating new variables as it's possible to overwrite built in types:
`list = 1` -> no more `list()`!

### Strings
Can be enclosed in either single or double quotes. It's best to always stick to double quotes and use single quotes where needed. Escaping characters is always and option with `\`.

#### FStrings
Work like string templates:
`name = "Rob"`
f"Hello, {name}"'severus', 'draco', 'goyle'}ith `\n`

### Numbers
When dividing two integers, a float will be returned

convert a string to a number with 'int'
`int('42')` -> 42

### Booleans
Must be with capitals: `True` or `False`

## Pep8
Python coding conventions:
https://pep8.org/

## Printing to Terminal
Use `print()` to print to terminal:
`print(foo)`

print all the things!
`print(item1, item2, item3)`

## Functions
- always start with the keyword `def` followed by a space.
- then the function name
- then comma separated arguments in parenthesis
- a colon
e.g.

`def foo():`

Use the `return` statement to... return:

Make sure that all lines of a function are indented. There are no brackets around function definitions.

```
def make_greeting(name):
    return f"Hello there, {name}!"
 
make_greeting('Rob')
```
'Hello there, Rob!'

### Arguments
Default values for arguments must come last in a function definition:
`def make_greeting(age, name="Rob"):`

If these are not declared last then you will get a syntax error

Positional arguments can be called with just a value or also with their labels. This can help if there's confusion when working with a function that has both positional and non-positional arugments:
`def foo(a, b=5)`

`foo(3)`
or
`foo(a=3)`

### Using lift types as default arguments.
*DON'T DO THIS*
Default arguments are not created every time a function is called. They are created once. So don't use lists as default arguments:

```python
def foo(a, b=[]):
    b.append(a);
    print(b)
```

`foo(5)` -> [5]

`foo(6)` -> [5, 6]

The same list is used over and over.

To get around this, Set the default value of `b` to `None` and then check in code if the value of `b` is still `None` and change it to a list if required:
```python
def foo(a, b=None):
    if b is None:
        b = []
    b.append(a)
    print(b)
```

### Function Scope
Similarly to how function scoping works in JS, Python functions have access to variables in their parent scope but cannot change these variables. Variables of the same name are redefined in the new scope.

## Equality
`==` is equality
`is` checks if is identical reference in memory

## Lists
lists (arrays in JS) are created with two square brackets:
`[]`
or by using the built in method:
`list()`

Can be defined with data
`data = ['Tim', 42, True]`

Find out a list's length with the `len()` built in:
```python
data = ['Tim', 42, True]
len(data)
```

Accessing items in a list can be done with the index like any other language. *Starts at index 0*.

Values can be reassigned by also using the index in a list:
```python
data = ['Tim', 42, True]
data[1] = 43
data[2] = False

data # Time, 43, False
```

### Sorting Lists
You can use the built in `sorted()` function to sort numbers:
```python
lottery_numbers = [1, 4, 34242, 78, 11]
sorted(lottery_numbers) # [1, 4, 11, 78, 34242]
```
Note: Sorted returns a copy of the array, the sorting is *not* done in place.

`sorted` can take an optional argument to reverse the sort:
```python
lottery_numbers = [1, 4, 34242, 78, 11]
sorted(lottery_numbers, reverse=True)
lottery_numbers # [34242, 78, 11, 4, 1]
```
#### Sorting in place
You can also sort lists in place using the `.sort()` built in list function:
```python
lottery_numbers = [1, 4, 34242, 78, 11]
lottery_numbers.sort()
lottery_numbers # [1, 4, 11, 78, 34242]
```
To reverse here, use the other built in list function `reverse`:
```python
lottery_numbers = [1, 4, 34242, 78, 11]
lottery_numbers.sort()
lottery_numbers.reverse()
lottery_numbers # [34242, 78, 11, 4, 1]
```

### Slicing Lists
A list can be sliced to access more than one item in a list at a time:
```python
test = ['p', 'y', 't', 'h', 'o', 'n']

test[0:3] # ['p', 'y', 't']
test[:3] # ['p', 'y', 't']
test[-1] # 'n'
```

### Other List Methods
#### append()
`list.append(NEW_ITEM)` - insert one new item into array. Multiple items not supported

#### insert
`list.insert(NEW_ITEM, INDEX)` - inserts one new item into array at index

#### extend
```pyhton
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

list1 # [1, 2, 3, 4, 5, 6]
```

### Finding items in a list
#### in
```python
numbers = [1, 2, 3, 4, 5, 1]

42 in numbers # False
3 in numbers # True
```

#### index
```python
numbers = [1, 2, 3, 4, 5, 1]

numbers.index(3) # 2
numbers.index(1) # 0 | the first found index only
numbers.index(42) # ValueError: 42 is not in list
```

#### count
```python
numbers = [1, 2, 3, 4, 5, 1]

numbers.count(3) # 1
numbers.count(1) # 2
numbers.count(42) # 0
```
### Removing items from a list
#### remove
```python
numbers = [1, 2, 3, 4, 5, 1]

numbers.remove(3)
numbers # [1, 2, 4, 5, 1]

numbers.remove(1)
nuumbers # [2, 3, 4, 5, 1] | only first occurrence removed
```

#### pop
`.pop()` on its own will return the last item on a list and remove it from the list in place

`.pop(2)` removes and returns the given index of the array in place

```pyhton
numbers = [1, 2, 3, 4, 5, 1]

test = numbers.pop();
test # 1
numbers # [1, 2, 3, 4, 5]

test2 = numbers.pop(2)
test2 # 3
numbers [1, 2, 4, 5]
```

## Tuples
tuples are light-weight collections used to keep track of related but different items. They are immutable.

```python
a = ()
type(a) # <class 'tuple'>
```

Creating a single item tuple must always be done with a comma after the 1 otherwise the variable type will be of that first entered value

```python
a = (1)
type(a) # <class 'int'>

a = (1,)
type(a) # <class 'tuple'>
```

Tuple indexes can be accessed with square bracket notation:

```python
person = ('rob', 28, 'programming')

person[2] # 'programming'
person[1] # 28
```

As they are immutable they cannot be changed in any way at all. They have no mutating methods such as pop or extend.

Tuples can be "unpacked" in the following way:
```python
person = ('rob', 28, 'programming')
name, age, interest = person

name # 'rob'
age # 28
interest # 'programming'
```
if state
person = ('rob', 28, 'programming')
name, age, _ = person

name # 'rob'
age # 28
# Our _ underscore means we didn't want the interest
```

Keep in mind that is is the comma(s) that mean the data is a tuple:
```python
def http_status_code():
    return 200, "OK" # This is a tuple!

http_status_code() # (200, 'OK')
http_status_code()[1] # 'OK'
code, status = http_status_code() # code and status defined because of unpacking
```

### Tuple Search Methods
`.index(item)`can be used to find a member of a tuple:
```python
student = ("rob", 28, "programming")
student.index(28) # 1
```
 or `item in my_tuple` can be used to get a boolean confirmation

 ## Sets
 Sets are used to store other immutable types in an unsorted way. An item can only be in a set once. NO DUPLICATES ALLOWED. Sets are fast for membership testing and have set operations.

 Define an empty one:
 ```python
 set()
 ```
 Otherwise it's a dictionary.
 Sets can also be defined with items:
 ```python
 a = {1,2,3,4}
 a # 1, 2, 3, 4
 ```

 Duplicate items are simply not included:
 ```python
names = {'rob', 'emma', 'rob'}
names # 'rob', 'emma'
 ```

Check the length of a set with `len()`
```python
names = {'rob', 'emma'}
len(names) # 2
```

Under the hood, Python uses a hash system to speed up searching in 'hashable' variables. It's not something you'd probably use often but it's fun to play with:
```python
hash("rob") # -8129098991804621400
```

non hashable variables return a type error:
```python
hash([]) # list - TypeError: unhashable type: 'list'
```

This explains why you cannot put a list inside of a set:
```python
testing = {'rob', 28, []} # TypeError: unhashable type: 'list'
```

However you can initialise a set with a list which will handily dedupe the list:
```python
names = ['gimli', 'max', 'snowball', 'max', 'snowball', 'max', 'snowball']
set(names) # {'gimli', 'max', 'snowball'}
```

The same works the other way round if you ever need to order a set:
```python
names = {'gimli', 'max', 'snowball'}
list(names) # ['max', 'gimli', 'snowball']
```

### Add to sets
Use the `add` method
```python
colors = {'red', 'green', 'blue'}
colors.add('pink')

colors # {'red', 'green', 'blue', 'pink'}
```

### Remove from sets
use the `discard` method
```python
colors = {'red', 'green', 'blue'}
colors.discard('blue')
colors # {'red', 'green'}
```
You can also use `remove` but trying to `remove` an item that does not exist in a set causes an error, `discard` does not.

### Concat sets
Use the `update` method:
```python
friends = {'fred', 'george', 'ron', 'harry'}
foes = {'severus', 'draco', 1234}

friends.update(foes)
friends # {'severus', 'fred', 'george', 'harry', 1234, 'ron', 'draco'}
```

Be careful with how you use `update`. Using with single (technically sequence) types will result in undesirable behaviour:
```python
friends = {'fred', 'george', 'ron', 'harry'}
friends.update('rob')
friends # {'fred', 'harry', 'ron', 'o', 'b', 'george', 'r'}
```
Each individual letter from the (technically) sequence is added to the set.

### Set Operations
#### union
`a.union(b)` or `a | b` creates a new set with all the items from both `a` and `b`
```python
friends = {'fred', 'george', 'ron', 'harry'}
foes = {'severus', 'draco', 'goyle', 'harry'}

friends.union(foes) # {'severus', 'fred', 'goyle', 'harry', 'ron', 'george', 'draco'}
friends | foes # {'severus', 'fred', 'goyle', 'harry', 'ron', 'george', 'draco'}
```

#### intersection
`a.intersection(b)` or `a & b` creates a new set containing only items that are both in set `a` and `b`
```python
friends = {'fred', 'george', 'ron', 'harry'}
foes = {'severus', 'draco', 'goyle', 'harry'}

friends.intersection(foes) # {'harry'}
friends & foes # {'harry'}
```

#### difference
`a.difference(b)` or `a ^ b` creates a new set with items that are in `a` but not in `b`.
```python
friends = {'fred', 'george', 'ron', 'harry'}
foes = {'severus', 'draco', 'goyle', 'harry'}

friends.difference(foes) # {'fred', 'george', 'ron'}
friends ^ foes # {'severus', 'fred', 'goyle', 'ron', 'george', 'draco'}

foes.difference(friends) # {'severus', 'draco', 'goyle'}
foes ^ friends # {'severus', 'fred', 'goyle', 'ron', 'george', 'draco'}
```

## Dictionaries
Is a hash under the hood. Dictionaries can eb used to store data in key/value pairs and item keys can only be of immutable types.

Define a dictionary:
```python
{}

type({}) # <class 'dict'>
```

The key value pair syntax is as follows:
```python
numbers = {"one": 1, "two": 2, "three": 3}
```

You can have mutable types as the value but not the key in a dictionary:
```python
{1: []} # ok!

{[]: 1} # TypeError: unhashable type: 'list'
```

Square bracket notation is used to access values at a key. Attempting to access a key that does not exist results in a KeyError:
```python
numbers = {"one": 1, "two": 2, "three": 3}

numbers["one"] # 1
numbers ["four"] # KeyError: 'four'

# Key error can be avoided by using .get():
numbers.get("four") # no error

# A default value can be passed for in the event the key does not exist:
numbers.get("four", 4) # 4
```

### Add to dictionary
Just add the new key in square brackets:
```python
numbers = {"one": 1, "two": 2, "three": 3}
numbers["four": 4]

numbers # {"one": 1, "two": 2, "three": 3, "four": 4}
```

### Overiting values
Simply use square notation again
```python
numbers = {"one": 1, "two": 2, "three": 3}
numbers["two": "two testing"]

numbers["two"] # two testing
```

### Checking existnence of keys
Use the `in` keyword
```python
numbers = {"one": 1, "two": 2, "three": 3}

"one" in numbers # True
```

### Combining Dictionaries
Use the `.update()` function
```python
numbersSmall = {"one": 1, "two": 2, "three": 3}
numbersBig = {"four": 4, "five": 5, "six": 6}

numbersSmall.update(numbersBig)
numbersSmall # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
```
Matched keys will be overwritten to the value in the array as the update argument

### Get Keys or Values from a Dictionary
Use `.keys()` or `.values()`:
```python
numbers = {"one": 1, "two": 2, "three": 3}

numbers.keys() # dict_keys(['one', 'two', 'three'])
numbers.values() # dict_values([1, 2, 3])
```

A list of tuples can be returned using `.items()`:
```python
numbers = {"one": 1, "two": 2, "three": 3}

numbers.items() # dict_items([('one', 1), ('two', 2), ('three', 3)])
```

## Truthy-ness
See if a variable is truthy using `bool()`:
```python
bool('blahh') # true
bool(0) # false
```

## Truth Table / Operators
Use `and`, `or`, and `not`:

```python
var1 = True
var2 = True
var3 = False
var4 = False

var1 and var2 # True
var1 and var3 # False

var1 or var2 # True
var3 or var4 # False

not var1 # False
not var4 # True

var1 or (not var4 and not var2) # True
```

Using an `and` with two values will return the first false-y value:
```pyhton
var1 = [] # false-y
var2 = 'testing text' # truthy

var1 and var2 # []
```

## Comparisons
```python
10 > 5 # True
5 < 10 # True

5 == 5 # True
5 != 5 # False
```

## Loops and Control Statements
### For Loop
```python
colours = ["Red", "Blue", "Green", "Pink", "Black"]

string = ""
for colour in colours:
    isFirst = colours[0] == colour
    isLast = colours[len(colours) -1] == colour

    if isFirst:
        string = f"My favourite colour is {colour}."
        continue

    if isLast:
        string = f"{string} Actually, no it's really {colour}. :)"
        continue

    string = f"{string} No, wait! It's actually {colour}."

print(string) # My favourite colour is Red. No, wait! It's actually Blue. No, wait! It's actually Green. No, wait! It's actually Pink. Actually, no it's really Black. :)
```

## While Loops
```python
counter = 0
max = 1000

while counter < max:
    print(f"the count is at {counter}")
    counter = counter + 1
```

Use `break` and `continue` to control the flow of the while loop

`break` ends the loop
`continue` skips to the next item in the loop

