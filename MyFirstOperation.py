import time
import math

print("We gaan een aantal rekensommen behandelen.")
time.sleep(2)

print("De eerste som is een plus (+) som.")
time.sleep(2)

print("Vul het 1e getal in.")

num1plus = float(input())
time.sleep(1)

print("Vul nu het 2e getal in.")

num2plus = float(input())
time.sleep(1)

print("Het antwoord van deze plus (+) som is:")
time.sleep(0.5)

n1plusn2 = num1plus + num2plus

print(n1plusn2)
time.sleep(2)



print("De tweede som is een min (-) som.")
time.sleep(2)

print("Vul het 1e getal in.")

num1min = float(input())
time.sleep(1)

print("Vul nu het 2e getal in.")

num2min = float(input())
time.sleep(1)

print("Het antwoord van deze min (-) som is:")
time.sleep(0.5)

n1minn2 = num1min - num2min

print(n1minn2)
time.sleep(2)


print("De derde som is een keer (*) som.")
time.sleep(2)

print("Vul het 1e getal in.")

num1keer = float(input())
time.sleep(1)

print("Vul nu het 2e getal in.")

num2keer = float(input())
time.sleep(1)

print("Het antwoord van deze keer (*) som is:")
time.sleep(0.5)

n1keern2 = num1keer * num2keer

print(n1keern2)
time.sleep(2)


print("De vierde som is een deel (/) som.")
time.sleep(2)

print("Vul het 1e getal in.")

num1deel1 = float(input())
time.sleep(1)

print("Vul nu het 2e getal in.")

num2deel1 = float(input())
time.sleep(1)

print("Het antwoord van deze deel (/) som is:")
time.sleep(0.5)

n1deel1n2 = num1deel1 / num2deel1

print(n1deel1n2)
time.sleep(2)



print("De vijfde som is opnieuw een deel (/) som, maar word hij deze keer afgerond.")
time.sleep(2)

print("Vul het 1e getal in.")

num1deel2 = float(input())
time.sleep(1)

print("Vul nu het 2e getal in.")

num2deel2 = float(input())
time.sleep(1)

print("Het antwoord van deze deel (/) som is:")
time.sleep(0.5)

n1deel2n2 = num1deel2 // num2deel2

print(n1deel2n2)
time.sleep(2)



print("De zesde som is opnieuw een deel (/) som, maar geeft de restwaarde in plaats van het aantal keer gedeeld.")
time.sleep(2)

print("Vul het 1e getal in.")

num1deel3 = float(input())
time.sleep(1)

print("Vul nu het 2e getal in.")

num2deel3 = float(input())
time.sleep(1)

print("Het antwoord van deze deel (/) som is:")
time.sleep(0.5)

n1deel3n2 = num1deel3 % num2deel3

print(n1deel3n2)
time.sleep(2)


print("De zevende som is het optellen bij het antwoord van een som")
time.sleep(2)

print("Vul het 1e getal in.")

num1plusplus = float(input())
time.sleep(1)

print("Vul nu het 2e getal in.")

num2plusplus = float(input())
time.sleep(1)

print("Het antwoord van deze plus (+) som is:")
time.sleep(0.5)

n1plusplusn2 = num1plusplus + num2plusplus
print(n1plusplusn2)
time.sleep(2)

print("Vul het getal in dat je bij het antwoord wilt optellen.")

num3plusplus = float(input())
time.sleep(1)

print("Het antwoord van de eerste som plus (+) de input is:")
n1plusplusn2 += num3plusplus
print(n1plusplusn2)
time.sleep(2)