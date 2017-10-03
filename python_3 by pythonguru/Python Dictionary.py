
Python Dictionaries
4 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Dictionary is a python data type that is used to store key value pairs. It enables you to quickly retrieve, add, remove, modify, values using key. Dictionary is very similar to what we call associative array or hash on other languages.

Note: Dictionaries are mutable.

Creating Dictionary

Dictionaries can be created using pair of curly braces ( {}  ). Each item in the dictionary consist of key, followed by a colon, which is followed by value. And each item is separated using commas ( ,). Let’s take an example.


friends = {
'tom' : '111-222-333',
'jerry' : '666-33-111'
}
1
2
3
4
friends = {
'tom' : '111-222-333',
'jerry' : '666-33-111'
}
here friends  is a dictionary with two items. One point to note that key must be of hashable type, but value can be of any type. Each key in the dictionary must be unique.


>>> dict_emp = {} # this will create an empty dictionary
1
>>> dict_emp = {} # this will create an empty dictionary
Retrieving, modifying and adding elements in the dictionary

To get an item from dictionary, use the following syntax:


>>> dictionary_name['key']
1
>>> dictionary_name['key']

>>> friends['tom']
'111-222-333'
1
2
>>> friends['tom']
'111-222-333'
if the key exists in the dictionary, the value will be returned otherwise KeyError exception will be thrown.

To add or modify an item, use the following syntax:


>>> dictionary_name['newkey'] = 'newvalue'
1
>>> dictionary_name['newkey'] = 'newvalue'

>>> friends['bob'] = '888-999-666'
>>> friends
 {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
1
2
3
>>> friends['bob'] = '888-999-666'
>>> friends
 {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
Deleting Items from dictionary.


>>> del dictionary_name['key']
1
>>> del dictionary_name['key']

>>>  del friends['bob']
>>>  friends
{'tom': '111-222-333', 'jerry': '666-33-111'}
1
2
3
>>>  del friends['bob']
>>>  friends
{'tom': '111-222-333', 'jerry': '666-33-111'}
If the key is found then item will be deleted otherwise KeyError  exception will be thrown.

Looping items in the dictionary

You can use for loop to traverse elements in the dictionary.


>>> friends = {
... 'tom' : '111-222-333',
... 'jerry' : '666-33-111'
...}
>>>
>>> for key in friends:
... print(key, ":", friends[key])
...
tom : 111-222-333
jerry : 666-33-111
>>>
>>>
1
2
3
4
5
6
7
8
9
10
11
12
>>> friends = {
... 'tom' : '111-222-333',
... 'jerry' : '666-33-111'
...}
>>>
>>> for key in friends:
... print(key, ":", friends[key])
...
tom : 111-222-333
jerry : 666-33-111
>>>
>>>
Find the length of the dictionary

You can use len()  function to find the length of the dictionary.


>>> len(friends)
2
1
2
>>> len(friends)
2
in or not in operators

in  and not in  operators to check whether key exists in the dictionary.


>>> 'tom' in friends
True
>>> 'tom' not in friends
False
1
2
3
4
>>> 'tom' in friends
True
>>> 'tom' not in friends
False
Equality Tests in dictionary

==  and !=  operators tells whether dictionary contains same items not.


>>> d1 = {"mike":41, "bob":3}
>>> d2 = {"bob":3, "mike":41}
>>> d1 == d2
True
>>> d1 != d2
False
>>>
1
2
3
4
5
6
7
>>> d1 = {"mike":41, "bob":3}
>>> d2 = {"bob":3, "mike":41}
>>> d1 == d2
True
>>> d1 != d2
False
>>>
Note: You can’t use other relational operators like <  , > , >= , <=  to compare dictionaries.

Dictionary methods

Python provides you several built-in methods for working with dictionaries.

METHODS	DESCRIPTION
popitem()	Returns randomly select item from dictionary and also remove the selected item.
clear()	Delete everything from dictionary
keys()	Return keys in dictionary as tuples
values()	Return values in dictionary as tuples
get(key)	Return value of key, if key is not found it returns None, instead on throwing KeyError exception
pop(key)	Remove the item from the dictionary, if key is not found KeyError will be thrown


>>> friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}

>>> friends.popitem()
('tom', '111-222-333')

>>> friends.clear()

>>>  friends
{}

>>> friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}

>>> friends.keys()
dict_keys(['tom', 'bob', 'jerry'])

>>> friends.values()
dict_values(['111-222-333', '888-999-666', '666-33-111'])

>>> friends.get('tom')
'111-222-333'

>>> friends.get('mike', 'Not Exists')
'Not Exists'

>>> friends.pop('bob')
'888-999-666'

>>> friends
{'tom': '111-222-333', 'jerry': '666-33-111'}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
>>> friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
 
>>> friends.popitem()
('tom', '111-222-333')
 
>>> friends.clear()
 
>>>  friends
{}
 
>>> friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
 
>>> friends.keys()
dict_keys(['tom', 'bob', 'jerry'])
 
>>> friends.values()
dict_values(['111-222-333', '888-999-666', '666-33-111'])
 
>>> friends.get('tom')
'111-222-333'
 
>>> friends.get('mike', 'Not Exists')
'Not Exists'
 
>>> friends.pop('bob')
'888-999-666'
 
>>> friends
{'tom': '111-222-333', 'jerry': '666-33-111'}

 
In next post we will learn about Python tuples.

