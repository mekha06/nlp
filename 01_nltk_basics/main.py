from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist


text=input("Enter text : ")

sent_tokens=sent_tokenize(text)
print("The sentence tokens are:" , sent_tokens)

tokens=word_tokenize(text)
print("The tokens are:" , tokens)

stop_words=set(stopwords.words("english"))

filtered=[]

for words in tokens:
    if words not in stop_words:
        filtered.append(words)
print("the filtered tokens are:",filtered)

flist=FreqDist(filtered)
print("the frequency list of tokens are:",flist)
print(flist.most_common(3))
