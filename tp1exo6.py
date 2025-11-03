Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> minutes_ecoulees = int(input("Entrez le nombre de minutes écoulées depuis le début du mois :"))
Entrez le nombre de minutes écoulées depuis le début du mois :14823
>>> jour = minutes_ecoulees // (24*60) + 1
>>> reste = minutes_ecoulees % (24*60)
>>> heure = reste // 60
>>> minute = rest % 60
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    minute = rest % 60
NameError: name 'rest' is not defined. Did you mean: 'reste'?
>>> minute = rete % 60
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    minute = rete % 60
NameError: name 'rete' is not defined. Did you mean: 'reste'?
>>> minute = reste % 60
>>> print(f"La date correspond au jour {jour}, à {heure:02d}h{minute:02d}.")
La date correspond au jour 11, à 07h03.
