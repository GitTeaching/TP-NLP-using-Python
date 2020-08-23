
# Générer des phrases de nombres

def num_vers_mot(n):
    mot = ""

    b1 = n % 10
    b2 = (n % 100)//10
    b3 = (n % 1000)//100
    #print(b1, b2, b3) 
         
    if n == 0:
        return 'ZERO' 
    
    if n > 999:
      return None

    if b2 == 0:
        mot = ones[b1]
    elif b2 == 1:
        mot = tens[b1] 
    elif b2 > 1:
        mot = twenties[b2] + ones[b1] +  mot
    
    if b3 == 1:
        mot = "CENT " + mot
    elif b3 > 0:
        mot = ones[b3] + "CENT " + mot

    return mot

ones = ["","UN ","DEUX ","TROIS ","QUATRE ","CINQ ","SIX ","SEPT ","HUIT ","NEUF "]
tens = ["DIX ","ONZE ","DOUZE ","TREIZE ","QUATORZE ","QUINZE ","SEIZE ","DIX SEPT ","DIX HUIT ","DIX NEUF "]
twenties = ["","DIX ","VINGT ","TRENTE ","QUARANTE ","CINQUANTE ","SOIXANTE ","SOIXANTE ","QUATRE VINGT ","QUATRE VINGT "]

n = 895
print(n)
print(num_vers_mot(n))

#################################################################

# Version anglaise

def num_vers_mot_eng(n):
    mot = ""

    b1 = n % 10
    b2 = (n % 100)//10
    b3 = (n % 1000)//100
    #print(b1, b2, b3) 
         
    if n == 0:
        return 'ZERO' 
    
    if n > 999:
      return None

    if b2 == 0:
        mot = ones[b1]
    elif b2 == 1:
        mot = tens[b1] 
    elif b2 > 1:
        mot = twenties[b2] + ones[b1] +  mot
    
    if b3 > 0:
        mot = ones[b3] + "hundred and " + mot

    return mot

ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine "]
tens = ["ten ","eleven ","twelve ","thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]
twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]

n = 158
print(n)
print(num_vers_mot_eng(n))

#######################################################

# En utilisant la librairie inflect - Anglais
import inflect
p = inflect.engine()
p.number_to_words(32)