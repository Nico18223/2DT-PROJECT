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
		time.sleep(0.5/10)
#slowprint("Yay, it works")

def slowerprint(lines):
  for letter in lines + '\n':
    #If I used print here, it would print on different lines, idk
    sys.stdout.write(letter)
    #makes the program output each letter at a time, instead of all at once
    sys.stdout.flush()
    #The time between each letter being printed
    if letter != ' ': time.sleep(0.7/10)


 


#Adds the [YOU]
def pronoun():
  print("[YOU]:", end="", flush = True)
  time.sleep(5/10)
def pronoun1():
  print("[CALLER]:", end="", flush = True)
  time.sleep(5/10)

def end0():
  slowprint("[YOU SAY NOTHING]")
  pronoun1()
  slowprint('"O-oh, I\'m sorry then"')
  pronoun1()
  slowprint('"I\'ll just go"')
  slowprint("*CLICK*")
  slowerprint("[THE CALL IS OVER, YOU CAN'T CALL THEM BACK]".center(100))
  slowerprint("[WHO KNOWS WHAT WILL HAPPEN TO THE POOR KID?]".center(100))
  slowerprint("[CAN YOU IMAGINE THE WEIGHT ON YOUR SHOULDERS, IF THIS WAS REAL?]".center(100))
  slowerprint("[BECAUSE FOR SOME PEOPLE IT IS]".center(100))
  slowerprint("[IN AN AUSTRALIAN STUDY, 135 MENTAL HEALTH WORKERS WERE SURVEYED]".center(100))
  slowerprint("[70.4% OF THEM SAID THAT THEY HAD EXPERIENCED A CLIENT SUICIDE SOMETIME IN THEIR CAREER]".center(96))
end0()
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
#starts a loop, so that if the user inputs something other than yes or no, they will be able to repeat the question
flag = False

while flag == False:
  slowprint("[PLEASE INPUT YES OR NO]")
  start = input().upper()

  if start == "YES":
    slowprint("[GOOD CHOICE]")
    slowprint("[WHAT IS YOUR NAME, PLAYER?]")
    name = input().capitalize()
  
    slowprint("")
    #ends the loop
    flag = True
    

    slowprint("A CALL IS COMING THROUGH")
    slowprint("YOU ANSWER IT")
    print("*CLICK*")
    print(" ")
    slowprint("[NOW YOU HAVE A CHOICE]")
    slowprint("[INPUT THE CORRESPONDING LETTER]")
    slowprint("A: CASUAL")
    slowprint("B: POLITE")
    slowprint("C: STAY SILENT")
    inpt0 = input("").upper()
    if inpt0 == "A":
      f_point += 1
      pronoun()
      slowprint('"Heya, you\'ve reached S.H.I.T, my name is "' + name + '"')
      pronoun()
      slowprint('"What\'s up?"')

    elif inpt0 == "B":
      pronoun()
      slowprint("“Thank you for reaching out, how may I help you?”")
      f_point += 1

    else:
      end0()




  elif start == "NO":
    flag = True
    break

  else:
    flag = False
    