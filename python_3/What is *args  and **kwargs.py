What is *args ??

*args  allows us to pass variable number of arguments to the function. Let’s take an example to make this clear.

Suppose you created a function to add two number like this.


def sum(a, b):
    print("sum is", a+b)
1
2
def sum(a, b):
    print("sum is", a+b)
As you can see this program only accepts two numbers, what if you want to pass more than two arguments, this is where *args  comes into play.


def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)
1
2
3
4
5
def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)
Now you can pass any number of arguments to the function like this,


>>> sum(1, 2, 3)
6
>>> sum(1, 2, 3, 4, 5, 7)
22
>>> sum(1, 2, 3, 4, 5, 7, 8, 9, 10)
49
>>> sum()
0
1
2
3
4
5
6
7
8
>>> sum(1, 2, 3)
6
>>> sum(1, 2, 3, 4, 5, 7)
22
>>> sum(1, 2, 3, 4, 5, 7, 8, 9, 10)
49
>>> sum()
0
Note: name of *args  is just a convention you can use anything that is a valid identifier. For e.g *myargs is perfectly valid.

What is **kwargs ?

**kwargs allows us to pass variable number of keyword argument like this func_name(name='tim', team='school')


def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)

my_func(name='tim', sport='football', roll=19)
1
2
3
4
5
def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)
 
my_func(name='tim', sport='football', roll=19)
Expected Output:


sport football
roll 19
name tim
1
2
3
sport football
roll 19
name tim
Using *args and **kwargs in function call

You can use *args  to pass elements in an iterable variable to a function. Following example will clear everything.


def my_three(a, b, c):
    print(a, b, c)

a = [1,2,3]
my_three(*a) # here list is broken into three elements
1
2
3
4
5
def my_three(a, b, c):
    print(a, b, c)
 
a = [1,2,3]
my_three(*a) # here list is broken into three elements
Note: This works only when number of argument is same as number of elements in the iterable variable.

Similarly you can use **kwargs  to call a function like this


def my_three(a, b, c):
    print(a, b, c)

a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a)
1
2
3
4
5
def my_three(a, b, c):
    print(a, b, c)
 
a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a)
Note: For this to work 2 things are necessary:

Names of arguments in function must match with the name of keys in dictionary.
Number of arguments should be same as number of keys in the dictionary.
