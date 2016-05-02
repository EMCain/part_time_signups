from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import re

# from  http://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python

def pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text
	
def txt_to_dict(fulltext):
	out_dict = {}
	vals = re.split('\n[\w,\s]+\w:', fulltext)[1:] # 0 index will be before first occurance
	keys = re.findall('\n[\w,?\s]+\w:', fulltext)

	for i in range(len(keys)):
		vals_array = re.split('[\n]+', vals[i])[1:] # first value is empty string
		ages = ['adults', 'youth', 'children']
		inner_dict = {'adults': [], 'youth': [], 'children': []}
		
		counter = 0 
		for val in vals_array:
			if counter == 3:
				counter = 0
			inner_dict[ages[counter]].append(val)
			counter +=1
		out_dict[keys[i].split("\n")[-1]] =  inner_dict # splitting on \n avoids a bunch of junk before the house names
	
	return out_dict

print("starting")
print(txt_to_dict(pdf_to_txt("rates_2016.pdf")))
print("done")