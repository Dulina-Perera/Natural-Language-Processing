# %%
import pprint

from collections import defaultdict
from gensim.corpora import Dictionary
from typing import List, Set, Tuple

# %%
# Document
document: str = "Human machine interface for lab abc computer applications"

# %%
# Corpus
with open("./resources/cognitive-analytics.clean.txt", "r") as file:
  corpus: List[str] = [line.strip() for line in file if line.strip()]

## Preprocess the corpus.
### Create a set of frequent words.
stoplist: Set[str] = set('a and for in of the to'.split())

### Lowercase each document, split it by white space and filter out stopwords.
texts: List[List[str]] = [
	[word for word in document.lower().split() if word not in stoplist]
	for document in corpus
]

### Count word frequencies.
frequency: defaultdict = defaultdict(int)
for text in texts:
  for token in text:
    frequency[token] += 1

### Only keep words that appear more than once.
processed_corpus: List[List[str]] = [
	[token for token in text if frequency[token] > 1]
	for text in texts
]

### Associate each word in the corpus with a unique integer ID.
dictionary: Dictionary = Dictionary(processed_corpus)

# %%
# Vector
bow_corpus: List[List[Tuple[int, int]]] = [dictionary.doc2bow(text) for text in processed_corpus]

# %%
