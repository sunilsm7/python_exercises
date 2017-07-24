"""Python Loops
15 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Python has only two loops: for loop  and while loop

For loop

For loop Syntax:
"""

for i in iterable_object:
   # do something
1
2
for i in iterable_object:
   # do something
"""   
Note: all the statements inside for  and while loop must be indented to the same number of spaces. Otherwise SyntaxError  will be thrown.

Let’s take an example
"""

my_list = [1,2,3,4]

for i in my_list:
    print(i)
1
2
3
4
my_list = [1,2,3,4]
 
for i in my_list:
    print(i)
Expected Output


1
2
3
4
1
2
3
4
1
2
3
4
here is how for loop works.

In the first iteration i  is assigned value 1  then print statement is executed, In second iteration i  is assigned value  2  then once again print statement is executed. This process continues until there are no more element in the list and for loop exists.

range(a, b) Function

range(a, b)  functions returns sequence of integers from a , a + 1 , a+ 2  …. , b - 2 , b - 1 . For e.g


for i in range(1, 10):
    print(i)
1
2
for i in range(1, 10):
    print(i)
Expected Output:


1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
You can also use range()  function by supplying only one argument like this:


>>> for i in range(10):
...        print(i)

0
1
2
3
4
5
6
7
8
9
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
>>> for i in range(10):
...        print(i)
 
0
1
2
3
4
5
6
7
8
9
here range for loop prints number from 0 to 9.

range(a, b)  function has an optional third parameter to specify the step size. For e.g


for i in range(1, 20, 2):
    print(i)
1
2
for i in range(1, 20, 2):
    print(i)
Expected Output:


1
3
5
7
9
11
13
15
17
19
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
1
3
5
7
9
11
13
15
17
19
While loop

Syntax:


while condition:
    # do something
1
2
while condition:
    # do something
While loop keeps executing statements inside it until condition becomes false. After each iteration condition is checked and if its True then once again statements inside the while loop will be executed.

let’s take an example:


count = 0

while count < 10:
    print(count)
    count += 1
1
2
3
4
5
count = 0
 
while count < 10:
    print(count)
    count += 1
Expected Output:


0
1
2
3
4
5
6
7
8
9
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
0
1
2
3
4
5
6
7
8
9
here while  will keep printing until count  is less than 10.

break statement

break  statement allows to breakout out of the loop.


count = 0

while count < 10:
    count += 1
    if count == 5:
         break    
    print("inside loop", count)


print("out of while loop")
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
count = 0
 
while count < 10:
    count += 1
    if count == 5:
         break    
    print("inside loop", count)
 
 
print("out of while loop")
when count  equals to 5  if condition evaluates to True  and break  keyword breaks out of loop.

Expected Output:


inside loop 1
inside loop 2
inside loop 3
inside loop 4
out of while loop
1
2
3
4
5
inside loop 1
inside loop 2
inside loop 3
inside loop 4
out of while loop
continue statement

When continue  statement encountered in the loop, it ends the current iteration and programs control goes to the end of the loop body.


count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
           continue
    print(count)
1
2
3
4
5
6
7
count = 0
 
while count < 10:
    count += 1
    if count % 2 == 0:
           continue
    print(count)
Expected Output:


1
3
5
7
9
1
2
3
4
5
1
3
5
7
9
As you can see when count % 2 == 0, continue statement is executed which causes the current iteration to end and the control moves on to the next iteration.

In next lesson we will learn about Python mathematical function.