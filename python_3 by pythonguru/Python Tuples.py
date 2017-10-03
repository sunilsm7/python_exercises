Python Tuples
Leave a reply
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

In Python Tuples are very similar to list but once a tuple is created, you cannot add, delete, replace, reorder elements.

Note: Tuples are immutable.

Creating a tuple


>>> t1 = () # creates an empty tuple with no data

>>> t2 = (11,22,33)

>>> t3 = tuple([1,2,3,4,4]) # tuple from array

>>> t4 = tuple("abc") # tuple from string
1
2
3
4
5
6
7
>>> t1 = () # creates an empty tuple with no data
 
>>> t2 = (11,22,33)
 
>>> t3 = tuple([1,2,3,4,4]) # tuple from array
 
>>> t4 = tuple("abc") # tuple from string

Tuples functions

Functions like max , min , len , sum  can also be used with tuples.


>>> t1 = (1, 12, 55, 12, 81)
>>> min(t1)
1
>>> max(t1)
81
>>> sum(t1)
161
>>> len(t1)
5
1
2
3
4
5
6
7
8
9
>>> t1 = (1, 12, 55, 12, 81)
>>> min(t1)
1
>>> max(t1)
81
>>> sum(t1)
161
>>> len(t1)
5
Iterating through tuples

Tuples are iterable using for loop [ Learn more about for loop here ] .


>>> t = (11,22,33,44,55)
>>> for i in t:
... print(i, end=" ")
>>> 11 22 33 44 55
1
2
3
4
>>> t = (11,22,33,44,55)
>>> for i in t:
... print(i, end=" ")
>>> 11 22 33 44 55
Slicing tuples

Slicing operators works same in tuples as in list and string.


>>> t = (11,22,33,44,55)
>>> t[0:2]
(11,22)
1
2
3
>>> t = (11,22,33,44,55)
>>> t[0:2]
(11,22)
in  and not in  operator

You can use in  and not in  operators to check existence of item in tuples as follows.


>>> t = (11,22,33,44,55)
>>> 22 in t
True
>>> 22 not in t
False
1
2
3
4
5
>>> t = (11,22,33,44,55)
>>> 22 in t
True
>>> 22 not in t
False
In next chapter we will learn about python data type conversion.

