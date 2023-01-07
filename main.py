import pyttsx3
import PyPDF2


book=open("C:/Users/HP/Downloads/CSD SYLLABUS (1).pdf","rb")
pdf=PyPDF2.PdfReader(book)
pages=len(pdf.pages)
# print(pages)



for i in range(1,pages):
    # page=pdf.getPage(i)
    page=pdf.pages[i]
    text=page.extract_text()

    speaker=pyttsx3.init()
    # book="hello how are you, well. fine"
    speaker.setProperty('rate',180)
    voice=speaker.getProperty('voices')
    speaker.setProperty('voice',voice[1].id)
    speaker.say(text)
    speaker.runAndWait()