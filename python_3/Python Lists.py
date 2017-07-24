Python Lists
4 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

List type is another sequence type defined by the list class of python. List allows you add, delete or process elements in very simple ways. List is very similar to arrays.

Creating list in python

You can create list using the following syntax.


>>> l = [1, 2, 3, 4]
1
>>> l = [1, 2, 3, 4]

here each elements in the list is separated by comma and enclosed by a pair of square brackets ( [] ). Elements in the list can be of same type or different type. For e.g:


l2 = ["this is a string", 12]
1
l2 = ["this is a string", 12]
Other ways of creating list.


list1 = list() # Create an empty list
list2 = list([22, 31, 61]) # Create a list with elements 22, 31, 61
list3 = list(["tom", "jerry", "spyke"]) # Create a list with strings
list5 = list("python") # Create a list with characters p, y, t, h, o, n
1
2
3
4
list1 = list() # Create an empty list
list2 = list([22, 31, 61]) # Create a list with elements 22, 31, 61
list3 = list(["tom", "jerry", "spyke"]) # Create a list with strings
list5 = list("python") # Create a list with characters p, y, t, h, o, n

Note: Lists are mutable.

Accessing elements in list

You can use index operator ( [] ) to access individual elements in the list. List index starts from 0.


>>> l = [1,2,3,4,5]
>>> l[1] # access second element in the list
2
>>> l[0] # access first element in the list
1
1
2
3
4
5
>>> l = [1,2,3,4,5]
>>> l[1] # access second element in the list
2
>>> l[0] # access first element in the list
1
 

List Common Operations

METHOD NAME	DESCRIPTION
x in s 	True if element x is in sequence s.
x not in s   	if element x is not in sequence s.
s1 + s2   	Concatenates two sequences s1 and s2
s * n , n * s 	n copies of sequence s concatenated
s[i] 	 ith element in sequence s.
len(s) 	Length of sequence s, i.e. the number of elements in s.
min(s) 	Smallest element in sequence s.
max(s) 	Largest element in sequence s.
sum(s)   	 Sum of all numbers in sequence s.
for loop 	 Traverses elements from left to right in a for loop.

List examples using functions

>>> list1 = [2, 3, 4, 1, 32]
>>> 2 in list1
True
>>> 33 not in list1
True
>>> len(list1) # find the number of elements in the list
5
>>> max(list1) # find the largest element in the list
32
>>> min(list1) # find the smallest element in the list
1
>>> sum(list1) # sum of elements in the list
42
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
>>> list1 = [2, 3, 4, 1, 32]
>>> 2 in list1
True
>>> 33 not in list1
True
>>> len(list1) # find the number of elements in the list
5
>>> max(list1) # find the largest element in the list
32
>>> min(list1) # find the smallest element in the list
1
>>> sum(list1) # sum of elements in the list
42

 
List slicing

Slice operator ( [start:end] ) allows to fetch sublist from the list. It works similar to string.


>>> list = [11,33,44,66,788,1]
>>> list[0:5] # this will return list starting from index 0 to index 4
[11,33,44,66,788]
1
2
3
>>> list = [11,33,44,66,788,1]
>>> list[0:5] # this will return list starting from index 0 to index 4
[11,33,44,66,788]

>>> list[:3] 
[11,33,44]
1
2
>>> list[:3] 
[11,33,44]
Similar to string start  index is optional, if omitted it will be 0.


>>> list[2:] 
[44,66,788,1]
1
2
>>> list[2:] 
[44,66,788,1]
end  index is also optional, if omitted it will be set to the last index of the list.

Note: If start >= end , list[start : end]  will return an empty list. If end specifies a
position which is beyond the end  of the list, Python will use the length of the list for end  instead.

+  and *  operators in list

+  operator joins the two list.


>>> list1 = [11, 33]
>>> list2 = [1, 9]
>>> list3 = list1 + list2
>>> list3
[11, 33, 1, 9]
1
2
3
4
5
>>> list1 = [11, 33]
>>> list2 = [1, 9]
>>> list3 = list1 + list2
>>> list3
[11, 33, 1, 9]
 

*  operator replicates the elements in the list.


>>> list4 = [1, 2, 3, 4]
>>> list5 = list4 * 3
>>> list5
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
1
2
3
4
>>> list4 = [1, 2, 3, 4]
>>> list5 = list4 * 3
>>> list5
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
 

in  or not in operator

in  operator is used to determine whether the elements exists in the list. On success it returns True  on failure it returns False .


>>> list1 = [11, 22, 44, 16, 77, 98]
>>> 22 in list1
True
1
2
3
>>> list1 = [11, 22, 44, 16, 77, 98]
>>> 22 in list1
True
Similarly not in  is opposite of in  operator.


