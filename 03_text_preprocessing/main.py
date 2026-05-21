import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = "Natural Language Processing is AMAZING! NLP helps computers understand languages easily."

# Tokenization
tokens = word_tokenize(text)

# Lowercasing
tokens = [word.lower() for word in tokens]

# Remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]

# Stopword removal
stop_words = set(stopwords.words('english'))

tokens = [word for word in tokens if word not in stop_words]

# Stemming
stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in tokens]

# Lemmatization
lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

print("Processed Tokens:")
print(tokens)

print("\nStemmed Words:")
print(stemmed_words)

print("\nLemmatized Words:")
print(lemmatized_words)