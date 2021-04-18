
# How to install and import nltk
# In terminal or prompt:
# pip install nltk
import nltk

# importing tokenization 
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

# importing the stopwords
from nltk.corpus import stopwords

# importing Porter and Lancaster stemmers from nltk
from nltk.stem import PorterStemmer, LancasterStemmer

# importing WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

# ------------------ Stemming -----------------------------------------------------

# LancasterStemmer is simple, but heavy stemming due to iterations and over-stemming may occur. 
# Over-stemming causes the stems to be not linguistic, or they may have no meaning. 
# LancasterStemmer produces an even shorter stem than porter because of iterations and over-stemming is occurred.



# create an object of class PorterStemmer and LancasterStemmer
porter = PorterStemmer()
lancaster = LancasterStemmer()

# - Stemming a word - PorterStemmer
print("Porter Stemmer")
print(porter.stem("cats"))
print(porter.stem("trouble"))
print(porter.stem("troubling"))
print(porter.stem("troubled"))

# - Stemming a word - LancasterStemmer 
print("Lancaster Stemmer")
print(lancaster.stem("cats"))
print(lancaster.stem("trouble"))
print(lancaster.stem("troubling"))
print(lancaster.stem("troubled"))

# ---------------------------

# - Stemming a list of words
word_list = ["friend", "friendship", "friends", "friendships","stabil","destabilize","misunderstanding","railroad","moonlight","football"]
print("{0:20}{1:20}{2:20}".format("Word","Porter Stemmer","lancaster Stemmer"))
for word in word_list:
    print("{0:20}{1:20}{2:20}".format(word, porter.stem(word), lancaster.stem(word)))

# ---------------------------

# - Stemming a sentence without tokenization
sentence = "Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."
porter.stem(sentence)

# ---------------------------

# - Stemming a sentence with word tokenization (punctuations are keeped with word_tokenizer)

sentence = "Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."

def stemSentence(sentence):
	# Tokenization
    token_words = word_tokenize(sentence)
    print('Tokens:', token_words)
    # Stemming
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

stems = stemSentence(sentence)
print('Stems: ', stems)

# ---------------------------

# - Stemming a sentence with tokenization, without stopwords

# downloading stopwords from nltk
nltk.download('stopwords')

# assigning the english stop-words to the sw list
sw = stopwords.words('english')

sentence = "Pythoners are very intelligent, and work very pythonly and now they are pythoning their way to success."

def cleanStemSentence(sentence):
    token_words = word_tokenize(sentence)
    # eliminate the stop words from the tokens
    clean_tokens = [token for token in token_words if token not in sw]
    print('Tokens:', clean_tokens)
    stem_sentence = []
    for word in clean_tokens:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

stems = cleanStemSentence(sentence)
print('Stems: ', stems)

# ---------------------------

# - Stemming a sentence with word tokenization (remove punctuations with RegexpTokenizer)

tokenizer = RegexpTokenizer(r'\w+')

sentence = "Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."

def stemSentence(sentence):
	# Tokenization
    token_words = tokenizer.tokenize(sentence)
    print('Tokens:', token_words)
    # Stemming
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

stems = stemSentence(sentence)
print('Stems: ', stems)

# ---------------------------

# - Stemming a document

with open("my_text.txt") as file:
	my_lines_list = file.readlines()

porter = PorterStemmer()

def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

# Stemming the first line of the document
stems = stemSentence(my_lines_list[0])
print('Sentence: ', my_lines_list[0])
print('Stemmed sentence: ', stems)

# Stemming all lines of the document
for line in my_lines_list:
    stem_sentence = stemSentence(line)
    print('Sentence: ', line)
    print('Stemmed sentence: ', stem_sentence)


# --------------------------- Lemmatization --------------------------------------------

# Lemmatization using WordNet Lemmatizer, with and without context - POS

# Instantiating the lemmaztizer object
lemmatizer = WordNetLemmatizer()

# ---------------------------

# - Lemmatize a single word without context
print(lemmatizer.lemmatize("bats"))
print(lemmatizer.lemmatize("feet"))
print(lemmatizer.lemmatize("are"))

# - Lemmatize a single word with context :parts-of-speech (POS) parameter 
print(lemmatizer.lemmatize("are", pos='v'))
print(lemmatizer.lemmatize("swimming", pos='n'))
print(lemmatizer.lemmatize("stripes", pos='v')) 
print(lemmatizer.lemmatize("stripes", pos='n'))

# ---------------------------

# - Lemmatize a sentence
sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."

# tokenize the sentence into a list of words without punctiations
tokenizer = RegexpTokenizer(r'\w+')
sentence_words = tokenizer.tokenize(sentence)

# without context
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print ("{0:20}{1:20}".format(word, lemmatizer.lemmatize(word)))


# with context : parts-of-speech (POS) parameter = V
for word in sentence_words:
    print ("{0:20}{1:20}".format(word, lemmatizer.lemmatize(word, pos="v")))


# ---------------------------
# Reference : https://www.datacamp.com/community/tutorials/stemming-lemmatization-python