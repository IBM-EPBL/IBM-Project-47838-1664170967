import random   #importing random values
import time     #importing time to introduce delay between instantaneous random values
while (True):   #looping the random values
  time.sleep(1)
  a=random.randint(10,70)   #getting random values as a for temperature
  b=random.randint(10,99)   #getting random values as a for humidity
    
  if(a>35 and b>60):
    print("high temperature and humidity of:",a,b,"%","alarm is on")
  elif(a<35 and b<60):
    print("Normal temperature and humidity of:",a,b,"%","alarm is off")
  continue
