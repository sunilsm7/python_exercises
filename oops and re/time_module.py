import time
start = time.time()

now = time.gmtime()
now = time.asctime(now)
print(now)
time.sleep(3)
stop = time.time()

print(stop - start)