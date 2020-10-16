"""
Solution du travail à domicile - Module TAL / NLP

Plusieurs solutions existent, même plus performantes avec moins de lignes de code.
Cela dit, cette solution proposée n'utilisent que les concepts et librairies vus en cours/TP.

A noter, les fichiers reviews doivent être mis dans un dossier ./reviews
Exemple nom de fichier review : review4.txt
"""

# imports
import re

# ----------------------------------------------------------------------------------

# Question 1 and 2) - 10 reviews from imdb were downloaded and saved in folder /reviews 

# ----------------------------------------------------------------------------------

# Fonction - pour 3-a) - Lis un fichier et retourne son contenu
def read_file(filename):
    try:
        myfile = open(filename)
        return myfile.read();
    except:
        return "Can't open file " + filename

# Fonction - Preprocess (lower and tokenize) text review and returns words list 
def preprocess(review):
    review = review.lower()
    #wordlist = review.split()
    wordlist = re.split("[\s.,!?:;\"-]+", review)
    wordlist = [x for x in wordlist if x != '']
    return wordlist
    
# Fonction - pour 3-b) - Calculer la fréquence de chaque mot dans un texte donné comme liste
def word_freq(wordlist):
    wordfreq = {}
    for word in wordlist:
        wordfreq[word] = wordlist.count(word)
    return (wordfreq)

# Fonction - pour 3-d) - Construire et afficher un index de tous les mots par leurs lemmes
SUFFIX_LIST = [ 'er','ing','ship','ment','al','ery','ion','ive','able','ible','ic','ant','ancy','y','ed']
def stemming(word, suffix_list):
    stem_list =[]
    for suffix in suffix_list:
        if word.endswith(suffix):
            stem = re.sub(suffix+'$','', word)
            stem_list.append([word, stem, suffix])
    return stem_list;

# ----------------------------------------------------------------------------------
    
# Liste - pour 3-e) - Calculer et afficher pour chaque fichier le pourcentage des stopwords
STOPWORDS_LIST = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
                  "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", 
                  "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", 
                  "theirs", "themselves", "what", "which", "who", "whom", "this", "that", 
                  "these", "those", "am", "is", "are", "was", "were", "be", "been", 
                  "being", "have", "has", "had", "having", "do", "does", "did", "doing", 
                  "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", 
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", 
                  "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", 
                  "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", 
                  "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", 
                  "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", 
                  "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", 
                  "should", "now"]

# ----------------------------------------------------------------------------------
    
def main():
    print('-'*50)
    
    # Question 3-a) - Lire un fichier review de votre choix et afficher son contenu
    review = read_file('reviews/review1.txt')
    print("Le contenu du fichier review :\n", review)
       
    print('-'*50)
       
    # Question 3-b) - Calculer et afficher la fréquence de chacun des mots dans chaque fichier
    for i in range(0,10):
        review = read_file('reviews/review' + str(i) +'.txt')
        wordlist = preprocess(review)
        print('La fréquence de chaque mot du fichier review ' + str(i) + ' est : ')
        print(word_freq(wordlist))
        print('\n')

    print('-'*50)
       
    # Question 3-c) - Calculer et afficher les 5 mots les plus similaires qu’on retrouve dans tous les fichiers.
    wordlists = []
    for i in range(0,10):
        review = read_file('reviews/review' + str(i) +'.txt')
        wordlist = preprocess(review)
        wordlists.append(wordlist)
    
    similar_words = []
    
    for i in range(0,10):
        flag = True
        list_element = wordlists.pop()
        for word in list_element:
            for sublist in wordlists:
                if word not in sublist:
                    flag = False
                    break   
            if flag and word not in similar_words:
                similar_words.append(word) 
        wordlists.insert(0, list_element)
    
    print("Les 5 mots les plus similaires qu'on retrouve dans TOUS les fichiers sont: ")
    print(similar_words[:6])
            
    print('-'*50)
    
    # Question 3-d) - Construire et afficher un index de tous les mots par leurs lemmes
    for i in range(0,10):
        review = read_file('reviews/review' + str(i) + '.txt')
        wordlist = preprocess(review)
        index_dict = {}
        for word in wordlist:
            index_list = []
            stem_list = stemming(word, SUFFIX_LIST)
            if stem_list :
              for j in range(0, len(stem_list)):  
                index_list.append(stem_list[j][1])
              index_dict[word] = index_list     
        print('\nIndex des mots par leurs lemmes - Fichier Review ', i)
        print(index_dict)
    
    print('-'*50)
    
    # Question 3-e) - Calculer et afficher pour chaque fichier le pourcentage des stopwords
    for i in range(0,10):
        count = 0
        review = read_file('reviews/review' + str(i) + '.txt')
        wordlist = preprocess(review)
        for word in wordlist:
            if word in STOPWORDS_LIST:
                count += 1
        percent = (count / len(wordlist)) * 100
        print("Le pourcentage des stopwords du fichier review ", i, ' : ', percent)
    

# ----------------------------------------------------------------------------------
    
if __name__ == "__main__":
    main()
    
# ----------------------------------------------------------------------------------    
    
    
    
    
    
    
    
    
    
    