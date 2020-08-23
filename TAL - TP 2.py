
# importer la bibliothèque sys
# on veut l'utiliser pour quiter le programme en cas d'erreur
import sys

# lire du texte à partir d'un fichier
def treat_line(line):
    """
    traiter une ligne de texte.
    """
    return line

def read_file(filename):
    try:
        myfile = open(filename)
    except:
        print("Can't open file ", filename)
        sys.exit()
    # lecture des lignes de texte
    return myfile.readlines();

def treat_text(lines):
    for line in lines:
        print(line)

# La fonction main
if __name__ == '__main__':
    DATA_FILE = "D:/Module - TAL/coursTAL-zip/Code/text.txt"
    lines = read_file(DATA_FILE)
    print(lines)
    treat_text(lines);
    treat_line(lines)

############################################################################

# Tester la fonction tokenize() - Split text into words
def tokenize(text):
    # diviser la lignes par les espaces
    list_word = text.split(" ")
    return list_word

# La fonction main
if __name__ == '__main__':
    text = "I'm Very Hungry, I want to eat something."
    tokens = tokenize(text);
    print(tokens)    
    
############################################################################    

# plusieurs implémentation de la fonction tokenize()
# tokenize par des expression régulière simple
# regular expression
import re
def tokenize_regex_punct(text):
    """ extraire les mots"""
    tokens = re.split("[.,:; ]+", text)
    return tokens
# tokenize par des expression régulière simple, en gardant la ponctuation
def tokenize_regex_punct_keep(text):
    """ extraire les mots"""
    tokens = re.split("([.,:; ]+)", text)
    return tokens
# tokenize par des expression régulière
def tokenize_regex(text):
    """ extraire les mots"""
    tokens = re.split("\W+", text)
    return tokens
# tokenize par des expression régulière, en gardant la ponctuation
def tokenize_regex_keep_punct(text):
    """ extraire les mots"""
    tokens = re.split("(\W+)", text)
    return tokens
# La fonction main
if __name__ == '__main__':
    text = "I'm Very Hungry, I want to eat something. United Kingdom."
    tokens = tokenize_regex_punct(text);
    print(tokens)
    tokens = tokenize_regex_punct_keep(text);
    print(tokens) 
    tokens = tokenize_regex(text);
    print(tokens) 
    tokens = tokenize_regex_keep_punct(text);
    print(tokens) 
    
############################################################################

# L'encodage
# afficher tous les codages qui existes
import sys
import encodings

# get encoding sets
codages = encodings.aliases.aliases.values()

# eliminer les doubles
codages = set(codages)

# trier les elements de la liste
codages = sorted(codages)

# la command join permet de mettre un separateur entre les éléments d'une liste
print("\n".join(codages))

# fixer le codage des caractères dans l'entête de script
# -*- coding: utf-8 -*-

# en python 2.7,
# il existe deux types de chaine de caractère le type str, et le type unicode
print(type('chaine')) # bits => encodée
print(type(u'chaine')) # unicode => décodée
print(type(u'étudiant')) # unicode => décodée
print(type(u' السلام عليكم ')) # unicode => décodée

# python 3
print(type("chaine")) # unicode => decodée
print(type(b"chaine")) # bits => encodée

# pour lire le contenu d'un fichier utiliser le décodage
f = open("D:/Module - TAL/coursTAL-zip/Code/text.txt")

#python 2.7
line = f.readline().decode('utf8')
# pour afficher utiliser encoder
print(line.encode('utf8'))
print(u" السلام عليكم ".encode('utf8'))

#python3
line = f.readline()
print(line)

#code unicode des caractères    
l = list(' السلام عليكم ')
print(l)
for c in l:
    print(c)
    
print("\u0643\u0644\u0645")

#We can use this to print chemical formulas too.
print("The chemical formula of water is H\u2082O.Water dissociates into H\u207A and OH\u207B")

# There are other encodings too. See the symbols here: http://en.wikipedia.org/wiki/Number_Forms
print('1/4 or \u00BC')
print('A good idea\u00AE')

# afficher les caractères arabe en unicode dans l’intervalle
for i in range(0x0600, 0x06ff):
    print(chr(i))
    
# afficher les caractères tifinagh en unicode dans l’intervalle
for i in range(0x2d30,0x2d6f):
    print(chr(i))
    
# afficher les caractères arabe en unicode avec leurs noms
import unicodedata
for i in range(0x0627,0x06ff):
    try:
        print(unicodedata.name(chr(i)))
    except:
        name ="no name" 
        












