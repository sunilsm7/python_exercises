Python File Handling
9 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

We can use File handling to read and write data to and from the file.

Opening a file

Before reading/writing you first need to open the file. Syntax of opening a file is.


f = open(filename, mode)
1
f = open(filename, mode)
open()  function accepts two arguments filename and mode . filename is a string argument which specify filename  along with it’s path  and mode is also a string argument which is used to specify how file will be used i.e for reading or writing. And f  is a file handler object also known as file pointer.

Closing a file

After you have finished reading/writing to the file you need to close the file using close()  method like this,


f.close()  # where f is a file pointer
1
f.close()  # where f is a file pointer

Different modes of opening a file are

MODES	DESCRIPTION
"r" 	 Open a file for read only
"w" 	 Open a file for writing. If file already exists its data will be cleared before opening. Otherwise new file will be created
"a" 	 Opens a file in append mode i.e to write a data to the end of the file
"wb" 	 Open a file to write in binary mode
"rb" 	 Open a file to read in binary mode
Let’s now look at some examples.

Writing data to the file


>>> f = open('myfile.txt', 'w')    # open file for writing
>>> f.write('this first line\n')   # write a line to the file
>>> f.write('this second line\n')  # write one more line to the file
>>> f.close()                      # close the file
1
2
3
4
>>> f = open('myfile.txt', 'w')    # open file for writing
>>> f.write('this first line\n')   # write a line to the file
>>> f.write('this second line\n')  # write one more line to the file
>>> f.close()                      # close the file
Note: write()  method will not insert new line ( '\n'  ) automatically like print  function, you need to explicitly add '\n'  to write write()  method.

Reading data from the file

To read data back from the file you need one of these three methods.

METHODS	DESCRIPTION
read([number]) 	Return specified number of characters from the file. if omitted it will read the entire contents of the file.
readline() 	Return the next line of the file.
readlines() 	Read all the lines as a list of strings in the file
Reading all the data at once.


>>> f = open('myfile.txt', 'r')
>>> f.read() # read entire content of file at once
"this first line\nthis second line\n"
>>> f.close()
1
2
3
4
>>> f = open('myfile.txt', 'r')
>>> f.read() # read entire content of file at once
"this first line\nthis second line\n"
>>> f.close()
Reading all lines as an array.


>>> f = open('myfile.txt', 'r')
>>> f.readlines() # read entire content of file at once
["this first line\n", "this second line\n"]
>>> f.close()
1
2
3
4
>>> f = open('myfile.txt', 'r')
>>> f.readlines() # read entire content of file at once
["this first line\n", "this second line\n"]
>>> f.close()
Reading only one line.


>>> f = open('myfile.txt', 'r')
>>> f.readline() # read entire content of file at once
"this first line\n"
>>> f.close()
1
2
3
4
>>> f = open('myfile.txt', 'r')
>>> f.readline() # read entire content of file at once
"this first line\n"
>>> f.close()
Appending data

To append the data you need open file in 'a'  mode.


>>> f = open('myfile.txt', 'a')
>>> f.write("this is third line\n")
19
>>> f.close()
1
2
3
4
>>> f = open('myfile.txt', 'a')
>>> f.write("this is third line\n")
19
>>> f.close()
Looping through the data using for loop

You can iterate through the file using file pointer.


>>> f = open('myfile.txt', 'r')
>>> for line in f:
... print(line)
...
this first line
this second line
this is third line

>>> f.close()
1
2
3
4
5
6
7
8
9
>>> f = open('myfile.txt', 'r')
>>> for line in f:
... print(line)
...
this first line
this second line
this is third line
 
>>> f.close()
Binary reading and writing

To perform binary i/o you need to use a module called pickle , pickle  module allows you to read and write data using load  and dump method respectively.

Writing data


>> import pickle
>>> f = open('pick.dat', 'wb')
>>> pickle.dump(11, f)
>>> pickle.dump("this is a line", f)
>>> pickle.dump([1, 2, 3, 4], f)
>>> f.close()
1
2
3
4
5
6
>> import pickle
>>> f = open('pick.dat', 'wb')
>>> pickle.dump(11, f)
>>> pickle.dump("this is a line", f)
>>> pickle.dump([1, 2, 3, 4], f)
>>> f.close()
Reading data


>> import pickle
>>> f = open('pick.dat', 'rb')
>>> pickle.load(f)
11
>>> pickle.load(f)
"this is a line"
>>> pickle.load(f)
[1,2,3,4]
>>> f.close()
1
2
3
4
5
6
7
8
9
>> import pickle
>>> f = open('pick.dat', 'rb')
>>> pickle.load(f)
11
>>> pickle.load(f)
"this is a line"
>>> pickle.load(f)
[1,2,3,4]
>>> f.close()
If there is no more data to read from the file pickle.load()  throws EOFError or end of file error.

In the next lesson we will learn about classes and objects in python.