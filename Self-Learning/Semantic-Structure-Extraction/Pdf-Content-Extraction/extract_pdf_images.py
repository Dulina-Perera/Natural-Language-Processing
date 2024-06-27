# %%
import io
import pymupdf

from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from PIL.PngImagePlugin import PngImageFile
import os

# %%
pdf: pymupdf.Document = pymupdf.open("Slides.pdf")

for i in range(pdf.page_count):
    page: pymupdf.Page = pdf[i]
    
    img_lst: list[tuple[int, int, int, int, int, str, str, str, str, int]] = page.get_images(full=True)
    if img_lst:
        os.makedirs(f"Images/Page_{i}", exist_ok=True)
    for img in img_lst:
        base_img: dict[str, int | str] = pdf.extract_image(img[0])

        to_save: JpegImageFile | PngImageFile = Image.open(io.BytesIO(base_img["image"]))
        ext: str = base_img["ext"]
        to_save.save(f"Images/Page_{i}/{img[7].lower()}.{ext}", ext)
