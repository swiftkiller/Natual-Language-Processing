from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text = "Hello Mr. Smith, how are you? The weather is great and python is awesome. The sky is pretty blue."

stop_words = set(stopwords.words("english"))
#print(stop_words)

words = word_tokenize(example_text)

#filtered_sentence = []
# for w in words:
# 	if w not in stop_words:
# 		filtered_sentence.append(w)

filtered_sentence = [w for w in words if not w in stop_words]

print (filtered_sentence)