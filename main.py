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

#def countdown():
   #slowprint("\nHello World")
 
# duration is in seconds
#t = Timer(5, countdown)
#t.start()
# wait for time completion


#inpt = input("A: ")
#if inpt == "a":
  #t.cancel()
 
#elif inpt == "b":
  #t.cancel()
  #slowprint("Hello")

#else:
  #print("")
  #t.join()

#game actually starts
print(" ")
print("[WARNING: THE FOLLOWING GAME INCLUDES MENTIONS OF SUICIDE AND/OR SELF HARM]")
print("[IF THIS MAKES YOU UNCOMFORTABLE PLEASE PROCEED WITH CAUTION]")
print(" ")
slowprint("[WELCOME TO [GAME]]")
slowprint("[WOULD YOU LIKE TO START?]")
flag = False
def pronoun():
  print("[YOU]:", end="", flush = True)
while flag == False:
  slowprint("[PLEASE INPUT YES OR NO]")
  start = input().upper()

  if start == "YES":
    slowprint("")
    flag = True
    

    slowprint("A call is coming through")
    slowprint("You answer it")
    print("*CLICK*")
    print(" ")
    slowprint("[NOW YOU HAVE A CHOICE]")
    slowprint("[INPUT THE CORRESPONDING LETTER]")
    slowprint("A: CASUAL")
    slowprint("B: POLITE")
    slowprint("C: STAY SILENT")
    inpt0 = input("").upper()
    if inpt0 == "A":
      pronoun()
      slowprint(" 'Hello' ")




  elif start == "NO":
    flag = True
    break

  else:
    flag = False
    