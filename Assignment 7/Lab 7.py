# David Ziama
# Lab Assignment 7


import nltk
from nltk.corpus import stopwords, wordnet as wn
from nltk.tokenize import RegexpTokenizer, word_tokenize, sent_tokenize
from collections import Counter
import string

# Initializing variables

text_NoStopWords = ""
text_NoPunct = ""
words_NoVerbs = []
res = []
text_res = ""

#Read the file
data = file('file1.txt').read()

# Remove all the words like “a the ! ? ...” Which does not have meaning using stopwords in NLTK
stop = set(stopwords.words('english'))

for i in data.lower().split():
    if i not in stop:
        text_NoStopWords = text_NoStopWords +' ' + i

punct = set(string.punctuation)
text_NoPunct = ''.join(x for x in text_NoStopWords if x not in punct)

# Using POS, remove all the verbs
words = word_tokenize(text_NoPunct)
tokes_pos = nltk.pos_tag(words)
for i in tokes_pos:
    if 'VB' not in i[1]:
        words_NoVerbs.append(i[0])

# Choose top five words that has been repeated most
counts = Counter(words_NoVerbs).most_common(5)

# Find all the sentences with those most repeated words. Extract those sentences and concatenate
for top in counts:
    for sent in sent_tokenize(data.lower()):
        if sent not in text_res:
            if top[0] in word_tokenize(sent):
                text_res = text_res + sent
