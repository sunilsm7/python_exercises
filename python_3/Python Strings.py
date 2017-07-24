Python Strings
2 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Strings in python are contiguous series of characters delimited by single or double quotes. Python don’t have any separate data type for characters so they are represented as a single character string.

Creating strings


>>> name = "tom" # a string
>>> mychar = 'a' # a character
1
2
>>> name = "tom" # a string
>>> mychar = 'a' # a character
you can also use the following syntax to create strings.


>>> name1 = str() # this will create empty string object
>>> name2 = str("newstring") # string object containing 'newstring'
1
2
>>> name1 = str() # this will create empty string object
>>> name2 = str("newstring") # string object containing 'newstring'
Strings in python are immutable.

What this means to you is that once string is created it can’t be modified. Let’s take an example to illustrate this point.


>>> str1 = "welcome"
>>> str2 = "welcome"
1
2
>>> str1 = "welcome"
>>> str2 = "welcome"
here str1  and str2  refers to the same string object "welcome"  which is stored somewhere in memory. You can test whether str1  refers to same object as str2  using id()  function.

What is id()  : Every object in python is stored somewhere in memory. We can use id()  to get that memory address.


>>> id(str1)
78965411
>>> id(str2)
78965411
1
2
3
4
>>> id(str1)
78965411
>>> id(str2)
78965411
As both str1  and str2  points to same memory location, hence they both points to the same object.

Let’s try to modify str1 object by adding new string to it.


>>> str1 += " mike"
>>> str1
welcome mike
>>> id(str1)
>>> 78965579
1
2
3
4
5
>>> str1 += " mike"
>>> str1
welcome mike
>>> id(str1)
>>> 78965579
As you can see now str1  points to totally different memory location, this proves the point that concatenation doesn’t modify original string object instead it creates a new string object. Similarly Number (i.e int  type) is also immutable.

Operations on string

String index starts from 0 , so to access the first character in the string type:


>>> name[0] #
t
1
2
>>> name[0] #
t
+  operator is used to concatenate string and *  operator is a repetition operator for string.


>>> s = "tom and " + "jerry"
>>> print(s)
tom and jerry
1
2
3
>>> s = "tom and " + "jerry"
>>> print(s)
tom and jerry

>>> s = "this is bad spam " * 3
>>> print(s)
this is bad spam this is bad spam this is bad spam
1
2
3
>>> s = "this is bad spam " * 3
>>> print(s)
this is bad spam this is bad spam this is bad spam
Slicing string

You can take subset of string from original string by using [] operator  also known as slicing operator.

Syntax: s[start:end]

this will return part of the string starting from index start  to index end - 1 .

Let’s take some examples.


>>> s = "Welcome"
>>> s[1:3]
el
1
2
3
>>> s = "Welcome"
>>> s[1:3]
el
Some more examples.


>>> s = "Welcome"
>>> s[ : 6]
'Welcom'

>>> s[4 : ]
'ome'

>>> s[1 : -1]
'elcom'
1
2
3
4
5
6
7
8
9
>>> s = "Welcome"
>>> s[ : 6]
'Welcom'
 
>>> s[4 : ]
'ome'
 
>>> s[1 : -1]
'elcom'
Note: start index and end index are optional. If omitted then the default value of start  index is 0 and that of end is the last index of the string.

ord() and chr() Functions

ord() – function returns the ASCII code of the character.
chr() – function returns character represented by a ASCII number.


>>> ch = 'b'
>>> ord(ch)
98
>>> chr(97)
'a'
>>> ord('A')
65
1
2
3
4
5
6
7
>>> ch = 'b'
>>> ord(ch)
98
>>> chr(97)
'a'
>>> ord('A')
65
String Functions in Python

FUNCTION NAME	FUNCTION DESCRIPTION
len()	returns length of the string
max()	returns character having highest ASCII value
min()	returns character having lowest ASCII value


>>> len("hello")
5
>>> max("abc")
'c'
>>> min("abc")
'a'
1
2
3
4
5
6
>>> len("hello")
5
>>> max("abc")
'c'
>>> min("abc")
'a'
in  and not in  operators

You can use in  and not in  operators to check existence of string in another string. They are also known as membership operator.


>>> s1 = "Welcome"
>>> "come" in s1
True
>>> "come" not in s1
False
>>>
1
2
3
4
5
6
>>> s1 = "Welcome"
>>> "come" in s1
True
>>> "come" not in s1
False
>>>
String comparison

You can use ( > , < , <= , <= , == , !=  ) to compare two strings. Python compares string lexicographically i.e using ASCII value of the characters.

Suppose you have str1  as "Jane"  and str2  as "Jake" . The first two characters from str1  and str2 ( J  and J ) are compared. As they are equal, the second two characters are compared. Because they are also equal, the third two characters ( n  and k ) are compared. And because 'n'  has greater ASCII value than 'k' , str1  is greater than str2 .

