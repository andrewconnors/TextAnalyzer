from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import operator
def convert_pdf_to_txt(path):
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

def getWordCount(text, numWords):
    words = text.split()
    wordCount = {}

    for i,word in enumerate(words):
        key = words[i]
        for j in range(numWords-1):
            if(i<len(words)-numWords):
                key += '-' + words[i+(j+1)]
        if(key in wordCount):
            wordCount[key] += 1
        else:
            wordCount[key] = 1
    return wordCount

def getTuples(text):
    words = text.split()
    wordCount = {}

    for word in words:
        if(word in wordCount):
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount



x = getWordCount(convert_pdf_to_txt('test-cases/animal_farm.pdf'),6)
print "Top 5 words used: "
for i in sorted(x, key=x.get, reverse=True)[0:5]:
    print i, x[i]
