import PyPDF2

def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

file_path1 = "2.pdf"
file_path2 = "1.pdf"

text1 = extract_text_from_pdf(file_path1)
text2 = extract_text_from_pdf(file_path2)

# Compare and create translation dataset
# Here we assume that text1 is in English and text2 is in Chinese
# You can adjust this based on your actual needs
translation_dataset = []
for sentence1, sentence2 in zip(text1.split('.'), text2.split('.')):
    translation_dataset.append({"en": sentence1, "zh": sentence2})

# Save the translation dataset to a file
import json

with open("translation_dataset.json", "w", encoding="utf-8") as file:
    json.dump(translation_dataset, file, ensure_ascii=False, indent=4)


