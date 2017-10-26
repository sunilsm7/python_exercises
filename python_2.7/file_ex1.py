fobj_in = open('myfile.txt', 'r')
fobj_out = open('myfile1.txt', 'w')

i=1
for line in fobj_in:
	print(line.rstrip())
	fobj_out.write("{} : {}".format(str(i), line))
	i += 1

fobj_in.close()
fobj_out.close()