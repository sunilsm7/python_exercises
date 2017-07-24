Python Generators
2 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Generators are function used to create iterators, so that it can be used in the for loop.

Creating Generators

Generators are defined similar to function but there is only one difference, we use yield  keyword to return value used for each iteration of the for loop. Let’s see an example where we are trying to clone python’s built-in range()  function.


def my_range(start, stop, step = 1):
    if stop <= start:
        raise RuntimeError("start must be smaller than stop")
    i = start
    while i < stop:
        yield i
        i += step

try:
    for k in my_range(10, 50, 3):
        print(k)
except RuntimeError as ex:
    print(ex)
except:
    print("Unknown error occurred")
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
def my_range(start, stop, step = 1):
    if stop <= start:
        raise RuntimeError("start must be smaller than stop")
    i = start
    while i < stop:
        yield i
        i += step
 
try:
    for k in my_range(10, 50, 3):
        print(k)
except RuntimeError as ex:
    print(ex)
except:
    print("Unknown error occurred")
Expected Output:


10
13
16
19
22
25
28
31
34
37
40
43
46
49
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
10
13
16
19
22
25
28
31
34
37
40
43
46
49
Here is how my_range()  works:

In for loop my_range()  function get called, it initializes values of the three arguments( start , stop  and step ) and also checks whether stop  is smaller than or equal to start , if it is not then i  is assigned value of start . At this point i  is 10 so while condition evaluates to True  and while loop starts executing. In next statement yield transfer control to the for loop and assigns current value of i to variable k , inside the for loop print statement get executed, then the control again passes to line 7 inside the function my_range()  where i  gets incremented. This process keeps on repeating until i < stop .

