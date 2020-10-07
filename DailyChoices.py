import time

print("Hello you! What's your name?")

name = input(">")

len(name)


while len(name) < 1:
 
    if len(name) == 0:
        
        print("Sorry, i didn't get that. What's your name?")
        name = input(">")
time.sleep(1)

print("Hi ",name,", i've got a few questions for you.")

#__________________________________________________________________________________________________________
x = 0




print("1st question, can you guess how old I am?")
print("a). 16")
print("b). 18")
print("c). 20")
time.sleep(1)

antwoord_1 = input(">")
if antwoord_1.lower() == "b" or antwoord_1.lower() == "18":
  time.sleep(1)
  print("That's correct, next question!")
  x = x + 1
elif antwoord_1.lower() == "a" or antwoord_1.lower() == "16":
  time.sleep(1)
  print("You're just off, a little higher. I'm 18, next question!")
elif antwoord_1.lower() == "c" or antwoord_1.lower() == "20":
  time.sleep(1)
  print("You're just off, a little lower. I'm 18, next question!")
else:
  time.sleep(1)
  print("That's not.. Never mind, next question.")
time.sleep(2)

print("Alright ",name,", where do you think i live?")
print("a). Amsterdam")
print("b). Amersfoort")
print("c). Almere")
time.sleep(1)


split = 0


while split < 1:
  antwoord_2 = input(">")
  if antwoord_2.lower() == "a" or antwoord_2.lower() == "amsterdam":
    time.sleep(1)
    split = split + 1
    print("That's incorrect, however i do go to my father in Amsterdam every other weekend.")
    time.sleep(1)
  elif antwoord_2.lower() == "b" or antwoord_2.lower() == "amersfoort":
    time.sleep(1)
    print("that's not right, try again.")
  elif antwoord_2.lower() == "c" or antwoord_2.lower() == "almere":
    time.sleep(1)
    print("You're right! Next question.")
    x = x + 1
    split = split + 2
  else:
    time.sleep(1)
    print("Uhhm... Try again i guess.")
time.sleep(2)



if split == 1:
  print("Last question, where in Amsterdam do you think i go?")
  print("a). Amsterdam Noord")
  print("b). Amsterdam West")
  print("c). Amsterdam Zuid-oost")
  time.sleep(1)

  antwoord_4 = input(">")
  if antwoord_4.lower() == "a" or antwoord_4.lower() == "amsterdam noord":
    time.sleep(1)
    print("Indeed, i do go to Amsterdam Noord")
    x = x + 1
  elif antwoord_4.lower() == "b" or antwoord_4.lower() == "amsterdam west":
    time.sleep(1)
    print("That's not right, i go to Amsterdam Noord")
  elif antwoord_4.lower() == "c" or antwoord_4.lower() == "amsterdam zuid-oost":
    time.sleep(1)
    print("That's not right, i go to Amsterdam Noord")
  else:
    time.sleep(1)
    print("Well...")
    time.sleep(3)
    print("Alright then...")
  time.sleep(2)


  
else:
  print("Last question ",name,", which one of the following options are hobbies of mine?")
  print("a). Playing the piano")
  print("b). Gaming")
  print("c). Martial Arts")
  time.sleep(1)

 
  
  antwoord_3 = input(">")
  if antwoord_3.lower() == "a" or antwoord_3.lower() == "playing the piano":
    time.sleep(1)
    print("You're right, although all three options were right.")
    x = x + 1
  elif antwoord_3.lower() == "b" or antwoord_3.lower() == "gaming":
    time.sleep(1)
    print("You're right, although all three options were right.")
    x = x + 1
  elif antwoord_3.lower() == "c" or antwoord_3.lower() == "martial arts":
    time.sleep(1)
    print("You're right, although all three options were right.")
    x = x + 1
  else:
    time.sleep(1)
    print("Nou, uhhm... ")
    time.sleep(3)
    print("ooookeeej...")
  time.sleep(2)

if x == 3:
  print("you gave the correct awnsers on all of the questions!")
else:
  print("That's all!")
  

time.sleep(3)