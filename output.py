Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>>  25 / 5
 
SyntaxError: unexpected indent
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print ('Mijn naam is Jaymar')
Mijn naam is Jaymar
>>> naam = Jaymar
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    naam = Jaymar
NameError: name 'Jaymar' is not defined
>>> naam = 'Jaymar'
>>> print(naam)
Jaymar
>>> print(naam.upper())
JAYMAR
>>> print(naam[0:2])
Ja
>>> print(naam[::-1])
ramyaJ
>>> leeftijd = 18
>>> print ('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Jaymar ben je al 18 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
19
>>> leeftijd-= 1
>>> leeftijd
18
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd < 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
	print('Je bent precies ' + str(leeftijd) + ' jaar')

	
Je bent precies 18 jaar
>>> from random import randint
>>> randint(0,1000)
539
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
929
>>> print('Willekeurig getal tussen 0 en 1000 ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000 929
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 12:59:10.667321
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> 