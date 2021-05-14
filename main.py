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
  slowerprint("[SUICIDE AFFECTS EVERYONE INVOLVED]".center(100))
  slowerprint("[IF YOU OR SOMEONE YOU KNOW IS STRUGGLING, PLEASE SEEK HELP]".center(100))

def endcard1():
  slowerprint("[YOU LOST]".center(100))
  slowerprint("[BUT IT'S A GOOD THING THAT THIS WAS JUST A GAME]".center(100))
  slowerprint("[CAN YOU IMAGINE THE WEIGHT ON YOUR SHOULDERS, IF THIS WAS REAL?]".center(100))
  slowerprint("[BECAUSE FOR SOME PEOPLE IT IS]".center(100))
  slowerprint("[IN AN AUSTRALIAN STUDY, 135 MENTAL HEALTH WORKERS WERE SURVEYED]".center(100))
  slowerprint("[70.4% OF THEM SAID THAT THEY HAD EXPERIENCED A CLIENT SUICIDE SOMETIME IN THEIR CAREER]".center(93))
  slowerprint("[SUICIDE AFFECTS EVERYONE INVOLVED]".center(100))
  slowerprint("[IF YOU OR SOMEONE YOU KNOW IS STRUGGLING, PLEASE SEEK HELP]".center(100))

def endcard2():
  slowerprint("[GAME OVER]".center(100))
  slowerprint("[YOU TRIED YOUR BEST]".center(100))
  slowerprint("[BUT YOU CAN'T SAVE EVERYONE]".center(100))
  slowerprint("[MEDICAL PROFFESIONALS, FIREFIGHTERS, AND HELPLINE WORKERS]".center(100))
  slowerprint("[LIKE THE ONE YOU JUST PLAYED AS, KNOW THIS FAR TOO WELL]".center(100))
  slowerprint("[IN AN AUSTRALIAN STUDY, 135 MENTAL HEALTH WORKERS WERE SURVEYED]".center(100))
  slowerprint("[70.4% OF THEM SAID THAT THEY HAD EXPERIENCED A CLIENT SUICIDE SOMETIME IN THEIR CAREER]".center(93))
  slowerprint("[SUICIDE AFFECTS EVERYONE INVOLVED]".center(100))
  slowerprint("[IF YOU OR SOMEONE YOU KNOW IS STRUGGLING, PLEASE SEEK HELP]".center(100))

def endcard3():
  slowerprint("[WELL THAT WAS RUDE]".center(100))
  slowerprint("[WHY THE HELL WOULD YOU SAY THAT?]".center(100))
  slowerprint("[THAT KIDS GONNA DIE, AND IT'S YOUR FAULT]".center(100))
  slowerprint("[CAN YOU IMAGINE THE WEIGHT ON YOUR SHOULDERS, IF THIS WAS REAL?]".center(100))
  slowerprint("[BECAUSE FOR SOME PEOPLE IT IS, THOUGH THEY ARE A LOT NICER ABOUT IT]".center(100))
  slowerprint("[IN AN AUSTRALIAN STUDY, 135 MENTAL HEALTH WORKERS WERE SURVEYED]".center(100))
  slowerprint("[70.4% OF THEM SAID THAT THEY HAD EXPERIENCED A CLIENT SUICIDE SOMETIME IN THEIR CAREER]".center(93))
  slowerprint("[SUICIDE AFFECTS EVERYONE INVOLVED]".center(100))
  slowerprint("[IF YOU OR SOMEONE YOU KNOW IS STRUGGLING, PLEASE SEEK HELP]".center(100))


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
  print("*CLICK*")
  slowprint("[THEY HUNG UP]")
  endcard()

def c4():
  pronoun1()
  slowprint('"I don- I\'m sorry"')
  print("*CLICK*")
  slowprint("[THEY HUNG UP]")
  endcard()

def c5():
  slowprint("[YOU SAY NOTHING]")
  pronoun1()
  slowerprint('"I\'v alr-dy done it anyw-y"')
  pronoun1()
  slowerprint('"th-nk you f\'r your tim- "')
  slowprint("[YOU HEAR A LITTLE BIT OF MUFFLED SHUFFLING]")
  slowerprint("...")
  c2()

def c6():
  slowprint("[YOU SAY NOTHING]")
  pronoun1()
  slowprint('"\'m s-rry"')
  slowprint("[THERE'S FUMBLING ON THE OTHER SIDE OF THE LINE, BUT THEY DO NOT HANG UP]")
  slowerprint("......")
  slowprint("[YOU HEAR A *THUMP*]")
  slowprint("[THERE IS NO MORE SOUND] ")
  slowprint("[YOU STAY ON THE LINE FOR A FEW MORE MINUTES]")
  slowerprint("......")
  slowprint("[THERE'S ANOTHER CALL COMING THROUGH]")
  slowprint("*Click*")
  slowprint("[YOU'VE HUNG UP]")
  endcard1()

def c7():
  slowprint("[YOU SAY NOTHING]")
  print("*CLICK*")
  slowprint("[THEY HUNG UP]")
  endcard()

def c8():
  slowprint("[YOU SAY NOTHING]")
  slowprint("[THERE IS NO SOUND ON THE OTHER SIDE OF THE LINE]")
  slowprint("[THEY DON'T HANG UP, EITHER]")
  slowerprint("......")
  slowerprint(".........")
  slowprint("*Beep*")
  slowprint("[ANOTHER CALL IS COMING THROUGH]")
  slowprint("[YOU HANG UP]")
  endcard1()

def c9():
  slowprint("[YOU SAY NOTHING]")
  pronoun1()
  slowerprint('"th-nk you f\'r your tim- "')
  slowprint("[YOU HEAR A LITTLE BIT OF MUFFLED SHUFFLING]")
  slowerprint("...")
  slowprint("*Click*")
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
          slowprint("B: FRIENDLY // not done")
          slowprint("C: PROFESSIONAL // not done")
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
            avgprint("[THEIR BREATHING IS PICKING UP]")
            avgprint("[THEY'RE ABOUT TO HANG UP]")
            print(" ")

            fastprint("A: QUICK")
            fastprint("B: KIND // not done")
            print(" ")
            t2 = Timer(3,c2)
            t2.start()

            inpt1 = input(" ").upper()
            print(" ")
            
            if inpt1 == "A":
              t2.cancel()
              pronoun()
              slowprint('"So what\'d you call for?"')
              f_point =- 1
              pronoun1()
              slowprint('"I don\'t know"')
              print(" ")
              slowprint("A: QUESTIONING")
              slowprint("B: HELPING // not done")
              slowprint("C: UNDERSTANDING // not done")
              print(" ")

              t3 = Timer(5,c3)
              t3.start()

              inpt2 = input(" ").upper()

              print(" ")
              if inpt2 == "A":
                t3.cancel()
                f_point -= 2
                pronoun()
                slowprint('"Really? There must\'ve been a reason"')
                pronoun1()
                slowprint('"I-I just, I don\'t-"')
                print(" ")
                slowprint("A: PUSH")
                slowprint("B: APOLOGISE")

                t4 = Timer(3,c4)
                t4.start()
                print(" ")
                inpt3 = input(" ").upper()
                print(" ")

                if inpt3 == "A":
                  t4.cancel()
                  pronoun()
                  slowprint('"C\'mon, there has to be a reason"')
                  pronoun()
                  slowprint('"I can\'t help you unless I know what the problem is"')
                  pronoun1()
                  slowprint('"N-no, I-It\'s too late for you to help m-me, any-anyways"')
                  pronoun1()
                  slowprint('"I-I\'m sorry for the incon-inconvenience"')

                  c2()

                elif inpt3 == "B":
                  t4.cancel()
                  f_point += 1
                  pronoun()
                  slowprint('"I\'m sorry for pushing, I didn\'t mean to stress you out"')
                  pronoun1()
                  slowprint('"N-no, I over- overre -reaacted"')
                  slowprint("[YOU HEAR A SHAKEY EXHALE DOWN THE LINE]")
                  pronoun1()
                  slowprint('"I reco-recommended thi-this helpline to-to a friend a wh-while ba-ck"')
                  pronoun1()
                  slowprint('"It, did\'nt help hi-him, though, s-so I don\'t know why I expect m-me to be diff-iferent"')
                  print(" ")

                  slowprint("A: COLD // not done")
                  slowprint("B: WARM")
                  t5 = Timer(3, c3)
                  t5.start()
                  print(" ")
                  inpt4 = input(" ").upper()
                  print(" ")
                  
                  if inpt4 == "A":
                    t5.cancel()
                    f_point =- 1
                    pronoun()
                    slowprint('"Yeah, I don\'t know why, either"')
                    pronoun()
                    slowprint('"Is your friend why you\'re here, then?"')
                    pronoun1()
                    slowprint('"N- he\'s - he-"')
                    pronoun('"Dead? Yeah, I got that"')
                    slowprint("[YOU HEAR A SNIFFLE]")
                    pronoun1()
                    slowprint('"I d\'nt know why I-I bothered"')
                    slowprint("[THEIR VOICE IS SLURRED]")
                    slowprint("[IS IT FROM CRYING OR...]")
                    slowprint("[YOU FEEL AS THOUGH SOMETHING IS VERY WRONG HERE]")


                  
                  elif inpt4 == "B":
                    t5.cancel()
                    f_point =+ 1
                    pronoun()
                    slowprint('"Well, I, for one, am glad that you decided to call"')
                    pronoun()
                    slowprint('"It was very brave of you"')
                    pronoun1()
                    slowprint("......")
                    slowprint("[A HICCUP COMES FROM THE RECIEVER]")
                    pronoun1()
                    slowerprint('"I-I\'m not brave"')
                    pronoun1()
                    slowerprint('"I\'m a coward"')
                    slowprint("[THEIR VOICE SOUNDS SLURRED]")
                    slowprint("[YOU FEEL AS THOUGH SOMETHING ISN'T QUITE RIGHT HERE]")
                    pronoun1()
                    slowerprint('"I don\'t \'ow why I both-rd"')
                    slowprint("[IT'S BECOMING MORE DIFFICULT TO HEAR THEM]")

                    print(' ')
                    slowprint("A: URGENT")
                    slowprint("B: GENTLE")
                    print(' ')

                    t6 = Timer(5,c5)
                    t6.start()
                    inpt5 = input(" ").upper()

                    print(" ")
                    if inpt5 == "A":
                      t6.cancel()
                      pronoun()
                      avgprint('"What do you mean by that?"')
