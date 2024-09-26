# %%
import mimetypes
import pymupdf
import os

from pathlib import Path
from typing import Union

# %%
def convert_pdf_to_txt(
	pdf_path: str,
	output_dir: str
) -> None:
	# Check if the path exists and is a file.
	if os.path.exists(pdf_path) and os.path.isfile(pdf_path):
		# Check if the file extension is '.pdf'.
		if pdf_path.lower().endswith(".pdf"):
			# Confirm the MIME type is 'application/pdf'.
			mime_type: Union[str, None]
			mime_type, _ = mimetypes.guess_type(pdf_path)
			if mime_type == "application/pdf":
				# Open the PDF file, read through each page, and extract the text content.
				with pymupdf.open(pdf_path) as pdf_file:
					txt_content: str = ""
					for page in pdf_file:
						txt_content += page.get_text() + "\n"

				# If the output directory does not exist, create it.
				if not os.path.exists(output_dir):
					os.makedirs(output_dir)

				# Write the plain text content to a file.
				txt_path: str = os.path.join(output_dir, Path(pdf_path).stem + ".txt")
				Path(txt_path).write_text(txt_content)

				print(f"Plain text content extracted and saved to '{txt_path}'.")
			else:
				raise ValueError(f"File '{pdf_path}' is not a PDF file.")
		else:
			raise ValueError(f"File '{pdf_path}' is not a PDF file.")
	else:
		raise FileNotFoundError(f"File '{pdf_path}' does not exist.")

# %%
if __name__ == "__main__":
	convert_pdf_to_txt(
		pdf_path="./resources/cognitive-analytics.pdf",
		output_dir="./resources"
	)
