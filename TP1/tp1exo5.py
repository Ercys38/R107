Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> jour = int(input("Entrez le jour du moii : "))
Entrez le jour du moii : 3
>>> heure = int(input("Entrez l'heure actuelle (0-23) :"))
Entrez l'heure actuelle (0-23) :10
>>> minute = int(input("Entrez la minute actuelle (0-59) :"))
Entrez la minute actuelle (0-59) :33
>>> 
>>> minutes_ecoulees = (jour - 1) * 24 * 60 +heure * 60 + minute
>>> print(f"Depuis le début du mois, il s'est écoulées {minutes_ecoulees} minutes.")
Depuis le début du mois, il s'est écoulées 3513 minutes.
