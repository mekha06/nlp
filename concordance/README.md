# Concordance and Vocabulary Analysis using NLTK

This project demonstrates the use of concordance and vocabulary analysis techniques using Python and the NLTK library.

The notebook explores how words are used in different contexts and how vocabulary statistics can be analyzed from a text corpus.

---

# Topics Covered

- Concordance
- Similar Words
- Common Contexts
- Vocabulary Analysis
- Lexical Diversity
- Frequency Distribution
- Frequency Graph Plotting

---

# Technologies Used

- Python
- NLTK
- Jupyter Notebook
- VS Code

---

# Project Structure

02_concordance/

├── concordance.ipynb  
├── README.md  

---

# What is Concordance?

Concordance is a method used to view the occurrences of a word along with its surrounding context in a text.

Example:

```python
text1.concordance("whale")
Why Concordance is Important

Concordance helps in:

understanding word usage
analyzing context
studying language patterns
linguistic analysis
text mining

Applications:

Search Engines
Chatbots
Language Models
Semantic Analysis
NLTK Book Corpus

The NLTK book corpus provides sample texts for analysis.

Examples:

text1 → Moby Dick
text2 → Sense and Sensibility
text3 → Genesis

Load corpus using:

from nltk.book import *
Similar Words

The similar() function displays words that appear in similar contexts.

Example:

text1.similar("whale")
Common Contexts

The common_contexts() function shows shared contexts between words.

Example:

text1.common_contexts(["whale", "sea"])
Vocabulary Analysis
Total Words
len(text1)

Returns the total number of tokens in the text.

Unique Words
len(set(text1))

Returns the number of unique words.

Lexical Diversity
len(set(text1)) / len(text1)

Lexical diversity measures vocabulary richness.

Higher value:

richer vocabulary

Lower value:

more repetitive text
Frequency Distribution

Frequency distribution counts how often words appear.

Example:

fdist = nltk.FreqDist(text1)
Most Common Words
fdist.most_common(10)

Displays the top 10 most frequent words.
Author

Mekha Sr

Computer Science Engineering (AI & ML)
NLP Beginner Guide Repository