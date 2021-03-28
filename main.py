import sys
import time
from threading import Timer
#making the letters print individualy, (simulated typing)
def slowprint(string):
	for letter in string + '\n':
    #If I used print here, it would print on different lines, idk
		sys.stdout.write(letter)
    #makes the program output each letter at a time, instead of all at once
		sys.stdout.flush()
    #The time between each letter being printed
		time.sleep(0.4/10)
#slowprint("Yay, it works")

#fpoint stands for friendship_points
f_point = 0

def countdown():
   slowprint("\nHello World")
 
# duration is in seconds
t = Timer(5, countdown)
t.start()
# wait for time completion


inpt = input("A: ")
if inpt == "a":
  t.cancel()
 
elif inpt == "b":
  t.cancel()
  slowprint("Hello")

else:
  print("")
  t.join()