>>> 22 not in list1
False
1
2
>>> 22 not in list1
False
Traversing list using for loop

As already discussed list is a sequence and also iterable. Means you can use for loop to loop through all the elements of the list.


>>> list = [1,2,3,4,5]
>>> for i in list:
... print(i, end=" ")
1 2 3 4 5
1
2
3
4
>>> list = [1,2,3,4,5]
>>> for i in list:
... print(i, end=" ")
1 2 3 4 5
 

Commonly used list methods with return type

METHOD NAME	DESCRIPTION
append(x:object):None	 Adds an element x to the end of the list and returns None.
count(x:object):int	 Returns the number of times element x appears in the list.
extend(l:list):None	Appends all the elements in l  to the list and returns None.
index(x: object):int 	Returns the index of the first occurrence of element x in the list
insert(index: int, x: object):None 	Inserts an element x at a given index. Note that the first element in the list has index 0 and returns None..
remove(x:object):None 	Removes the first occurrence of element x from the list and returns None
reverse():None 	 Reverse the list and returns None
sort(): None 	Sorts the elements in the list in ascending order and returns None.
pop(i): object 	Removes the element at the given position and returns it. The parameter i is optional. If it is not specified, pop() removes and returns the last element in the list.
 


>>> list1 = [2, 3, 4, 1, 32, 4]
>>> list1.append(19)
>>> list1
[2, 3, 4, 1, 32, 4, 19]
>>> list1.count(4) # Return the count for number 4
2
>>> list2 = [99, 54]
>>> list1.extend(list2)
>>> list1
[2, 3, 4, 1, 32, 4, 19, 99, 54]
>>> list1.index(4) # Return the index of number 4
2
>>> list1.insert(1, 25) # Insert 25 at position index 1
>>> list1
[2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
>>>
>>> list1 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
>>> list1.pop(2)
3
>>> list1
[2, 25, 4, 1, 32, 4, 19, 99, 54]
>>> list1.pop()
54
>>> list1
[2, 25, 4, 1, 32, 4, 19, 99]
>>> list1.remove(32) # Remove number 32
>>> list1
[2, 25, 4, 1, 4, 19, 99]
>>> list1.reverse() # Reverse the list
>>> list1
[99, 19, 4, 1, 4, 25, 2]
>>> list1.sort() # Sort the list
>>> list1
[1, 2, 4, 4, 19, 25, 99]
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
30
31
32
33
34
35
>>> list1 = [2, 3, 4, 1, 32, 4]
>>> list1.append(19)
>>> list1
[2, 3, 4, 1, 32, 4, 19]
>>> list1.count(4) # Return the count for number 4
2
>>> list2 = [99, 54]
>>> list1.extend(list2)
>>> list1
[2, 3, 4, 1, 32, 4, 19, 99, 54]
>>> list1.index(4) # Return the index of number 4
2
>>> list1.insert(1, 25) # Insert 25 at position index 1
>>> list1
[2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
>>>
>>> list1 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
>>> list1.pop(2)
3
>>> list1
[2, 25, 4, 1, 32, 4, 19, 99, 54]
>>> list1.pop()
54
>>> list1
[2, 25, 4, 1, 32, 4, 19, 99]
>>> list1.remove(32) # Remove number 32
>>> list1
[2, 25, 4, 1, 4, 19, 99]
>>> list1.reverse() # Reverse the list
>>> list1
[99, 19, 4, 1, 4, 25, 2]
>>> list1.sort() # Sort the list
>>> list1
[1, 2, 4, 4, 19, 25, 99]
>>>
List Comprehension

Note: This topic needs to have a working knowledge of python for loops.

List comprehension provides a concise way to create list. It consists of square brackets containing expression followed by for clause then zero or more for or if clauses.

here are some examples:


>>> list1 = [ x for x in range(10) ]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> list2 = [ x + 1 for x in range(10) ]
>>> list2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> list3 = [ x for x in range(10) if x % 2 == 0 ]
>>> list3
[0, 2, 4, 6, 8]

>>> list4 = [ x *2 for x in range(10) if x % 2 == 0 ]
[0, 4, 8, 12, 16]
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
>>> list1 = [ x for x in range(10) ]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
>>> list2 = [ x + 1 for x in range(10) ]
>>> list2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
>>> list3 = [ x for x in range(10) if x % 2 == 0 ]
>>> list3
[0, 2, 4, 6, 8]
 
>>> list4 = [ x *2 for x in range(10) if x % 2 == 0 ]
[0, 4, 8, 12, 16]
 

In the next tutorial we will learn about python dictionaries.