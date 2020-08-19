#Pdf Voice Reader.
import PyPDF2 	#pip install pypdf2
import pyttsx3	#pip install pyttsx3

#open pdf file.
pdfobj = open('demo.pdf','rb')	#rb : Binaray Mode.	

#pdf file object.
pdfreader = PyPDF2.PdfFileReader(pdfobj)

text = ""	

#read all the page of pdf.
for pagenumber in range(pdfreader.numPages):
	page = pdfreader.getPage(pagenumber)	#get page.
	text += page.extractText()				#extract the text.

pdfobj.close()		#close the file.

print(text)

engine = pyttsx3.init()		#init the text to speech library.
engine.say(text)			#this function speak the text.
engine.runAndWait()