Here are some more examples:


>>> "tim" == "tie"
False
>>> "free" != "freedom"
True
>>> "arrow" > "aron"
True
>>> "green" >= "glow"
True
>>> "green" < "glow"
False
>>> "green" <= "glow"
False
>>> "ab" <= "abc"
True
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
>>> "tim" == "tie"
False
>>> "free" != "freedom"
True
>>> "arrow" > "aron"
True
>>> "green" >= "glow"
True
>>> "green" < "glow"
False
>>> "green" <= "glow"
False
>>> "ab" <= "abc"
True
>>>
Iterating string using for loop

String is a sequence type and also iterable using for loop (to learn more about for loop click here).


>>> s = "hello"
>>> for i in s:
... print(i, end="")
hello
1
2
3
4
>>> s = "hello"
>>> for i in s:
... print(i, end="")
hello
Note: By default print()  function prints string with a newline , we change this behavior by supplying a second argument to it as follows.


print("my string", end="\n")  #this is default behavior
1
print("my string", end="\n")  #this is default behavior

print("my string", end="")    # print string without a newline
1
print("my string", end="")    # print string without a newline

print("my string", end="foo")  # now print() will print foo after every string
1
print("my string", end="foo")  # now print() will print foo after every string
Testing strings

String class in python has various inbuilt methods which allows to check for different types of strings.

METHOD NAME	 METHOD DESCRIPTION
isalnum()	Returns True if string is alphanumeric
isalpha()	Returns True if string contains only alphabets
isdigit()	Returns True if string contains only digits
isidentifier()	Return True is string is valid identifier
islower()	Returns True if string is in lowercase
isupper()	Returns True if string is in uppercase
isspace()	Returns True if string contains only whitespace


>>> s = "welcome to python"
>>> s.isalnum()
False
>>> "Welcome".isalpha()
True
>>> "2012".isdigit()
True
>>> "first Number".isidentifier()
False
>>> s.islower()
True
>>> "WELCOME".isupper()
True
>>> "  \t".isspace()
True
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
>>> s = "welcome to python"
>>> s.isalnum()
False
>>> "Welcome".isalpha()
True
>>> "2012".isdigit()
True
>>> "first Number".isidentifier()
False
>>> s.islower()
True
>>> "WELCOME".isupper()
True
>>> "  \t".isspace()
True

 
Searching for Substrings

METHOD NAME	METHODS DESCRIPTION:
endswith(s1: str): bool	Returns True if strings ends with substring s1
startswith(s1: str): bool	Returns True if strings starts with substring s1
count(substring): int	Returns number of occurrences of substring the string
find(s1): int	Returns lowest index from where s1 starts in the string, if string not found returns -1
rfind(s1): int	Returns highest index from where s1 starts in the string, if string not found returns -1


>>> s = "welcome to python"
>>> s.endswith("thon")
True
>>> s.startswith("good")
False
>>> s.find("come")
3
>>> s.find("become")
-1
>>> s.rfind("o")
15
>>> s.count("o")
3
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
>>> s = "welcome to python"
>>> s.endswith("thon")
True
>>> s.startswith("good")
False
>>> s.find("come")
3
>>> s.find("become")
-1
>>> s.rfind("o")
15
>>> s.count("o")
3
>>>
Converting Strings

METHOD NAME	METHOD DESCRIPTION
capitalize(): str	Returns a copy of this string with only the first character capitalized.
lower(): str	Return string by converting every character to lowercase
upper(): str	Return string by converting every character to uppercase
title(): str	This function return string by capitalizing first letter of every word in the string
swapcase(): str	Return a string in which the lowercase letter is converted to uppercase and uppercase to lowercase
replace(old, new): str	This function returns new string by replacing the occurrence of old string with new string


s = "string in python"
>>> s1 = s.capitalize()
>>> s1
'String in python'
>>> s2 = s.title()
>>> s2
'String In Python'
>>> s = "This Is Test"
>>> s3 = s.lower()
>>> s3
'this is test'
>>> s4 = s.upper()
>>> s4
'THIS IS TEST'
>>> s5 = s.swapcase()
>>> s5
'tHIS iS tEST'
>>> s6 = s.replace("Is", "Was")
>>> s6
'This Was Test'
>>> s
'This Is Test'
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
s = "string in python"
>>> s1 = s.capitalize()
>>> s1
'String in python'
>>> s2 = s.title()
>>> s2
'String In Python'
>>> s = "This Is Test"
>>> s3 = s.lower()
>>> s3
'this is test'
>>> s4 = s.upper()
>>> s4
'THIS IS TEST'
>>> s5 = s.swapcase()
>>> s5
'tHIS iS tEST'
>>> s6 = s.replace("Is", "Was")
>>> s6
'This Was Test'
>>> s
'This Is Test'
>>>

In next chapter we will learn about python lists