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

def fastprint(lines):
  for letter in lines + '\n':
    #If I used print here, it would print on different lines, idk
    sys.stdout.write(letter)
    #makes the program output each letter at a time, instead of all at once
    sys.stdout.flush()
    #The time between each letter being printed
    time.sleep(0.2/10)
def avgprint(lines):
  for letter in lines + '\n':
    #If I used print here, it would print on different lines, idk
    sys.stdout.write(letter)
    #makes the program output each letter at a time, instead of all at once
    sys.stdout.flush()
    #The time between each letter being printed
    time.sleep(0.4/10) 

#Adds the [YOU]
def pronoun():
  print("[YOU]:", end="", flush = True)
  time.sleep(5/10)

def pronoun1():
  print("[CALLER]:", end="", flush = True)
  time.sleep(5/10)

def endcard():
  slowerprint("[THE CALL IS OVER, YOU CAN'T CALL THEM BACK]".center(100))
  slowerprint("[WHO KNOWS WHAT WILL HAPPEN TO THE POOR KID?]".center(100))
  slowerprint("[CAN YOU IMAGINE THE WEIGHT ON YOUR SHOULDERS, IF THIS WAS REAL?]".center(100))
  slowerprint("[BECAUSE FOR SOME PEOPLE IT IS]".center(100))
  slowerprint("[IN AN AUSTRALIAN STUDY, 135 MENTAL HEALTH WORKERS WERE SURVEYED]".center(100))
  slowerprint("[70.4% OF THEM SAID THAT THEY HAD EXPERIENCED A CLIENT SUICIDE SOMETIME IN THEIR CAREER]".center(93))

def end0():
  slowprint("\n[YOU SAY NOTHING]")
  pronoun1()
  slowprint('"O-oh, I\'m sorry then"')
  pronoun1()
  slowprint('"I\'ll just go"')
  slowprint("*CLICK*")

def c3():
  pronoun1()
  slowprint('"I know, it\'s dumb"')
  pronoun1()
  slowprint('"I\ll just go"')
  slowprint("*CLICK*")
  slowprint("[THEY HUNG UP]")
  endcard()
#fpoint stands for friendship_points
f_point = 0

def c1():
   end0()
   endcard()

def c2():
  slowprint("*CLICK*")
  slowprint("[THEY HUNG UP]")
  endcard()

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
flag2 = False

while flag == False:
  slowprint("[PLEASE INPUT YES OR NO]")
  start = input().upper()

  if start == "YES":
    slowprint("[GOOD CHOICE]")
    while flag2 == False:
      slowprint("[WHAT IS YOUR NAME, PLAYER?]")
      name = input().capitalize()
      if not name:
        flag2 = False
      else:
        flag2 = True
        slowprint("")
        #ends the loop
        flag = True
      

        slowprint("[A CALL IS COMING THROUGH]")
        slowprint("[YOU ANSWER IT]")
        print("*CLICK*")
        print(" ")
        slowprint("[NOW YOU HAVE A CHOICE]")
        slowprint("[INPUT THE CORRESPONDING LETTER]")
        print(" ")
        slowprint("A: CASUAL")
        slowprint("B: POLITE")
        slowprint("C: STAY SILENT")
        print(" ")
        inpt0 = input("").upper()


        if inpt0 == "A":
          f_point += 1

          pronoun()
          slowprint('"Heya, thank you for reaching out, my name is ' + name + '"')
          pronoun()
          slowprint('"What\'s up?"')
          pronoun1()
          slowprint('"H-Hello, is this the right hotline?"')

          slowprint("[NOW SOME PRESSURE IS APPLIED]")
          slowprint("[YOU ARE NOW BEING TIMED]")
          slowprint("[JUST LIKE IN REAL LIFE, YOU DON'T KNOW HOW MUCH TIME YOU HAVE]")
          print(" ")
          slowprint("A: POLITE")
          slowprint("B: FRIENDLY")
          slowprint("C: PROFESSIONAL")
          t1 = Timer(10, c1)
          t1.start()
          print(" ")

          reply = input(" ").upper()
          print(" ")

          if reply == "A":
            t1.cancel()
            pronoun()
            slowprint('"I believe so, yes"')
            pronoun1()
            slowprint('"Oh"')
            avgprint("[THEIR VOICE IS SHAKING]")
            avgprint("[THEY'RE BREATHING IS PICKING UP]")
            avgprint("[THEY'RE ABOUT TO HANG UP]")
            print(" ")

            fastprint("A: QUICK")
            fastprint("B: KIND")
            print(" ")
            t2 = Timer(3,c2)
            t2.start()

            inpt1 = input(" ").upper()
            print(" ")
            
            if inpt1 == "A":
              t2.cancel()
              pronoun()
              fastprint('"So what\'d you call for?"')
              f_point =- 1
              pronoun1()
              slowprint('"I don\'t know"')
              print(" ")
              slowprint("A: QUESTIONING")
              slowprint("B: HELPING")
              slowprint("C: UNDERSTANDING")
              print(" ")

              t3 = Timer(5,c3)
              t3.start()

              inpt2 = input(" ").upper()

              print(" ")
              if inpt2 == "A":
                t3.cancel()
                pronoun()
                slowprint('"Really? There must\'ve been a reason"')
                pronoun1()
                slowprint('"I-I just, I don\'t-"')
                slowprint("A: PUSH")
                slowprint("B: APOLOGISE")
        

            elif inpt1 == "B":
              t2.cancel()
            
            else:
              pronoun()
              slowprint('"YOU SAY NOTHING"')
              t2.cancel()
              pronoun()
              endcard()


            

          elif reply == "B":
            t1.cancel()
            pronoun()
            slowprint('"I sure hope so, or I\'m in the wrong building again"')
            f_point += 1

          elif reply == "C":
            t1.cancel()
            pronoun()
            slowprint('"Yes, do you need help?"')
            f_points =- 1

          else:
            t1.cancel()
            end0()
            endcard()

          

        elif inpt0 == "B":
          pronoun()
          slowprint("“Thank you for reaching out, how may I help you?”")
          f_point += 1
          pronoun1()
          slowprint('"H-Hello, is this the right hotline?"')

          slowprint("[NOW SOME PRESSURE IS APPLIED]")
          slowprint("[YOU ARE NOW BEING TIMED]")
          slowprint("[JUST LIKE IN REAL LIFE, YOU DON'T KNOW HOW MUCH TIME YOU HAVE]")
          slowprint("A: POLITE")
          slowprint("B: FRIENDLY")
          slowprint("C: PROFESSIONAL")
          t1 = Timer(10, c1)
          t1.start()

          reply = input(" ").upper()

          if reply == "A":
            t1.cancel()
            pronoun()
            slowprint('"I believe so, yes"')

          elif reply == "B":
            t1.cancel()
            pronoun()
            slowprint('"I sure hope so, or I\'m in the wrong building again"')
            f_point += 1

          elif reply == "C":
            t1.cancel()
            pronoun()
            slowprint('"Yes, do you need help?"')
            f_points =- 1

          else:
            t1.cancel()
            end0()
            endcard()


        else:
          end0()
          endcard()

    
  elif start == "NO":
    flag = True

  else:
    flag = False
    

