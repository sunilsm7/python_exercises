Python inheritance and polymorphism
12 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Inheritance allows programmer to create a general class first then later extend it to more specialized class. It also allows programmer to write better code.

Using inheritance you can inherit all access data fields and methods, plus you can add your own methods and fields, thus inheritance provide a way to organize code, rather than rewriting it from scratch.

In object-oriented terminology when class X  extend class Y , then Y  is called super class or base class and X  is called subclass or derived class. One more point to note that only data fields and method which are not private are accessible by child classes, private data fields and methods are accessible only inside the class.

Syntax to create a subclass is:


class SubClass(SuperClass):
  # data fields
  # instance methods
1
2
3
class SubClass(SuperClass):
  # data fields
  # instance methods
Let take an example to illustrate the point.


class Vehicle:

    def __init__(self, name, color):
        self.__name = name      # __name is private to Vehicle class
        self.__color = color

    def getColor(self):         # getColor() function is accessible to class Car
        return self.__color

    def setColor(self, color):  # setColor is accessible outside the class
        self.__color = color

    def getName(self):          # getName() is accessible outside the class
        return self.__name

class Car(Vehicle):

    def __init__(self, name, color, model):
        # call parent constructor to set name and color  
        super().__init__(name, color)       
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"

# in method getDescrition we are able to call getName(), getColor() because they are 
# accessible to child class through inheritance

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName()) # car has no method getName() but it is accessible through class Vehicle
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
class Vehicle:
 
    def __init__(self, name, color):
        self.__name = name      # __name is private to Vehicle class
        self.__color = color
 
    def getColor(self):         # getColor() function is accessible to class Car
        return self.__color
 
    def setColor(self, color):  # setColor is accessible outside the class
        self.__color = color
 
    def getName(self):          # getName() is accessible outside the class
        return self.__name
 
class Car(Vehicle):
 
    def __init__(self, name, color, model):
        # call parent constructor to set name and color  
        super().__init__(name, color)       
        self.__model = model
 
    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"
 
# in method getDescrition we are able to call getName(), getColor() because they are 
# accessible to child class through inheritance
 
c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName()) # car has no method getName() but it is accessible through class Vehicle
Expected Output:


Ford MustangGT350 in red color
Ford Mustang
1
2
Ford MustangGT350 in red color
Ford Mustang
here we have created base class Vehicle  and it’s subclass Car . Notice that we have not defined getName()  in Car  class but we are still able to access it, because class Car  inherits it from Vehicle  class. In the above code super()  method is used to call method of the base class. Here is the how super()  works

Suppose you need to call a method called get_information()  in the base class from child class , you can do so using the following code.


super().get_information()
1
super().get_information()
similarly you can call base class constructor from child class constructor using the following code.


super().__init__()
1
super().__init__()
Multiple inheritance

Unlike languages like Java and C#, python allows multiple inheritance i.e you can inherit from multiple classes at the same time like this,


class Subclass(SuperClass1, SuperClass2, ...):
   # initializer
   # methods
1
2
3
class Subclass(SuperClass1, SuperClass2, ...):
   # initializer
   # methods
Let’s take an example:


class MySuperClass1():

    def method_super1(self):
        print("method_super1 method called")

class MySuperClass2():

    def method_super2(self):
        print("method_super2 method called")

class ChildClass(MySuperClass1, MySuperClass2):

    def child_method(self):
        print("child method")

c = ChildClass()
c.method_super1()
c.method_super2()
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
class MySuperClass1():
 
    def method_super1(self):
        print("method_super1 method called")
 
class MySuperClass2():
 
    def method_super2(self):
        print("method_super2 method called")
 
class ChildClass(MySuperClass1, MySuperClass2):
 
    def child_method(self):
        print("child method")
 
c = ChildClass()
c.method_super1()
c.method_super2()
Expected Output:


method_super1 method called
method_super2 method called
1
2
method_super1 method called
method_super2 method called
As you can see becuase ChildClass  inherited MySuperClass1 , MySuperClass2 , object of ChildClass  is now able to access method_super1()  and method_super2() .

Overriding methods

To override a method in the base class, sub class needs to define a method of same signature. (i.e same method name and same number of parameters as method in base class).


class A():

    def __init__(self):
        self.__x = 1

    def m1(self):
        print("m1 from A")


class B(A):

    def __init__(self):
        self.__y = 1

    def m1(self):
        print("m1 from B")

c = B()
c.m1()
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
class A():
 
    def __init__(self):
        self.__x = 1
 
    def m1(self):
        print("m1 from A")
 
 
class B(A):
 
    def __init__(self):
        self.__y = 1
 
    def m1(self):
        print("m1 from B")
 
c = B()
c.m1()
Expected Output:


m1 from B
1
m1 from B
Here we are overriding m1()  method from the base class. Try commenting m1()  method  in B  class and now m1()  method from Base class i.e class A  will run.

Expected Output:


m1 from A
1
m1 from A
isinstance() function

isinstance()  function is used to determine whether the object is an instance of the class or not.

Syntax: isinstance(object, class_type)


>>> isinstance(1, int)
True

>>> isinstance(1.2, int)
False

>>> isinstance([1,2,3,4], list)
True
1
2
3
4
5
6
7
8
>>> isinstance(1, int)
True
 
>>> isinstance(1.2, int)
False
 
>>> isinstance([1,2,3,4], list)
True