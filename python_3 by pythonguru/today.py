import datetime
import time

today = time.strftime("%A")
print(time.strftime("%A"))
 
if today == "Monday":
   print("this is Monday")
elif today == "tuesday":
   print("this is tuesday")
elif today == "wednesday":
   print("this is wednesday")
elif today == "Thursday":
   print("this is thursday")
elif today == "Friday":
   print("this is Friday")
elif today == "saturday":
   print("this is saturday")
elif today == "sunday":
   print("this is sunday")
else:
   print("something else")