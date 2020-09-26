import time

name = "Jaymar"
surname = "Westerlow"
age = 18
residence = "Almere"
home2school = 28.0
hobbys = ["gamen", "sporten", "stappen"]

print("Mijn voornaam is " + name + " en mijn achternaam is " + surname + ".")
time.sleep(2)
print("Ik ben " + str(age) + " jaar oud, ik woon in " + residence + " en de afstand tussen mijn huis en school is " + str(home2school) + ".")
time.sleep(2)
print("Mijn hobby's zijn: " + ', '.join(hobbys) + ".")

print()
