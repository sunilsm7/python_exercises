Python Modules
Leave a reply
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Python module is a normal python file which can store function, variable, classes, constants etc. Module helps us to organize related codes . For e.g math module in python has mathematical related functions.

Creating module

Create a new file called mymodule.py and write the following code.


foo = 100

def hello():
    print("i am from mymodule.py")
1
2
3
4
foo = 100
 
def hello():
    print("i am from mymodule.py")

as you can see we have defined a global variable foo  and a function hello()  in our module. Now to use this module in our programs we first need to import it using import statement like this


import mymodule
1
import mymodule
now you can use variable and call functions in the  mymodule.py  using the following code.


import mymodule

print(mymodule.foo)
print(mymodule.hello())
1
2
3
4
import mymodule
 
print(mymodule.foo)
print(mymodule.hello())
Expected Output:


100
i am from mymodule.py
1
2
100
i am from mymodule.py
Remember you need to specify name of module first to access it’s variables and functions, failure to so will result in error.

Using from  with import

Using import statements imports everything in the module, what if you want to access only specific function or variable ? This is where from  statement comes, here is how to use it.


from mymodule import foo # this statement import only foo variable from mymodule
print(foo)
1
2
from mymodule import foo # this statement import only foo variable from mymodule
print(foo)
Expected output:


100
1
100
Note: In this case you don’t need to specify module name to access variables and function.

dir() method

dir() is an in-built method used to find all attributes (i.e all available classes, functions, variables and constants ) of the object. As we have already discussed everything in python is object, we can use dir() method to find attributes of the module like this:


dir(module_name)
1
dir(module_name)
dir() returns a list of string containing the names of the available attributes.


>>> dir(mymodule)
['__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', 'foo', 'hello']
1
2
3
>>> dir(mymodule)
['__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', 'foo', 'hello']
As you can see besides foo and hello there are additional attributes in the mymodule . These are in-built attributes which python provides to all the modules automatically.

