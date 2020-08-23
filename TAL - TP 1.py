
# déclaration de codage des caractère, utiliser souvent UTF-8, pour prendre en charge toutes les langues.
print ("Salam Alykom")

# lire entrée utilisateur
input1 = input()
print("User input is : ", input1)

# Déclaration des variables
# pas de déclaration explicite
# il suffit d'affecter une valeur pour spécifier le type d'une variable
age = 125 # entier
print("type de age", type(age))
salaire = 3.14
print("type de salaire", type(salaire))
name = "Ahmed"
print("type de name", type(name))

#substitution
s2 = "I am %s" %name
s3 = "I am %d old" %age
print (s2, s3)

# listes
liste = [1,2,31,4]
print ("type de ls", type(liste))
print (liste)

# ajouter in element
liste.append(5)
print (liste)

# liste de mots
wordlist = ["I", "am", "learning", "english"]
print (wordlist)

# les dictionnaires
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


# structure de controle
a = 15
if a > 15:  
    #attention aux tabulations
    print ('a supérieur à 15')
elif a <= 15 and a >= 10:
    print ('a entre 10 et 15')
else:
    print ('a est intfieur à 10')
    
# tester si un element appartient à une liste
a = 5
if a in liste:
    print ("a existe dans la liste")
    
# les boucles
for word in wordlist:
    print (word)

# boucle et tests
# calculer le nombre d'occurence d'un caractère dans une chaine de caractère
chaine = "Le TAL est l’ensemble des méthodes et des programmes qui permettent"
caractere= "e"
cpt = 0
for c in chaine:
    if c == caractere:
        cpt += 1
print("le caractère %s existe %d fois"%(caractere, cpt))

