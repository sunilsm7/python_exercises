Python Exception Handling
3 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Exception handling enables you handle errors gracefully and do something meaningful about it. Like display a message to user if intended file not found. Python handles exception using try .. except ..  block.

Syntax:


try:
    # write some code 
    # that might throw exception
except <ExceptionType>: 
    # Exception handler, alert the user
1
2
3
4
5
try:
    # write some code 
    # that might throw exception
except <ExceptionType>: 
    # Exception handler, alert the user
As you can see in try block you need to write code that might throw an exception. When exception occurs code in the try block is skipped. If there exist a matching exception type in except  clause then it’s handler is executed.

Let’s take an example:


try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()
except IOError:
    print('file not found')
1
2
3
4
5
6
try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()
except IOError:
    print('file not found')
 

The above code work as follows:

1. First statement between try  and except  block are executed.
2. If no exception occurs then code under except  clause will be skipped.
3. If file don’t exists then exception will be raised and the rest of the code in the try  block will be skipped
4. When exceptions occurs, if the exception type matches exception name after except  keyword, then the code in that except  clause is executed.

Note: The above code is only capable of handling IOError exception. To handle other kind of exception you need to add more except  clause.

A try  statement can have more than once except  clause, It can also have optional else  and/or finally  statement.


try:
    <body>
except <ExceptionType1>:
    <handler1>
except <ExceptionTypeN>:
    <handlerN>
except:
    <handlerExcept>
else:
    <process_else>
finally:
    <process_finally>
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
try:
    <body>
except <ExceptionType1>:
    <handler1>
except <ExceptionTypeN>:
    <handlerN>
except:
    <handlerExcept>
else:
    <process_else>
finally:
    <process_finally>
except  clause is similar to elif . When exception occurs, it is checked to match the exception type in except  clause. If match is found then handler for the matching case is executed. Also note that in last except  clause ExceptionType  is omitted. If exception does not match any exception type before the last except  clause, then the handler for last except  clause is executed.

Note:  Statements under the else  clause run only when no exception is raised.

Note: Statements in finally  block will run every time no matter exception occurs or not.

Now let’s take an example.


try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")
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
try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)
 
except ZeroDivisionError:
    print("Division by zero is error !!")
 
except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")
 
except:
    print("Wrong input")
 
else:
    print("No exceptions")
 
finally:
    print("This will execute no matter what")
 

Note: The eval()  function lets a python program run python code within itself, eval()  expects a string argument.

To learn more about eval()  see the link http://stackoverflow.com/questions/9383740/what-does-pythons-eval-do

Raising exceptions

To raise your exceptions from your own methods you need to use raise  keyword like this


raise ExceptionClass("Your argument")
1
raise ExceptionClass("Your argument")
Let’s take an example


def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    num = int(input("Enter your age: "))
    enterage(num)

except ValueError:
    print("Only positive integers are allowed")
except:
    print("something is wrong")
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
def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")
 
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")
 
try:
    num = int(input("Enter your age: "))
    enterage(num)
 
except ValueError:
    print("Only positive integers are allowed")
except:
    print("something is wrong")
Run the program and enter positive integer.

Expected Output:


Enter your age: 12
age id even
1
2
Enter your age: 12
age id even
Again run the program and enter a negative number.

Expected Output:


Enter your age: -12
Only integers are allowed
1
2
Enter your age: -12
Only integers are allowed
Using Exception objects

Now you know how to handle exception, in this section we will learn how to access exception object in exception handler code. You can use the following code to assign exception object to a variable.


try:
    # this code is expected to throw exception
except ExceptionType as ex:
    # code to handle exception
1
2
3
4
try:
    # this code is expected to throw exception
except ExceptionType as ex:
    # code to handle exception
As you can see you can store exception object in variable ex . Now you can use this object in exception handler code


try:
    number = eval(input("Enter a number: "))
    print("The number entered is", number)
except NameError as ex:
    print("Exception:", ex)
1
2
3
4
5
try:
    number = eval(input("Enter a number: "))
    print("The number entered is", number)
except NameError as ex:
    print("Exception:", ex)
Run the program and enter a number.

Expected Output:


Enter a number: 34
The number entered is 34
1
2
Enter a number: 34
The number entered is 34
Again run the program and enter a string .

Expected Output:


Enter a number: one
Exception: name 'one' is not defined
1
2
Enter a number: one
Exception: name 'one' is not defined
Creating custom exception class

You can create a custom exception class by Extending BaseException  class or subclass of BaseException .

python exception classes

As you can see from most of the exception classes in python extends from the BaseException  class. You can derive you own exception class from BaseException  class or from sublcass of BaseException  like RuntimeError .

Create a new file called NegativeAgeException.py  and write the following code.


class NegativeAgeException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
1
2
3
4
class NegativeAgeException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
Above code creates a new exception class named NegativeAgeException , which consists of only constructor which call parent class constructor using super().__init__()  and sets the age .

Using custom exception class


def enterage(age):
    if age < 0:
        raise NegativeAgeException("Only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    num = int(input("Enter your age: "))
    enterage(num)
except NegativeAgeException:
    print("Only positive integers are allowed")
except:
    print("something is wrong")
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
def enterage(age):
    if age < 0:
        raise NegativeAgeException("Only positive integers are allowed")
 
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")
 
try:
    num = int(input("Enter your age: "))
    enterage(num)
except NegativeAgeException:
    print("Only positive integers are allowed")
except:
    print("something is wrong")
In the next post we will learn about Python Modules.

