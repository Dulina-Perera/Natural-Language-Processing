# %%
import spacy

from spacy import displacy
from spacy.tokens.doc import Doc
from spacy.lang.en import English

# %%
nlp: English = spacy.load("en_core_web_lg")
doc: Doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# %%
for token in doc:
  print(
		token.text,
		token.lemma_,
		token.pos_,
		token.tag_,
		token.dep_,
		token.shape_,
		token.is_alpha,
		token.is_stop
	)
displacy.serve(doc, style="dep")

# %%
