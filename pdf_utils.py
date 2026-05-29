

# Day - 01
#   we will extract all the textes from pdf
#   and we will add all text in .txt file

import fitz   # import pymupdf -> (both are same)
import os

# its open the pdf and extarct the all text
def extract_text(pdf): 

    # ye check krega agar pdf nhii hoga to msg dega
    if not os.path.exists(pdf):
        print('PDF file does not exist')
        return None


    # step1: open the pdf file
    doc = fitz.open(pdf)
    all_text = []  # it store all text of pdf

    # step2: loop through every page
    for i in range (len(doc)):

        page = doc[i]  # we are getting each pages

        # tep3: extarct the text of each pages
        text = page.get_text() # extracting all text from each page
        all_text.append(text)
       
    # step4: join all pages in one big string
    full_text = "\n".join(all_text)
    return full_text

# step5: save the exctracted_text.text
def save_file(text):
    with open('extracted_text.txt', 'w') as file:
        file.write(text)
        print('All the text from each pages extracted succesfully')

# extract text
text = extract_text('sample.pdf')

# save file
save_file(text)