import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)),category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]

#OR
# documents = []
# for category in movie_reviews.categories()			
# 	for fileid in movie_reviews.fileids(category)
#		documents.append(list(movie reviews.words(field)), category)
random.shuffle(documents)

#print(documents[1])

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))

print(all_words["stupid"])	
