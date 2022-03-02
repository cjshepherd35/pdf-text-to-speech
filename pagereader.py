import requests
from bs4 import BeautifulSoup
import PyPDF2 as pdf
import pyttsx3
import os
## the page no is irrelevant
page_no = 1

# empty string to attaach text to.
earnings_call = ''
## if using pdf from computer.

# page = '/Users/ColtonShepherd/Documents/Meta_earnings.pdf'
# file = open(page, "rb")

## if using internet pdf. must be already in the pdf link.otherwise get pdf link

page_url = 'https://s21.q4cdn.com/399680738/files/doc_financials/2021/q4/Meta-Q4-2021-Earnings-Call-Transcript.pdf'
response = requests.get(page_url)
date = "now"
madefile = "C:\\{}_{}.pdf".format(date, page_no)

if (response.status_code == 200) and ("warning" not in str(response.content)):
    print("reading page no {}".format(page_no))
    with open(madefile, "wb") as f:
        f.write((response.content))

else:
    print("could not read file")

if madefile:

    source = open(madefile, "rb")

    reader = pdf.PdfFileReader(source)
    for i in range(0,reader.numPages):

        page_i = reader.getPage(i).extractText()
        earnings_call += page_i

else:
    print("file doesn't exist")

print(earnings_call)

enginge = pyttsx3.init()
enginge.say(earnings_call)
enginge.runAndWait()

os.remove(madefile)



#######
# earningscall = ''
# for i in range(0,reader.numPages):
#     pdfdata = reader.getPage(i).extractText()
#     earningscall = earningscall + pdfdata
#
#
# enginge = pyttsx3.init()
# enginge.say(earningscall)
# enginge.runAndWait()






# language = 'en'
# speech = gTTS(text = earningscall, lang = language, slow= False)

# print("about to save speech")
# speech.save("earnings.mp3")
# print('earnings call saved ')
# os.system("start earningscall.mp3")