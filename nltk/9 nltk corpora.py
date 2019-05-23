from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

train_text = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(train_text)
print(tok[5:15])