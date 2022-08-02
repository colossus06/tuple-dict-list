# Tuples

* Sequence types and mutability
* **sequence**: is data which can be scanned by the for loop.
* **mutability**: readiness to be freely changed during program execution

* A tuple is an immutable sequence type.
* * It can behave like a list, you can't modify it program execution(in situ).

## create an empty tuple
`empty_tuple = ()`
## create a one element tuple


`one_element_tuple_1 = (1, )`

`one_element_tuple_2 = 1.,`

Removing the commas get two single variables, not tuples.

## Getting elements of a tuple:
 You can access tuple elements by indexing them. you can get the multiple elements of a tuple such as the following:

 ```

my_tuple = (1, 10, 100, 1000)
print(my_tuple[1:]) # prints (10, 100, 1000)
print(my_tuple[0]) # prints 1
```

**immutability**: AttributeError: 'tuple' object has no attribute 'append'

list(): convert a tuple to a list
```
tuple_ = 1,5,8
my_list= list(tuple_)

## Working with tuples

* the len() function accepts tuples, and returns the number of elements contained inside;
* the + operator can join tuples together (we've shown you this already)
* the * operator can multiply tuples, just like lists;
* the in and not in operators work in the same way as in lists.

you can delete a tuple as a whole:

```
my_tuple = 1, 2, 3, 
del my_tuple
print(my_tuple) 
```

# Dictionaries
`school_class = {}` : this is an empty dictionary
* a dictionary is a set of key-value pairs
* each key must be unique
* a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
* a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values;

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
```

* As of Python version 3.7, dictionaries are ordered.

## How to use a dictionary: the keys() and sorted()


you can adapt a dictionary to accept for loops. The method returns an iterable object consisting of all the keys gathered within the dictionary. Having a group of keys enables you to access the whole dictionary in an easy and handy way.

```
for key in dictionary.keys():
    print(key, "->", dictionary[key]
```

`for key in sorted(dictionary.keys()):`


## items()
```
for english, french in dictionary.items():
    print(english, "->", french)
```

There is also a method named values(), which works similarly to keys(), but returns values.

## values()

If you want to get only the values you can use valuse()

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)
```

## How to use a dictionary: modifying and adding values

**updating a value**

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)
```

**adding a new key**
```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)
```
or use `dictionary.update({"your key" : "value pair"})`

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)
```

## del

Note: removing a key will always cause the removal of the associated value. Values cannot exist without their keys.

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)

```

To remove the last item in a dictionary, you can use the popitem() method:

`dictionary.popitem()`
In the older versions of Python, i.e., before 3.6.7, the popitem() method removes a random item from a dictionary.