
# -*- coding: utf-8 -*-
# Déclaration de codage des caractères, utiliser souvent UTF-8, 
# pour prendre en charge toutes les langues

# ---------------------------

# affichage
print("Bonjour !")

# Lire entrée utilisateur
input1 = input()
print("User input is : ", input1)

# ---------------------------

# Déclaration des variables, pas de déclaration explicite
# Suffit d'affecter une valeur pour spécifier le type de variable
age = 125 
print("type de age", type(age))
salaire = 3.14
print("type de salaire", type(salaire))
name = "Ahmed"
print("type de name", type(name))

# ---------------------------

# Substitution
s2 = "I am %s" %name
s3 = "I am %d old" %age
print(s2, s3)

# ---------------------------

# Listes
liste = [1,2,31,4]
print("type de ls", type(liste))
print(liste)

# Ajouter un element
liste.append(5)
print (liste)

# Liste de mots
wordlist = ["I", "am", "learning", "english"]
print (wordlist)

# ---------------------------

# Dictionnaires
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict.keys())
print(thisdict.values())
print(thisdict["brand"])
for x, y in thisdict.items():
  print(x, y)

# ---------------------------

# Structure de contrôle
a = 15
if a > 15:  
    #attention aux tabulations
    print ('a supérieur à 15')
elif a <= 15 and a >= 10:
    print ('a entre 10 et 15')
else:
    print ('a est inférieur à 10')
    
# Tester si un élément appartient à une liste
a = 5
if a in liste:
    print ("a existe dans la liste")

# ---------------------------

# les boucles
for word in wordlist:
    print (word)

# Boucle et tests
# Calculer le nombre d'occurrence d'un caractère dans un string
chaine = "Le TAL est l’ensemble des méthodes et des programmes"
caractere= "e"
cpt = 0
for c in chaine:
    if c == caractere:
        cpt += 1
print("le caractère %s existe %d fois"%(caractere, cpt))


# 3 – Quelques programmes ---------------------------------------------------

# Programme python qui permet de calculer la fréquence des 
# caractères dans un texte
input_string = "Data Science calculer la fréquence des caractères"
frequencies = {} 
for char in input_string:    
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1   
print(frequencies)

# ---------------------------

# Programme python qui permet de calculer la fréquence des mots dans # un texte donné
input_string = "Data Science calculer la fréquence des caractères"
wordlist = input_string.split()
wordfreq = {} 
for word in wordlist:    
   if word in wordfreq: 
      wordfreq[word] += 1
   else: 
      wordfreq[word] = 1   
print(wordfreq)

# ---------------------------

# Les 6 mots les plus fréquents
print(sorted(wordfreq, key=wordfreq.get, reverse=True)[:6])

# ---------------------------