from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rock"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better",'a'))
print(lemmatizer.lemmatize("more",'a'))
print(lemmatizer.lemmatize("pikachu"))
print(lemmatizer.lemmatize("pichu"))