#---------------------------point split-------------------------------------
                      if f_point >= 5:
                        pronoun1()
                        slowerprint('"I\'ve alr\'dy d-ne i\'"')
                        slowprint("[IT IS GETTING INCREASINGLY DIFFICULT TO UNDERSTAND THEM]")
                        print(" ")
                        slowprint("A: PANIC")
                        slowprint("B: CALM")
                        print(" ")
                        inpt6 = input(" ").upper()
                        print(" ")

                        t7 = Timer(5,c6)
                        t7.start()

                        if inpt6 == "A":
                          t7.cancel()
                          pronoun()
                          avgprint('"What? What did you do?"')
                          pronoun1()
                          slowerprint('"\'m s-rry, I d\'n w-na w-rry any\'un"')
                          pronoun1()
                          slowerprint('"M\'by- sh\'d go"')

                          print(" ")
                          slowprint("A: INTERVENE")
                          print(" ")

                          inpt7 = input(" ").upper()
                          
                          t8 = Timer(3,c7)
                          t8.start()
                          print(" ")
                          if inpt7 == "A":
                            t8.cancel()
                            pronoun()
                            avgprint('"Wai-"')
                            c2()
                          else:
                            t8.join()


                        elif inpt6 == "B":
                          t7.cancel()
                          pronoun()
                          slowprint('"Okay, can you tell me what\'s wrong?"')
                          pronoun1()
                          slowerprint("a\'r-dy took the p\'lls, \'m die anyw\'y")

                          print(" ")
                          slowprint("A: WHAT?")
                          slowprint("B: WHERE?")
                          print(" ")

                          inpt8 = input(" ").upper()
                          print(" ")
                          if inpt8 == "A":
                            pronoun()
                            slowprint('"Okay, can you tell me what you took?"')
                            pronoun1()
                            slowerprint('"P\'rce\'mol"')
                            pronoun()
                            avgprint('"Okay, okay, paracetamol?"')
                            pronoun1()
                            slowerprint('"mhm"')

                            print(" ")
                            slowprint("A: WHY?")
                            slowprint("B: WHERE?")
                            print(" ")
                            
                            t9 = Timer(8,c8)
                            t9.start()
                            inpt9 = input(" ").upper()
                            print(" ")

                            if inpt9 == "A":
                              t9.cancel()
                              pronoun()
                              slowprint('"But... Why? What made you do this?"')
                              pronoun1()
                              slowprint('"Mh.. hur\'z."')
                              pronoun()
                              slowprint('"It hurts? Is that why you took them"')
                              pronoun1()
                              slowerprint('"..."')
                              pronoun()
                              slowprint('"Hey kid, stay awake, yeah?"')
                              pronoun1()
                              slowerprint('"..."')
                              slowprint("[THERE IS NO ANSWER]")
                              print(" ")
                              slowprint("A: WHERE?")
                              t10 = Timer(8, c8)
                              t10.start()
                              print(" ")
                              inpt10 = input(" ").upper()
                              print(" ")
                              if inpt10 == "A":
                                t10.cancel()
                                pronoun()
                                slowprint('"Can you tell me where you are?"')
                                pronoun1()
                                slowerprint('"..."')
                                pronoun()
                                slowprint('"Kid?"')
                                slowprint("[THERE IS NO ANSWER]")
                                print(" ")
                                slowprint("A: ?")
                                print(" ")
                                t11 = Timer(8, c8)
                                t11.start()
                                inpt11 = input(" ").upper()
                                print(" ")
                                if inpt11 == "A":
                                  t11.cancel()
                                  pronoun()
                                  slowprint('"Kid?"')
                                  pronoun1()
                                  slowerprint('"..."')
                                  print(" ")
                                  slowprint("A: ?")
                                  print()
                                  t12 = Timer(8,c8)
                                  t12.start()
                                  inpt12 = input(" ").upper()
                                  print(" ")
                                  if inpt12 == "A":
                                    t12.cancel()
                                    pronoun()
                                    slowerprint('"Are you still there? Can you tell me where you are?"')
                                    pronoun1()
                                    slowerprint('"..."')
                                    slowprint("[THERE IS NO ANSWER]")
                                    print(" ")
                                    slowprint("A: PANIC")
                                    slowprint("B: LISTEN")
                                    print(" ")
                                    t13 = Timer(8,c8)
                                    t13.start()
                                    inpt13 = input(" ").upper()
                                    print(" ")
                                    if inpt13 == "A":
                                      t13.cancel()
                                      slowprint("[YOU FEEL PANIC RISE IN YOUR CHEST]")
                                      pronoun()
                                      avgprint('"Hey? Kid! Kid, answer me!"')
                                      pronoun1()
                                      slowerprint('"......"')
                                      slowprint("[NOBODY ANSWERS]")
                                      endcard2()
                                    elif inpt13 == "B":
                                      t13.cancel()
                                      slowprint("[YOU HOLD YOUR BREATH AND LISTEN]")
                                      slowerprint('"..."')
                                      slowprint("[YOU DON'T HEAR ANYTHING FROM THE RECIEVER]")
                                      slowerprint('"...."')
                                      slowprint("[YOU LISTEN A LITTLE LONGER]")
                                      slowerprint('"....."')
                                      slowprint("[YOU HEAR NO BREATHING]")
                                      endcard2()
                                    else:
                                      t13.join()


                                  else:
                                    t12.join()
                                    
                          
                                else:
                                  t11.join()
                                  


                              else:
                                t10.join()


                            elif inpt9 == "B":
                              t9.cancel()
                              pronoun()
                              slowprint('"Can you tell me where you are right now?"')
                              pronoun1()
                              slowprint('"M\'m.. a\' \'ome"')
                              pronoun()
                              slowprint('"Can you tell me where that is?"')
                              slowprint("[THERE IS ONLY A INCOMPREHENSIBLE MUMBLE IN REPLY]")
                              pronoun()
                              slowprint('"Where do you live?"')
                              slowprint("[YOU DON'T HEAR ANOTHER MUMBLE]")
                              pronoun()
                              slowprint('"Try to stay awake. Help is on it\'s way"')
                              pronoun1()
                              slowerprint('"..."')
                              pronoun()
                              slowprint('"You still there?"')
                              slowprint("[THERE IS NO REPLY]")
                              print(" ")
                              slowprint("A: WHY?")
                              print(" ")

                              t14 = Timer(8,c8)
                              t14.start()
                              inpt14 = input(" ").upper()
                              print(" ")
                              if inpt14 == "A":
                                t14.cancel()
                                pronoun()
                                slowprint('"Why would you do this? You\'re so young"')
                                pronoun1()
                                slowerprint('"..."')
                                pronoun()
                                slowprint('"Kid?"')
                                slowprint("[THERE IS NO ANSWER]")
                                print(" ")
                                slowprint("A: ?")
                                print(" ")
                                t15 = Timer(8, c8)
                                t15.start()
                                inpt15 = input(" ").upper()
                                print(" ")
                                if inpt15 == "A":
                                  t15.cancel()
                                  pronoun()
                                  slowprint('"Kid?"')
                                  pronoun1()
                                  slowerprint('"..."')
                                  print(" ")
                                  slowprint("A: ?")
                                  print()
                                  t16 = Timer(8,c8)
                                  t16.start()
                                  inpt12 = input(" ").upper()
                                  print(" ")
                                  if inpt12 == "A":
                                    t16.cancel()
                                    pronoun()
                                    slowerprint('"Are you still there? Can you tell me where you are?"')
                                    pronoun1()
                                    slowerprint("...")
                                    slowprint("[THERE IS NO ANSWER]")
                                    print(" ")
                                    slowprint("A: PANIC")
                                    slowprint("B: LISTEN")
                                    print(" ")
                                    t17 = Timer(8,c8)
                                    t17.start()
                                    inpt13 = input(" ").upper()
                                    print(" ")
                                    if inpt13 == "A":
                                      t17.cancel()
                                      slowprint("[YOU FEEL PANIC RISE IN YOUR CHEST]")
                                      pronoun()
                                      avgprint('"Hey? Kid! Kid, answer me!"')
                                      pronoun1()
                                      slowerprint('"......"')
                                      slowprint("[NOBODY ANSWERS]")
                                      endcard2()
                                    elif inpt13 == "B":
                                      t17.cancel()
                                      slowprint("[YOU HOLD YOUR BREATH AND LISTEN]")
                                      slowerprint("...")
                                      slowprint("[YOU DON'T HEAR ANYTHING FROM THE RECIEVER]")
                                      slowerprint("....")
                                      slowprint("[YOU LISTEN A LITTLE LONGER]")
                                      slowerprint(".....")
                                      slowprint("[YOU HEAR NO BREATHING]")
                                      endcard2()
                                    else:
                                      t17.join()


                                  else:
                                    t16.join()
                                    
                          
                                else:
                                  t15.join()
                                  


                              else:
                                t14.join()


                              
                            
                            else:
                              t9.join()

                          elif inpt8 == "B":
                            print(" ")
                            pronoun()
                            slowprint('"Can you tell me where you are right now?"')
                            pronoun1()
                            slowprint('"D\'n\'t... w\'nna die"')
                            pronoun()
                            slowprint('"You want to die?"')
                            pronoun1()
                            slowprint('"Mhm"')
                            pronoun()
                            slowprint('"You must\'ve called for a reason, though"')
                            pronoun()
                            slowprint('"Can you tell me where you are right now?"')
                            print(" ")
                            slowprint("A: WHY?")
                            slowprint("B: WHAT?")
                            print(" ")
                            
                            t18 = Timer(8,c8)
                            t18.start()
                            inpt18 = input(" ").upper()
                            print(" ")

                            if inpt9 == "A":
                              t18.cancel()
                              pronoun()
                              slowprint('"But... Why? What made you do this?"')
                              pronoun1()
                              slowprint('"Mh.. hur\'z."')
                              pronoun()
                              slowprint('"Hey kid, stay awake, yeah?"')
                              pronoun1()
                              slowerprint('"..."')
                              slowprint("[THERE IS NO ANSWER]")
                              print(" ")
                              slowprint("A: WHAT?")
                              t19 = Timer(8, c8)
                              t19.start()
                              print(" ")
                              inpt19 = input(" ").upper()
                              print(" ")
                              if inpt19 == "A":
                                t19.cancel()
                                pronoun()
                                slowprint('"Can you tell me what you took?"')
                                pronoun1()
                                slowerprint('"..."')
                                pronoun()
                                slowprint('"Kid?"')
                                slowprint("[THERE IS NO ANSWER]")
                                print(" ")
                                slowprint("A: ?")
                                print(" ")
                                t11 = Timer(8, c8)
                                t11.start()
                                inpt11 = input(" ").upper()
                                print(" ")
                                if inpt11 == "A":
                                  t11.cancel()
                                  pronoun()
                                  slowprint('"Kid?"')
                                  pronoun1()
                                  slowerprint('"..."')
                                  print(" ")
                                  slowprint("A: ?")
                                  print()
                                  t12 = Timer(8,c8)
                                  t12.start()
                                  inpt12 = input(" ").upper()
                                  print(" ")
                                  if inpt12 == "A":
                                    t12.cancel()
                                    pronoun()
                                    slowerprint('"Are you still there? What pills did you take?"')
                                    pronoun1()
                                    slowerprint("...")
                                    slowprint("[THERE IS NO ANSWER]")
                                    print(" ")
                                    slowprint("A: PANIC")
                                    slowprint("B: LISTEN")
                                    print(" ")
                                    t13 = Timer(8,c8)
                                    t13.start()
                                    inpt13 = input(" ").upper()
                                    print(" ")
                                    if inpt13 == "A":
                                      t13.cancel()
                                      slowprint("[YOU FEEL PANIC RISE IN YOUR CHEST]")
                                      pronoun()
                                      avgprint('"Hey? Kid! Kid, answer me!"')
                                      pronoun1()
                                      slowerprint('"......"')
                                      slowprint("[NOBODY ANSWERS]")
                                      endcard2()
                                    elif inpt13 == "B":
                                      t13.cancel()
                                      slowprint("[YOU HOLD YOUR BREATH AND LISTEN]")
                                      slowerprint("...")
                                      slowprint("[YOU DON'T HEAR ANYTHING FROM THE RECIEVER]")
                                      slowerprint("....")
                                      slowprint("[YOU LISTEN A LITTLE LONGER]")
                                      slowerprint(".....")
                                      slowprint("[YOU HEAR NO BREATHING]")
                                      endcard2()
                                    else:
                                      t13.join()


                                  else:
                                    t12.join()
                                    
                          
                                else:
                                  t11.join()
                                  


                              else:
                                t10.join()


                            elif inpt9 == "B":
                              t18.cancel()
                              pronoun()
                              slowprint('"You said you took something?"')
                              pronoun1()
                              slowprint('"Mhm"')
                              pronoun()
                              slowprint('"What did you take?"')
                              slowprint("[THERE IS ONLY A INCOMPREHENSIBLE MUMBLE IN REPLY]")
                              pronoun()
                              slowprint('"Can you tell me what you took?"')
                              slowprint("[YOU DON'T HEAR ANOTHER MUMBLE]")
                              pronoun()
                              slowprint('"Hey, stay awake"')
                              pronoun1()
                              slowerprint('"..."')
                              pronoun()
                              slowprint('"Hello?"')
                              slowprint("[THERE IS NO REPLY]")
                              print(" ")
                              slowprint("A: WHY?")
                              print(" ")

                              t14 = Timer(8,c8)
                              t14.start()
                              inpt14 = input(" ").upper()
                              print(" ")
                              if inpt14 == "A":
                                t14.cancel()
                                pronoun()
                                slowprint('"Why would you do this? You\'re so young"')
                                pronoun1()
                                slowerprint('"..."')
                                pronoun()
                                slowprint('"Kid?"')
                                slowprint("[THERE IS NO ANSWER]")
                                print(" ")
                                slowprint("A: ?")
                                print(" ")
                                t15 = Timer(8, c8)
                                t15.start()
                                inpt15 = input(" ").upper()
                                print(" ")
                                if inpt15 == "A":
                                  t15.cancel()
                                  pronoun()
                                  slowprint('"Kid?"')
                                  pronoun1()
                                  slowerprint('"..."')
                                  print(" ")
                                  slowprint("A: ?")
                                  print()
                                  t16 = Timer(8,c8)
                                  t16.start()
                                  inpt12 = input(" ").upper()
                                  print(" ")
                                  if inpt12 == "A":
                                    t16.cancel()
                                    pronoun()
                                    slowerprint('"Are you there? Please answer"')
                                    pronoun1()
                                    slowerprint("...")
                                    slowprint("[THERE IS NO ANSWER]")
                                    print(" ")
                                    slowprint("A: PANIC")
                                    slowprint("B: LISTEN")
                                    print(" ")
                                    t17 = Timer(8,c8)
                                    t17.start()
                                    inpt13 = input(" ").upper()
                                    print(" ")
                                    if inpt13 == "A":
                                      t17.cancel()
                                      slowprint("[YOU FEEL PANIC RISE IN YOUR CHEST]")
                                      pronoun()
                                      avgprint('"Hey? Kid! Kid, answer me!"')
                                      pronoun1()
                                      slowerprint('"......"')
                                      slowprint("[NOBODY ANSWERS]")
                                      endcard2()
                                    elif inpt13 == "B":
                                      t17.cancel()
                                      slowprint("[YOU HOLD YOUR BREATH AND LISTEN]")
                                      slowerprint("...")
                                      slowprint("[YOU DON'T HEAR ANYTHING FROM THE RECIEVER]")
                                      slowerprint("....")
                                      slowprint("[YOU LISTEN A LITTLE LONGER]")
                                      slowerprint(".....")
                                      slowprint("[YOU HEAR NO BREATHING]")
                                      endcard2()
                                    else:
                                      t17.join()


                                  else:
                                    t16.join()
                                else:
                                  t15.join()
                                  


                              else:
                                t14.join()


                              
                            
                            else:
                              t18.join()

                          else:
                            print(" ")





                            


                        else:
                          t7.join()

                      else:
                        pronoun1()
                        slowprint('"I\'v alr-dy d\'n it, too la\'e"')
                        pronoun1()
                        slowprint('"Maybe s\'m part of me wan\'ed to live"')
                        pronoun1()
                        slowprint('"Bu\' this \'s proba-ly f\'r the best"')
                        print(" ")
                        slowprint("A: WHAT?")
                        slowprint("B: WHY?")
                        slowprint("C: WHERE?")
                        print(" ")
                        t3w = Timer(8,c9)
                        t3w.start()
                        inpt3w = input(" ").upper()
                        print(" ")
                        if inpt3w == "A":
                          t3w.cancel()
                          pronoun()
                          slowprint('"What? What\'d you do?"')
                          pronoun1()
                          slowprint('"jus\' some meds"')
                          pronoun()
                          slowprint('"What meds? How much did you take?"')
                          pronoun1()
                          slowprint('"eno\'gh"')
                          print(" ")
                          slowprint("A: WHERE?")
                          slowprint("B: WHY?")
                          print(" ")
                          t2w = Timer(6, c9)
                          t2w.start()
                          inpt2w = input(" ").upper()
                          print(" ")
                          if inpt2w == "A":
                            t2w.cancel()
                            pronoun()
                            slowprint('"Where are you?"')
                            pronoun1()
                            slowprint('"Doe\'nt matt\'r"')
                            print(" ")
                            avgprint("A: SOFT")
                            avgprint("B: HARSH")
                            print(" ")
                            tsh = Timer(3, c9)
                            tsh.start()
                            inptsh = input(" ").upper()
                            print(" ")
                            if inptsh == "A":
                              tsh.cancel()
                              pronoun()
                              slowprint('"Of course it matters"')
                              pronoun()
                              slowprint('"You matter"')
                              pronoun1()
                              slowprint('"......"')
                              pronoun1()
                              slowprint('"Th-nk you, f\'r listning an\' caring, ev\'n a li-le"')
                              pronoun1()
                              slowerprint('"..."')
                              pronoun()
                              slowprint('"Kid-"')
                              print("*Click*")
                              endcard()

                            elif inptsh == "B":
                              tsh.cancel()
                              pronoun()
                              slowprint('"Yes, it matters"')
                              pronoun()
                              slowprint('"I get paid to help you, not sit here helplessly as you, what? kill yourself?"')
                              slowprint("[YOU HEAR A SHARP BREATH]")
                              slowprint("[YOU SEE YOUR COWORKER GIVING YOU A LOOK FROM THE CORNER OF YOUR EYE]")
                              pronoun1()
                              slowprint('"\'m s-rry"')
                              print("*Click*")
                              endcard3()

                            else:
                              tsh.join()

                          
                          elif inpt2w == "B":
                            t2w.cancel()
                            pronoun()
                            slowprint('"That\'s - that\'s, why would you-"')
                            pronoun1()
                            slowprint('"T\' make the pain go \'way"')
                            print(" ")
                            slowprint("A: WHERE?")
                            print(" ")
                            tw = Timer(5, c9)
                            tw.start()
                            inptw = input(" ").upper()
                            if inptw == "A":
                              tw.cancel()
                              pronoun()
                              slowprint('"Where are you right now?"')
                              pronoun1()
                              slowprint('"I g-t t\' go"')
                              print(" ")
                              avgprint("A: INTERVENE")
                              print(" ")
                              ti = Timer(3, c2)
                              ti.start()
                              inpti = input(" ").upper()
                              print(" ")
                              if inpti == "A":
                                ti.cancel()
                                avgprint('"Wait- please don\'t g- "')
                                c2()
                              else:
                                ti.join()
                            else:
                              tw.join()

                          else:
                            t2w.join()





                        elif inpt3w == "B":
                          t3w.cancel()
                          pronoun()
                          slowprint("Why, why did you call if you think that?")
                          pronoun1()
                          slowprint('"I don- \'ow"')
                          pronoun()
                          slowprint('"Part of you want\'s to live, righ? That\'s what you said"')
                          pronoun1()
                          slowprint('"Jus\' want s-mone t\' care"')
                          print(" ")
                          slowprint("A: WHERE?")
                          slowprint("B: FAMILY?")
                          print(" ")
                          t2w = Timer(6, c9)
                          t2w.start()
                          inpt2w = input(" ").upper()
                          print(" ")
                          if inpt2w == "A":
                            t2w.cancel()
                            pronoun()
                            slowprint('"Are you at home right now?"')
                            pronoun1()
                            slowprint('"uh huh"')
                            print(" ")
                            avgprint("A: WHAT?")
                            avgprint("B: WHERE?")
                            print(" ")
                            tsh = Timer(8, c9)
                            tsh.start()
                            inptsh = input(" ").upper()
                            print(" ")
                            if inptsh == "A":
                              tsh.cancel()
                              pronoun()
                              slowprint('"What did you do? You said you did something?"')
                              pronoun()
                              slowprint('"Pills of some kind?"')
                              pronoun1()
                              slowprint('"mhm"')
                              pronoun1()
                              slowprint('"St\'ps the pain"')
                              pronoun()
                              slowprint('"Okay, I need to know what kind so I can help you"')
                              pronoun1()
                              slowprint('"I don\' wan\' -elp"')
                              slowprint("[YOU HEAR THEM FUMBLING WITH THE PHONE]")
                              pronoun()
                              avgprint('"Wai-"')
                              print("*Click*")
                              endcard()

                            elif inptsh == "B":
                              tsh.cancel()
                              pronoun()
                              slowprint('"Where is your home?"')
                              
                              pronoun()
                              slowprint('"What about your family? Friends?"')
                              pronoun1()
                              slowprint('"Don\' -ave any frien\'s"')
                              pronoun1()
                              slowprint('"M\' fam-ly don\' care "')
                              slowprint("[YOU HEAR A SHARP BREATH]")
                              pronoun1()
                              slowprint('"an- neith\'r do you"')
                              pronoun()
                              avgprint('"Wait, I ca-"')
                              print("*Click*")
                              endcard()

                            else:
                              tsh.join()

                          
                          elif inpt2w == "B":
                            t2w.cancel()
                            pronoun()
                            slowprint('"What about your family? Friends?"')
                            pronoun1()
                            slowprint('"Don\' -ave any frien\'s"')
                            pronoun1()
                            slowprint('"M\' fam-ly don\' care "')
                            slowprint("[YOU HEAR A SHARP BREATH]")
                            pronoun1()
                            slowprint('"an- neith\'r do you"')
                            pronoun()
                            avgprint('"Wait, I ca-"')
                            print("*Click*")
                            endcard()
                        

                          else:
                            t2w.join()
                        elif inpt3w == "C":
                          t3w.cancel()

                          if inpt3w == "C":
                            pronoun()
                            slowprint('"Where are you right now?"')
                            pronoun1()
                            slowprint('"\'om"')
                            pronoun()
                            slowprint('"You\'re at home?"')
                            pronoun1()
                            slowprint('"mhm"')
                            pronoun()
                            slowprint('"Okay, stay awake for me"')
                            print(" ")
                            slowprint("A: HOME?")
                            slowprint("B: FAMILY?")
                            print(" ")
                            t2w = Timer(6, c9)
                            t2w.start()
                            inpt2w = input(" ").upper()
                            print(" ")
                            if inpt2w == "A":
                              t2w.cancel()
                              pronoun()
                              slowprint('"Where\'s your home?"')
                              pronoun1()
                              slowprint('"Doe\'nt matt\'r"')
                              print(" ")
                              avgprint("A: SOFT")
                              avgprint("B: HARSH")
                              print(" ")
                              tsh = Timer(3, c9)
                              tsh.start()
                              inptsh = input(" ").upper()
                              print(" ")
                              if inptsh == "A":
                                tsh.cancel()
                                pronoun()
                                slowprint('"Of course it matters"')
                                pronoun()
                                slowprint('"I can\'t help you if you I don\'t know where you are"')
                                pronoun()
                                slowprint('"Please, kid, let me help you"')
                                pronoun1()
                                slowprint('"......"')
                                pronoun1()
                                slowprint('"Th-nk you, f\'r listning an\' caring, ev\'n a li-le"')
                                pronoun1()
                                slowprint('"..."')
                                pronoun()
                                slowprint('"Kid-"')
                                print("*Click*")
                                endcard()

                              elif inptsh == "B":
                                tsh.cancel()
                                pronoun()
                                slowprint('"Yes, it matters"')
                                pronoun()
                                slowprint('"I get paid to help you, not sit here helplessly as you, what? kill yourself?"')
                                slowprint("[YOU HEAR A SHARP BREATH]")
                                slowprint("[YOU SEE YOUR COWORKER GIVING YOU A LOOK FROM THE CORNER OF YOUR EYE]")
                                pronoun1()
                                slowprint('"\'m s-rry"')
                                print("*Click*")
                                endcard3()

                              else:
                                tsh.join()

                            
                            elif inpt2w == "B":
                              t2w.cancel()
                              pronoun()
                              slowprint('"Do you have someone who can help nearby? Family? Friends?"')
                              pronoun1()
                              slowprint('"No"')
                              print(" ")
                              slowprint("A: HOME?")
                              print(" ")
                              tw = Timer(5, c9)
                              tw.start()  
                              inptw = input(" ").upper()
                              if inptw == "A":
                                tw.cancel()
                                pronoun()
                                slowprint('"Where is your house?"')
                                pronoun1()
                                slowprint('"n\' don\' wan- help"')
                                slowprint("[YOU HEAR THE CALLER MOVING TO HANG UP]")
                                slowprint("[THEY SOUND LIKE THEY'RE STRUGGLING]")
                                print(" ")
                                avgprint("A: INTERVENE")
                                print(" ")
                                ti = Timer(3, c2)
                                ti.start()
                                inpti = input(" ").upper()
                                print(" ")
                                if inpti == "A":
                                  ti.cancel()
                                  avgprint('"Wait- please don\'t g- "')
                                  c2()
                                else:
                                  ti.join()
                              else:
                                tw.join()

                            else:
                              t2w.join()

                        else:
                          t3w.join()





                    elif inpt5 == "B":
                      t5.cancel()
                      f_point += 1
                      pronoun()
                      slowprint('"Are you okay? What\s wrong?"')

                      if f_point >= 5:
                        pronoun1()
                        slowerprint('"I\'ve alr\'dy d-ne i\'"')
                        slowprint("[IT IS GETTING INCREASINGLY DIFFICULT TO UNDERSTAND THEM]")
                        print(" ")
                        slowprint("A: PANIC")
                        slowprint("B: CALM")
                        print(" ")
                        inpt6 = input(" ").upper()
                        print(" ")

                        t7 = Timer(5,c6)
                        t7.start()

                        if inpt6 == "A":
                          t7.cancel()
                          pronoun()
                          avgprint('"What? What did you do?"')
                          pronoun1()
                          slowerprint('"\'m s-rry, I d\'n w-na w-rry any\'un"')
                          pronoun1()
                          slowerprint('"M\'by- sh\'d go"')

                          print(" ")
                          slowprint("A: INTERVENE")
                          print(" ")

                          inpt7 = input(" ").upper()
                          
                          t8 = Timer(3,c7)
                          t8.start()
                          print(" ")
                          if inpt7 == "A":
                            t8.cancel()
                            pronoun()
                            avgprint('"Wai-"')
                            c2()
                          else:
                            t8.join()


                        elif inpt6 == "B":
                          t7.cancel()
                          pronoun()
                          slowprint('"Okay, can you tell me what\'s wrong?"')
                          pronoun1()
                          slowerprint("a\'r-dy took the p\'lls, \'m die anyw\'y")

                          print(" ")
                          slowprint("A: WHAT?")
                          slowprint("B: WHERE?")
                          print(" ")

                          inpt8 = input(" ").upper()
                          print(" ")
                          if inpt8 == "A":
                            pronoun()
                            slowprint('"Okay, can you tell me what you took?"')
                            pronoun1()
                            slowerprint('"P\'rce\'mol"')
                            pronoun()
                            avgprint('"Okay, okay, paracetamol?"')
                            pronoun1()
                            slowerprint('"mhm"')

                            print(" ")
                            slowprint("A: WHY?")
                            slowprint("B: WHERE?")
                            print(" ")
                            
                            t9 = Timer(8,c8)
                            t9.start()
                            inpt9 = input(" ").upper()
                            print(" ")

                            if inpt9 == "A":
                              t9.cancel()
                              pronoun()
                              slowprint('"But... Why? What made you do this?"')
                              pronoun1()
                              slowprint('"Mh.. hur\'z."')
                              pronoun()
                              slowprint('"It hurts? Is that why you took them"')
                              pronoun1()
                              slowerprint('"..."')
                              pronoun()
                              slowprint('"Hey kid, stay awake, yeah?"')
                              pronoun1()
                              slowerprint('"..."')
                              slowprint("[THERE IS NO ANSWER]")
                              print(" ")
                              slowprint("A: WHERE?")
                              t10 = Timer(8, c8)
                              t10.start()
                              print(" ")
                              inpt10 = input(" ").upper()
                              print(" ")
                              if inpt10 == "A":
                                t10.cancel()
                                pronoun()
                                slowprint('"Can you tell me where you are?"')
                                pronoun1()
                                slowerprint('"..."')
                                pronoun()
                                slowprint('"Kid?"')
                                slowprint("[THERE IS NO ANSWER]")
                                print(" ")
                                slowprint("A: ?")
                                print(" ")
                                t11 = Timer(8, c8)
                                t11.start()
                                inpt11 = input(" ").upper()
                                print(" ")
                                if inpt11 == "A":
                                  t11.cancel()
                                  pronoun()
                                  slowprint('"Kid?"')
                                  pronoun1()
                                  slowerprint('"..."')
                                  print(" ")
                                  slowprint("A: ?")
                                  print()
                                  t12 = Timer(8,c8)
                                  t12.start()
                                  inpt12 = input(" ").upper()
                                  print(" ")
                                  if inpt12 == "A":
                                    t12.cancel()
                                    pronoun()
                                    slowerprint('"Are you still there? Can you tell me where you are?"')
                                    pronoun1()
                                    slowerprint('"..."')
                                    slowprint("[THERE IS NO ANSWER]")
                                    print(" ")
                                    slowprint("A: PANIC")
                                    slowprint("B: LISTEN")
                                    print(" ")
                                    t13 = Timer(8,c8)
                                    t13.start()
                                    inpt13 = input(" ").upper()
                                    print(" ")
                                    if inpt13 == "A":
                                      t13.cancel()
                                      slowprint("[YOU FEEL PANIC RISE IN YOUR CHEST]")
                                      pronoun()
                                      avgprint('"Hey? Kid! Kid, answer me!"')
                                      pronoun1()
                                      slowerprint('"......"')
                                      slowprint("[NOBODY ANSWERS]")
                                      endcard2()
                                    elif inpt13 == "B":
                                      t13.cancel()
                                      slowprint("[YOU HOLD YOUR BREATH AND LISTEN]")
                                      slowerprint('"..."')
                                      slowprint("[YOU DON'T HEAR ANYTHING FROM THE RECIEVER]")
                                      slowerprint('"...."')
                                      slowprint("[YOU LISTEN A LITTLE LONGER]")
                                      slowerprint('"....."')
                                      slowprint("[YOU HEAR NO BREATHING]")
                                      endcard2()
                                    else:
                                      t13.join()


                                  else:
                                    t12.join()
                                    
                          
                                else:
                                  t11.join()
                                  


                              else:
                                t10.join()


                            elif inpt9 == "B":
                              t9.cancel()
                              pronoun()
                              slowprint('"Can you tell me where you are right now?"')
                              pronoun1()
                              slowprint('"M\'m.. a\' \'ome"')
                              pronoun()
                              slowprint('"Can you tell me where that is?"')
                              slowprint("[THERE IS ONLY A INCOMPREHENSIBLE MUMBLE IN REPLY]")
                              pronoun()
                              slowprint('"Where do you live?"')
                              slowprint("[YOU DON'T HEAR ANOTHER MUMBLE]")
                              pronoun()
                              slowprint('"Try to stay awake. Help is on it\'s way"')
                              pronoun1()
                              slowerprint('"..."')
                              pronoun()
                              slowprint('"You still there?"')
                              slowprint("[THERE IS NO REPLY]")
                              print(" ")
                              slowprint("A: WHY?")
                              print(" ")

                              t14 = Timer(8,c8)
                              t14.start()
                              inpt14 = input(" ").upper()
                              print(" ")
                              if inpt14 == "A":
                                t14.cancel()
                                pronoun()
                                slowprint('"Why would you do this? You\'re so young"')
                                pronoun1()
                                slowerprint('"..."')
                                pronoun()
                                slowprint('"Kid?"')
                                slowprint("[THERE IS NO ANSWER]")
                                print(" ")
                                slowprint("A: ?")
                                print(" ")
                                t15 = Timer(8, c8)
                                t15.start()
                                inpt15 = input(" ").upper()
                                print(" ")
                                if inpt15 == "A":
                                  t15.cancel()
                                  pronoun()
                                  slowprint('"Kid?"')
                                  pronoun1()
                                  slowerprint('"..."')
                                  print(" ")
                                  slowprint("A: ?")
                                  print()
                                  t16 = Timer(8,c8)
                                  t16.start()
                                  inpt12 = input(" ").upper()
                                  print(" ")
                                  if inpt12 == "A":
                                    t16.cancel()
                                    pronoun()
                                    slowerprint('"Are you still there? Can you tell me where you are?"')
                                    pronoun1()
                                    slowerprint("...")
                                    slowprint("[THERE IS NO ANSWER]")
                                    print(" ")
                                    slowprint("A: PANIC")
                                    slowprint("B: LISTEN")
                                    print(" ")
                                    t17 = Timer(8,c8)
                                    t17.start()
                                    inpt13 = input(" ").upper()
                                    print(" ")
                                    if inpt13 == "A":
                                      t17.cancel()
                                      slowprint("[YOU FEEL PANIC RISE IN YOUR CHEST]")
                                      pronoun()
                                      avgprint('"Hey? Kid! Kid, answer me!"')
                                      pronoun1()
                                      slowerprint('"......"')
                                      slowprint("[NOBODY ANSWERS]")
                                      endcard2()
                                    elif inpt13 == "B":
                                      t17.cancel()
                                      slowprint("[YOU HOLD YOUR BREATH AND LISTEN]")
                                      slowerprint("...")
                                      slowprint("[YOU DON'T HEAR ANYTHING FROM THE RECIEVER]")
                                      slowerprint("....")
                                      slowprint("[YOU LISTEN A LITTLE LONGER]")
                                      slowerprint(".....")
                                      slowprint("[YOU HEAR NO BREATHING]")
                                      endcard2()
                                    else:
                                      t17.join()


                                  else:
                                    t16.join()
                                    
                          
                                else:
                                  t15.join()
                                  


                              else:
                                t14.join()


                              
                            
                            else:
                              t9.join()

                          elif inpt8 == "B":
                            print(" ")
                            pronoun()
                            slowprint('"Can you tell me where you are right now?"')
                            pronoun1()
                            slowprint('"D\'n\'t... w\'nna die"')
                            pronoun()
                            slowprint('"You want to die?"')
                            pronoun1()
                            slowprint('"Mhm"')
                            pronoun()
                            slowprint('"You must\'ve called for a reason, though"')
                            pronoun()
                            slowprint('"Can you tell me where you are right now?"')
                            print(" ")
                            slowprint("A: WHY?")
                            slowprint("B: WHAT?")
                            print(" ")
                            
                            t18 = Timer(8,c8)
                            t18.start()
                            inpt18 = input(" ").upper()
                            print(" ")

                            if inpt9 == "A":
                              t18.cancel()
                              pronoun()
                              slowprint('"But... Why? What made you do this?"')
                              pronoun1()
                              slowprint('"Mh.. hur\'z."')
                              pronoun()
                              slowprint('"Hey kid, stay awake, yeah?"')
                              pronoun1()
                              slowerprint('"..."')
                              slowprint("[THERE IS NO ANSWER]")
                              print(" ")
                              slowprint("A: WHAT?")
                              t19 = Timer(8, c8)
                              t19.start()
                              print(" ")
                              inpt19 = input(" ").upper()
                              print(" ")
                              if inpt19 == "A":
                                t19.cancel()
                                pronoun()
                                slowprint('"Can you tell me what you took?"')
                                pronoun1()
                                slowerprint('"..."')
                                pronoun()
                                slowprint('"Kid?"')
                                slowprint("[THERE IS NO ANSWER]")
                                print(" ")
                                slowprint("A: ?")
                                print(" ")
                                t11 = Timer(8, c8)
                                t11.start()
                                inpt11 = input(" ").upper()
                                print(" ")
                                if inpt11 == "A":
                                  t11.cancel()
                                  pronoun()
                                  slowprint('"Kid?"')
                                  pronoun1()
                                  slowerprint('"..."')
                                  print(" ")
                                  slowprint("A: ?")
                                  print()
                                  t12 = Timer(8,c8)
                                  t12.start()
                                  inpt12 = input(" ").upper()
                                  print(" ")
                                  if inpt12 == "A":
                                    t12.cancel()
                                    pronoun()
                                    slowerprint('"Are you still there? What pills did you take?"')
                                    pronoun1()
                                    slowerprint("...")
                                    slowprint("[THERE IS NO ANSWER]")
                                    print(" ")
                                    slowprint("A: PANIC")
                                    slowprint("B: LISTEN")
                                    print(" ")
                                    t13 = Timer(8,c8)
                                    t13.start()
                                    inpt13 = input(" ").upper()
                                    print(" ")
                                    if inpt13 == "A":
                                      t13.cancel()
                                      slowprint("[YOU FEEL PANIC RISE IN YOUR CHEST]")
                                      pronoun()
                                      avgprint('"Hey? Kid! Kid, answer me!"')
                                      pronoun1()
                                      slowerprint('"......"')
                                      slowprint("[NOBODY ANSWERS]")
                                      endcard2()
                                    elif inpt13 == "B":
                                      t13.cancel()
                                      slowprint("[YOU HOLD YOUR BREATH AND LISTEN]")
                                      slowerprint("...")
                                      slowprint("[YOU DON'T HEAR ANYTHING FROM THE RECIEVER]")
                                      slowerprint("....")
                                      slowprint("[YOU LISTEN A LITTLE LONGER]")
                                      slowerprint(".....")
                                      slowprint("[YOU HEAR NO BREATHING]")
                                      endcard2()
                                    else:
                                      t13.join()


                                  else:
                                    t12.join()
                                    
                          
                                else:
                                  t11.join()
                                  


                              else:
                                t10.join()


                            elif inpt9 == "B":
                              t18.cancel()
                              pronoun()
                              slowprint('"You said you took something?"')
                              pronoun1()
                              slowprint('"Mhm"')
                              pronoun()
                              slowprint('"What did you take?"')
                              slowprint("[THERE IS ONLY A INCOMPREHENSIBLE MUMBLE IN REPLY]")
                              pronoun()
                              slowprint('"Can you tell me what you took?"')
                              slowprint("[YOU DON'T HEAR ANOTHER MUMBLE]")
                              pronoun()
                              slowprint('"Hey, stay awake"')
                              pronoun1()
                              slowerprint('"..."')
                              pronoun()
                              slowprint('"Hello?"')
                              slowprint("[THERE IS NO REPLY]")
                              print(" ")
                              slowprint("A: WHY?")
                              print(" ")

                              t14 = Timer(8,c8)
                              t14.start()
                              inpt14 = input(" ").upper()
                              print(" ")
                              if inpt14 == "A":
                                t14.cancel()
                                pronoun()
                                slowprint('"Why would you do this? You\'re so young"')
                                pronoun1()
                                slowerprint('"..."')
                                pronoun()
                                slowprint('"Kid?"')
                                slowprint("[THERE IS NO ANSWER]")
                                print(" ")
                                slowprint("A: ?")
                                print(" ")
                                t15 = Timer(8, c8)
                                t15.start()
                                inpt15 = input(" ").upper()
                                print(" ")
                                if inpt15 == "A":
                                  t15.cancel()
                                  pronoun()
                                  slowprint('"Kid?"')
                                  pronoun1()
                                  slowerprint('"..."')
                                  print(" ")
                                  slowprint("A: ?")
                                  print()
                                  t16 = Timer(8,c8)
                                  t16.start()
                                  inpt12 = input(" ").upper()
                                  print(" ")
                                  if inpt12 == "A":
                                    t16.cancel()
                                    pronoun()
                                    slowerprint('"Are you there? Please answer"')
                                    pronoun1()
                                    slowerprint("...")
                                    slowprint("[THERE IS NO ANSWER]")
                                    print(" ")
                                    slowprint("A: PANIC")
                                    slowprint("B: LISTEN")
                                    print(" ")
                                    t17 = Timer(8,c8)
                                    t17.start()
                                    inpt13 = input(" ").upper()
                                    print(" ")
                                    if inpt13 == "A":
                                      t17.cancel()
                                      slowprint("[YOU FEEL PANIC RISE IN YOUR CHEST]")
                                      pronoun()
                                      avgprint('"Hey? Kid! Kid, answer me!"')
                                      pronoun1()
                                      slowerprint('"......"')
                                      slowprint("[NOBODY ANSWERS]")
                                      endcard2()
                                    elif inpt13 == "B":
                                      t17.cancel()
                                      slowprint("[YOU HOLD YOUR BREATH AND LISTEN]")
                                      slowerprint("...")
                                      slowprint("[YOU DON'T HEAR ANYTHING FROM THE RECIEVER]")
                                      slowerprint("....")
                                      slowprint("[YOU LISTEN A LITTLE LONGER]")
                                      slowerprint(".....")
                                      slowprint("[YOU HEAR NO BREATHING]")
                                      endcard2()
                                    else:
                                      t17.join()


                                  else:
                                    t16.join()
                                else:
                                  t15.join()
                                  


                              else:
                                t14.join()


                              
                            
                            else:
                              t18.join()

                          else:
                            print(" ")





                            


                        else:
                          t7.join()

                      else:
                        pronoun1()
                        slowprint('"I\'v alr-dy d\'n it, too la\'e"')
                        pronoun1()
                        slowprint('"Maybe s\'m part of me wan\'ed to live"')
                        pronoun1()
                        slowprint('"Bu\' this \'s proba-ly f\'r the best"')
                        print(" ")
                        slowprint("A: WHAT?")
                        slowprint("B: WHY?")
                        slowprint("C: WHERE?")
                        print(" ")
                        t3w = Timer(8,c9)
                        t3w.start()
                        inpt3w = input(" ").upper()
                        print(" ")
                        if inpt3w == "A":
                          t3w.cancel()
                          pronoun()
                          slowprint('"What? What\'d you do?"')
                          pronoun1()
                          slowprint('"jus\' some meds"')
                          pronoun()
                          slowprint('"What meds? How much did you take?"')
                          pronoun1()
                          slowprint('"eno\'gh"')
                          print(" ")
                          slowprint("A: WHERE?")
                          slowprint("B: WHY?")
                          print(" ")
                          t2w = Timer(6, c9)
                          t2w.start()
                          inpt2w = input(" ").upper()
                          print(" ")
                          if inpt2w == "A":
                            t2w.cancel()
                            pronoun()
                            slowprint('"Where are you?"')
                            pronoun1()
                            slowprint('"Doe\'nt matt\'r"')
                            print(" ")
                            avgprint("A: SOFT")
                            avgprint("B: HARSH")
                            print(" ")
                            tsh = Timer(3, c9)
                            tsh.start()
                            inptsh = input(" ").upper()
                            print(" ")
                            if inptsh == "A":
                              tsh.cancel()
                              pronoun()
                              slowprint('"Of course it matters"')
                              pronoun()
                              slowprint('"You matter"')
                              pronoun1()
                              slowprint('"......"')
                              pronoun1()
                              slowprint('"Th-nk you, f\'r listning an\' caring, ev\'n a li-le"')
                              pronoun1()
                              slowerprint('"..."')
                              pronoun()
                              slowprint('"Kid-"')
                              print("*Click*")
                              endcard()

                            elif inptsh == "B":
                              tsh.cancel()
                              pronoun()
                              slowprint('"Yes, it matters"')
                              pronoun()
                              slowprint('"I get paid to help you, not sit here helplessly as you, what? kill yourself?"')
                              slowprint("[YOU HEAR A SHARP BREATH]")
                              slowprint("[YOU SEE YOUR COWORKER GIVING YOU A LOOK FROM THE CORNER OF YOUR EYE]")
                              pronoun1()
                              slowprint('"\'m s-rry"')
                              print("*Click*")
                              endcard3()

                            else:
                              tsh.join()

                          
                          elif inpt2w == "B":
                            t2w.cancel()
                            pronoun()
                            slowprint('"That\'s - that\'s, why would you-"')
                            pronoun1()
                            slowprint('"T\' make the pain go \'way"')
                            print(" ")
                            slowprint("A: WHERE?")
                            print(" ")
                            tw = Timer(5, c9)
                            tw.start()
                            inptw = input(" ").upper()
                            if inptw == "A":
                              tw.cancel()
                              pronoun()
                              slowprint('"Where are you right now?"')
                              pronoun1()
                              slowprint('"I g-t t\' go"')
                              print(" ")
                              avgprint("A: INTERVENE")
                              print(" ")
                              ti = Timer(3, c2)
                              ti.start()
                              inpti = input(" ").upper()
                              print(" ")
                              if inpti == "A":
                                ti.cancel()
                                avgprint('"Wait- please don\'t g- "')
                                c2()
                              else:
                                ti.join()
                            else:
                              tw.join()

                          else:
                            t2w.join()





                        elif inpt3w == "B":
                          t3w.cancel()
                          pronoun()
                          slowprint("Why, why did you call if you think that?")
                          pronoun1()
                          slowprint('"I don- \'ow"')
                          pronoun()
                          slowprint('"Part of you want\'s to live, righ? That\'s what you said"')
                          pronoun1()
                          slowprint('"Jus\' want s-mone t\' care"')
                          print(" ")
                          slowprint("A: WHERE?")
                          slowprint("B: FAMILY?")
                          print(" ")
                          t2w = Timer(6, c9)
                          t2w.start()
                          inpt2w = input(" ").upper()
                          print(" ")
                          if inpt2w == "A":
                            t2w.cancel()
                            pronoun()
                            slowprint('"Are you at home right now?"')
                            pronoun1()
                            slowprint('"uh huh"')
                            print(" ")
                            avgprint("A: WHAT?")
                            avgprint("B: WHERE?")
                            print(" ")
                            tsh = Timer(8, c9)
                            tsh.start()
                            inptsh = input(" ").upper()
                            print(" ")
                            if inptsh == "A":
                              tsh.cancel()
                              pronoun()
                              slowprint('"What did you do? You said you did something?"')
                              pronoun()
                              slowprint('"Pills of some kind?"')
                              pronoun1()
                              slowprint('"mhm"')
                              pronoun1()
                              slowprint('"St\'ps the pain"')
                              pronoun()
                              slowprint('"Okay, I need to know what kind so I can help you"')
                              pronoun1()
                              slowprint('"I don\' wan\' -elp"')
                              slowprint("[YOU HEAR THEM FUMBLING WITH THE PHONE]")
                              pronoun()
                              avgprint('"Wai-"')
                              print("*Click*")
                              endcard()

                            elif inptsh == "B":
                              tsh.cancel()
                              pronoun()
                              slowprint('"Where is your home?"')
                              
                              pronoun()
                              slowprint('"What about your family? Friends?"')
                              pronoun1()
                              slowprint('"Don\' -ave any frien\'s"')
                              pronoun1()
                              slowprint('"M\' fam-ly don\' care "')
                              slowprint("[YOU HEAR A SHARP BREATH]")
                              pronoun1()
                              slowprint('"an- neith\'r do you"')
                              pronoun()
                              avgprint('"Wait, I ca-"')
                              print("*Click*")
                              endcard()

                            else:
                              tsh.join()

                          
                          elif inpt2w == "B":
                            t2w.cancel()
                            pronoun()
                            slowprint('"What about your family? Friends?"')
                            pronoun1()
                            slowprint('"Don\' -ave any frien\'s"')
                            pronoun1()
                            slowprint('"M\' fam-ly don\' care "')
                            slowprint("[YOU HEAR A SHARP BREATH]")
                            pronoun1()
                            slowprint('"an- neith\'r do you"')
                            pronoun()
                            avgprint('"Wait, I ca-"')
                            print("*Click*")
                            endcard()
                        

                          else:
                            t2w.join()
                        elif inpt3w == "C":
                          t3w.cancel()

                          if inpt3w == "C":
                            pronoun()
                            slowprint('"Where are you right now?"')
                            pronoun1()
                            slowprint('"\'om"')
                            pronoun()
                            slowprint('"You\'re at home?"')
                            pronoun1()
                            slowprint('"mhm"')
                            pronoun()
                            slowprint('"Okay, stay awake for me"')
                            print(" ")
                            slowprint("A: HOME?")
                            slowprint("B: FAMILY?")
                            print(" ")
                            t2w = Timer(6, c9)
                            t2w.start()
                            inpt2w = input(" ").upper()
                            print(" ")
                            if inpt2w == "A":
                              t2w.cancel()
                              pronoun()
                              slowprint('"Where\'s your home?"')
                              pronoun1()
                              slowprint('"Doe\'nt matt\'r"')
                              print(" ")
                              avgprint("A: SOFT")
                              avgprint("B: HARSH")
                              print(" ")
                              tsh = Timer(3, c9)
                              tsh.start()
                              inptsh = input(" ").upper()
                              print(" ")
                              if inptsh == "A":
                                tsh.cancel()
                                pronoun()
                                slowprint('"Of course it matters"')
                                pronoun()
                                slowprint('"I can\'t help you if you I don\'t know where you are"')
                                pronoun()
                                slowprint('"Please, kid, let me help you"')
                                pronoun1()
                                slowprint('"......"')
                                pronoun1()
                                slowprint('"Th-nk you, f\'r listning an\' caring, ev\'n a li-le"')
                                pronoun1()
                                slowprint('"..."')
                                pronoun()
                                slowprint('"Kid-"')
                                print("*Click*")
                                endcard()

                              elif inptsh == "B":
                                tsh.cancel()
                                pronoun()
                                slowprint('"Yes, it matters"')
                                pronoun()
                                slowprint('"I get paid to help you, not sit here helplessly as you, what? kill yourself?"')
                                slowprint("[YOU HEAR A SHARP BREATH]")
                                slowprint("[YOU SEE YOUR COWORKER GIVING YOU A LOOK FROM THE CORNER OF YOUR EYE]")
                                pronoun1()
                                slowprint('"\'m s-rry"')
                                print("*Click*")
                                endcard3()

                              else:
                                tsh.join()

                            
                            elif inpt2w == "B":
                              t2w.cancel()
                              pronoun()
                              slowprint('"Do you have someone who can help nearby? Family? Friends?"')
                              pronoun1()
                              slowprint('"No"')
                              print(" ")
                              slowprint("A: HOME?")
                              print(" ")
                              tw = Timer(5, c9)
                              tw.start()  
                              inptw = input(" ").upper()
                              if inptw == "A":
                                tw.cancel()
                                pronoun()
                                slowprint('"Where is your house?"')
                                pronoun1()
                                slowprint('"n\' don\' wan- help"')
                                slowprint("[YOU HEAR THE CALLER MOVING TO HANG UP]")
                                slowprint("[THEY SOUND LIKE THEY'RE STRUGGLING]")
                                print(" ")
                                avgprint("A: INTERVENE")
                                print(" ")
                                ti = Timer(3, c2)
                                ti.start()
                                inpti = input(" ").upper()
                                print(" ")
                                if inpti == "A":
                                  ti.cancel()
                                  avgprint('"Wait- please don\'t g- "')
                                  c2()
                                else:
                                  ti.join()
                              else:
                                tw.join()

                            else:
                              t2w.join()

                        else:
                          t3w.join()

                      

                    else:
                      t6.join()


                
                else:
                  t4.join()

              elif inpt2 == "B":
                t3.cancel()
                f_point =+ 1
                print("not done yet")
              elif inpt2 == "C":
                f_point =+ 1
                t3.cancel()
                print("not done yet")
              else:
                t3.cancel
                end0()

        

            elif inpt1 == "B":
              t2.cancel()
              print("not done yet")
            
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

          print(" ")
          reply = input(" ").upper()
          print(" ")

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
    

