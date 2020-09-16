import time

#Name:				Kazuya Mishima

#All attributes:
#1.	Health:			Standard(170)
#2.	Strength:		60
#3.	Magic:			Standard(20)( + 10 * 4 while in devil transformation)
#4.	Evasion:		70( + 30 while in devil transformation)
#5.	Stealth:		0
#6.	Defence:		Standard(50)
#7.	Magic Resistance:	30( x 4 while in devil transformation)
#8.	Special Moves:		Wavedash, Electric Wind God Fist
#9.	Rage Moves:		Rage Art, Rage Drive, Devil Transformation	(During Rage)
#10.	Transformations:	Devil Kazuya					(During Rage)





name = "Kazuya Mishima"
stat_health = "Standard (170)"
stat_strength = 60
stat_magic = "Standard(20)(+ 10 * 4 while in devil transformation)"
stat_evasion = 70
stat_stealth = 0
stat_defence = "Standard (50)"
stat_magic_resistance = 30
stat_special_moves = ["Wavedash", "Electric Wind God Fist"]
stat_rage_moves = ["Rage Art", "Rage Drive", "Devil transformation"]
stat_transformations = "Devil Kazuya"


print("Name:			" + name)
print("")
time.sleep(0.8)

print("Character Statistics")
time.sleep(0.5)
print("Health:			" + stat_health)
time.sleep(0.2)
print("Strength:		" + str(stat_strength))
time.sleep(0.2)
print("Magic:			" + stat_magic)
time.sleep(0.2)
print("Evasion:		" + str(stat_evasion))
time.sleep(0.2)
print("Stealth:		" + str(stat_stealth))
time.sleep(0.2)
print("Defence:		" + stat_defence)
time.sleep(0.2)
print("Magic Resistance:	" + str(stat_magic_resistance))
time.sleep(0.2)
print("Special Moves:		" + str(stat_special_moves))
time.sleep(0.2)
print("Rage Moves:		" + str(stat_rage_moves))
time.sleep(0.2)
print("Transformations:	" + stat_transformations)
time.sleep(0.2)



