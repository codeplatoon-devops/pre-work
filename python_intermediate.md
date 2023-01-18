# Intermediate Python

## Topics Covered / Goals
- Understand lambda functions
- Understand list methods map(), filter(), sort(), reduce()
- Understand ternary statements
- Understand list comprehensions
- Understand Try-Except error handling

### Lambda functions
- temporary, unnamed ("anonymous") functions
```python
## typical function example
def add_one(x):
    return x + 1

print(add_one(7)) # output would be 8

## lambda function example
add_two = lambda x : x + 2

print(add_two(7)) # output would be 9
```

### List Methods
**map()**
- creates a new list, using a function that returns a new item
```python
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = map(lambda item : item + 2, my_list)
for x in new_list:
    print(x)
## [3,4,5,6,7,8,9,10,11,12]
```

**filter()**
- creates a new list, using a function that returns a bool (True => include item in new list)
```python
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = filter(lambda item : item % 3 == 0, my_list)
for x in new_list:
    print(x)
## [3,6,9]
```

**reduce()**
- creates a single value, using a function that aggregates values
```python
import functools
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = functools.reduce(lambda agg, item : agg + item, my_list)
print(sum)
```

## Ternary Statements
- inline if-statements
```python
## if statement
x = None
y = 9
if y > 5:
    x = "donuts"
else:
    x = "bagels"

print(x)

## ternary statement
x = "donuts" if y > 5 else "bagels"
print(x)
```

### List Comprehensions
```python
full_list = [a for a in range(10)]
print(full_list)

evens_list = [x for x in range(10) if x % 2 == 0]
print(my_list)

some_list = ["donuts" if x % 2 == 0 else "bagels" for x in range(10) if x % 3 == 0]
print(some_list)
```

### Try-Except
```python
try:
    a = 1
    b = 2
    c = "donuts"
    
    d = a + b
    print(d)

    e = a + c # error
    print(e)
except:
    # handle exception
    print("BOO! there was an error")
else:
    # handle success
    print("YAY! there was no error")
finally:
    # always execute regardless of exception or success
    print("donuts are yummy!")
```

## Modules, Packages, Libraries, and Frameworks

- Modules, libraries, frameworks, and packages are just code that someone else wrote ahead of time to make your life as a developer easier. There is no magic here - it's just meant to make your life easier and for you to make more robust applications
- There are a number of package managers to manage the different libraries we will use. The most popular package manager for Python is Pip, and the most popular (and default) package manager for Javascript is npm. 
- You can find some very useful libraries [here](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/). We'll be using Django in the next few weeks. If you go the data science route, there are some data science heavy libraries like NumPy and Pandas

You can also write your own modules, which allows for you as the author to organize your code and group it together for ease of use. To put it very simply, a module is a file of Python code that you bring into other files. Let's take a look at an example:

### Python modules

```python
## file1.py
def say_hello():
    print('Hey there')

## file2.py
import file1
import file1 as anything
anything.say_hello()
```
We just created two files: `file1.py` and `file2.py`. `file1.py` has a `say_hello` function. `file2.py` has nothing in it, but imports that file in as the name of the file and we can use all the methods in that file. We can also rewrite it as `import file1 as anything` and call `anything.say_hello()`. You can `import` anything into your file by providing the correct relative path to the file. More on that can be found under external resources.

## Resources
- [Python Modules](https://www.tutorialspoint.com/python/python_modules.htm)

## Assignments

- [Armstrong Numbers](https://github.com/codeplatoon-devops/algo-armstrong-numbers)
- [Sum Pairs](https://github.com/codeplatoon-devops/algo-sum-pairs)
- [Credit Check](https://github.com/codeplatoon-devops/algo-credit-check)
- [Anagrams I](https://github.com/codeplatoon-devops/algo-anagrams-i)
- [Debugging One](https://github.com/codeplatoon-devops/algo-debugging-one)
