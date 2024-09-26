# %%
import spacy

from spacy.lang.en import English
from spacy.matcher import Matcher
from spacy.tokens.doc import Doc
from spacy.tokens.span import Span

from typing import Any, Dict, List, Tuple

# %%
nlp: English = spacy.load("en_core_web_lg")
matcher: Matcher = Matcher(nlp.vocab)

pattern: List[Dict[str, Any]] = [
	{"LOWER": "hello"},
	{"IS_PUNCT": True, "OP": "?"},
	{"LOWER": "world"},
	{"LOWER": "!", "OP": "?"}
]
matcher.add("HelloWorld", [pattern])

# %%
doc: Doc = nlp("Hello, world! Hello world!")
matches: List[Tuple[int, int, int]] = matcher(doc)
for (match_id, start, end) in matches:
  string_id: str = nlp.vocab.strings[match_id]
  span: Span = doc[start:end]
  print(match_id, string_id, start, end, span.text)
