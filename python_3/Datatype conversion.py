Datatype conversion
4 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Once in a while you will want to convert data type of one type to another type. Data type conversion is also known as Type casting.

Converting int to float

To convert int  to float  you need to use float() function.


>>> i = 10
>>> float(i)
10.0
1
2
3
>>> i = 10
>>> float(i)
10.0

Converting float to int

To convert float  to int  you need to use int() function.


>>> f = 14.66
>>> int(f)
14
1
2
3
>>> f = 14.66
>>> int(f)
14
Converting string to int

You can also use int()  to convert string  to int


>>> s = "123"
>>> int(s)
123
1
2
3
>>> s = "123"
>>> int(s)
123
Note: If string contains non numeric character then int()  will throw ValueError.

Converting number to string

To convert number  to string  you need to use str()  function.


>>> i = 100
>>> str(i)
"100"
>>> f = 1.3
str(f)
'1.3'
1
2
3
4
5
6
>>> i = 100
>>> str(i)
"100"
>>> f = 1.3
str(f)
'1.3'
Rounding numbers

To round numbers you need to use round()  function.

Syntax: round(number[, ndigits])


>>> i = 23.97312
>>> round(i, 2)
23.97
1
2
3
>>> i = 23.97312
>>> round(i, 2)
23.97
Next we will cover control statements.