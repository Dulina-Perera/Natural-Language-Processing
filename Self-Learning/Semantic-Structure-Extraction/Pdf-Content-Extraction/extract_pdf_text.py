# %%
from pdfminer.high_level import extract_pages, extract_text

# %%
for page_layout in extract_pages("Slides.pdf"):
    for element in page_layout:
        print(element)

# %%
text: str = extract_text("Slides.pdf")
print(text)

# %%
