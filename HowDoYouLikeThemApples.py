import math
import time

#Vervang de 0-en met de juiste berekeningen

trees               = 333             #hoeveel bomen zijn er in totaal?
shadedTrees         = math.ceil(222)  #hoeveel bomen staan er in de schaduw (afgerond naar boven)?
sunnyTrees          = 111             #hoeveel in de zon?

shadeOutputModifier = 80              #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146             #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = 116.8           #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = 16206           #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = 25929.6         #hoeveel appels geven alle schaduw bomen?
totalOutput         = 42135.6         #hoeveel appels zijn er in totaal?

owners              = 3               #met hoeveel mensen verdelen we de appels?

eatCount            = 0.6             #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = 42135           #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = 14045           #hoeveel appels mag ik verkopen?

print("Er zijn in totaal " + str(trees) + " bomen.")
time.sleep(2.5)

print("Een boom in de zon produceert " + str(sunnyTreeOutput) + " appels.")
time.sleep(2.5)

print("Een boom in de schaduw produceert " + str(shadeOutputModifier) + "% van de appels dat een boom in de zon doet.")
time.sleep(3)

print("Er staan " + str(sunnyTrees) + " In de zon")
time.sleep(2.5)

print("Er staan " + str(shadedTrees) + " In de schaduw")
time.sleep(2.5)

print("De appels worden tussen " + str(owners) + " mensen verdeelt.")
time.sleep(2.5)

print("De " + str(sunnyTrees) + " bomen produceren in totaal " + str(sunnyOutput) + ".")
time.sleep(2.5)

print("De " + str(shadedTrees) + " bomen produceren in totaal " + str(shadedOutput) + ".")
time.sleep(2.5)

print(str(sunnyOutput) + " + " + str(shadedOutput) + " = " + str(totalOutput))
time.sleep(2.5)

print("De " + str(eatCount) + " kunnen we niet verkopen, dus verkopen van de  " + str(totalOutput) + " appels " + str(sellableOutput) + ".")
time.sleep(2.5)

print(str(sellableOutput) + " gedeelt door " + str(owners) + " = " + str(cut))
time.sleep(2.5)



print(str(cut) +  " is hoeveel appels ik kan verkopen")