# %%
import spacy

from spacy.tokens.doc import Doc
from spacy.tokens.token import Token
from spacy.lang.en import English

# %%
nlp: English = spacy.load("en_core_web_lg")

# %%
doc: Doc = nlp("I was reading the paper.")

token: Token = doc[0]
print(token.morph)

# %%
doc: Doc = nlp("She was reading the paper.")

token: Token = doc[0]
print(token.morph)
