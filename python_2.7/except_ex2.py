try:
	f = open('testfile','r')
	f.write('Test write this')
except:
	# This will check for any exception and then execute this print statement
   print "Error: Could not find file or read data"
else:
   print "Content written successfully"
   f.close()