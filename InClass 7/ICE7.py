# Wordnet

import nltk

#nltk.download('wordnet')
from nltk.corpus import wordnet as wn

syns = wn.synsets('Jeremiah')

for s in syns:
    print (s.definition())

# Token

import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

s = "'Good muffins cost $3.88\nin New York.','Please buy me\ntwo of them.','Thanks.'"

print(sent_tokenize(s))

print(word_tokenize(s))

# Stemming

import nltk
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer('spanish')
print(stemmer.stem('concinar'))

#Part of Speech

import nltk

#nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

words = word_tokenize('And now for something completely different')

print(pos_tag(words))

#Lemmatization

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('cooking'))
print(lemmatizer.lemmatize('cooking', pos = 'v'))

#Trigram

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

sent = "Jeremiah is a fool that love big ugly food."
n=3
trigrams = ngrams(sent.split(), n)
for grams in trigrams:
    print(grams)

#Trigram

#import nltk
#from nltk import word_tokenize
#from nltk.util import ngrams

#sent = "Jeremiah is a fool that love big ugly food."
#token = nltk.word_tokenize(sent)

#trigrams = ngrams(token,3)
#print(trigrams)


#Name Entity recognition

import nltk
nltk.download('words')
from nltk import pos_tag, ne_chunk
from nltk.tokenize import wordpunct_tokenize

sent = 'Jeremiah is a fool.'

print(ne_chunk(pos_tag(wordpunct_tokenize(sent))))



