# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:04:36 2020

@author: Hedia
"""

import re

# la liste des suffixes
SUFFIX_LIST=['ique', 'ation', 'tion', 'é', 'er','eur', 'ien', 'iste', 'able', 'ible', 'ard', 'phobe']

def stemming(word, suffix_list):
    """ stem a word"""
    stem_list =[]
    for suffix in suffix_list:
        if word.endswith(suffix):
            stem = re.sub(suffix+'$','', word)
            stem_list.append((word, stem, suffix))
    return stem_list;

if __name__ == "__main__":
    text = """Soundex est un algorithme phonétique d'indexation de noms par
    leur prononciation en anglais britannique"""
    
    #tokenize
    list_word = text.split(' ')
    list_word = re.split("\W+", text)
    
    #print stemme
    for word in list_word:
        print(word, stemming(word, SUFFIX_LIST))

##########################################################################################
        
# Indexer les mots par leur lemmes    
# Enrichir la liste des suffixes afin de lemmatiser les mots de votre texte
SUFFIX_LIST=['ique', 'ation', 'tion', 'é', 'er','eur', 'ien', 'iste', 'able', 'ible', 'ard', 'phobe']

def stemming(word, suffix_list):
    """ stem a word"""
    stem_list =[]
    for suffix in suffix_list:
        if word.endswith(suffix):
            stem = re.sub(suffix+'$','', word)
            stem_list.append([word, stem, suffix])
    return stem_list;

text = """Soundex est un algorithme phonétique d'indexation de noms indexation par leur prononciation en anglais britannique"""
    
#tokenize
list_word = text.split(' ')
list_word = re.split("\W+", text)
    
#print stemme
for word in list_word:
    print(word, stemming(word, SUFFIX_LIST))

# Indexer les mots par leurs lemmes
index_dict = {}
for word in list_word:
    index_list = []
    stem_list = stemming(word, SUFFIX_LIST)
    if stem_list :
      for i in range(0, len(stem_list)):  
        index_list.append(stem_list[i][1])
      index_dict[word] = index_list
      
print('\nIndex des mots par leurs lemmes : ')
print(index_dict)











