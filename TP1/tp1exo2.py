Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=254
type(a)
<class 'int'>
data1=10
data2=11
print(data1, data2)
10 11
print("{} a {} ans".format(name, age)) # méthode format() permet une meilleure organisation de l’affichage des variables
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("{} a {} ans".format(name, age)) # méthode format() permet une meilleure organisation de l’affichage des variables
NameError: name 'name' is not defined
>>> var = (4500 + 2575) / 14800
>>> print ("Le resultat du calcul est", var)
Le resultat du calcul est 0.4780405405405405
>>>  print("Le résultat du calcul est {:.2f}".format(var))
...  
SyntaxError: unexpected indent
>>> print("Le résultat du calcul est {:.2f}".format(var))
Le résultat du calcul est 0.48

>>> name ="Eric"
>>> age=20
>>> f"Hello, {name}. vous avez {age} ans."
'Hello, Eric. vous avez 20 ans.'
>>> int nom
SyntaxError: invalid syntax
>>> nom ="Titi"
>>> prenom ="Toto"
>>> math = 14.5
>>> anglais = 11
>>> promotion =2025
>>> 
>>> #calcul de la moyenne
>>> m = (math + anglais +info) / 3
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    m = (math + anglais +info) / 3
NameError: name 'info' is not defined
>>> nom = "Titi"
>>> prenom ="Toto"
>>> math = 14.5
>>> anglais = 11
>>> info = 12
>>> promotion = 2025
>>> 
>>> #Calcul de la moyenne
>>> m = (math + anglais + info) / 3
>>> 
>>> #Afficher Type
>>> print ("type de nom :", type(nom))
type de nom : <class 'str'>
>>> print ("type de prenom :", type(prenom))
type de prenom : <class 'str'>
>>> print ("type de math :", type(math))
type de math : <class 'float'>
>>> print ("type de anglais :", type(anglais))
type de anglais : <class 'int'>
>>> print ("type de info :", type(info))
type de info : <class 'int'>
>>> print ("type de promotion :", type(promotion))
type de promotion : <class 'int'>
>>> print ("type de m :", type(m))
type de m : <class 'float'>
>>> 
>>> print(f"L'étudiant {prenom} {nom} de la promotion {promotion} a une moyenne de {m:.1f}")
L'étudiant Toto Titi de la promotion 2025 a une moyenne de 12.5
>>> 
>>> 
>>> 
