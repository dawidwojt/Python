from gtts import gTTS
import PyPDF2, time, webbrowser

# Locating and opening pdf file
file_to_translate = input("Please type file name that you want to convert: ")
if file_to_translate[-4:] != '.pdf': # if user did not include '.pdf', it'll be added automatically
    file_to_translate += '.pdf'
    print(file_to_translate)
    

pdf_file_obj = open(file_to_translate, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
x = pdf_reader.numPages
page_obj = pdf_reader.getPage(x - 1) # minus 1 due to a fact that python starts with 0 instead of 1
text = page_obj.extractText()
print(text) # Printing found text in the console

tts = gTTS(text)
tts.save('output.mp3')
time.sleep(2)
webbrowser.open('output.mp3')
print("File has been saved as 'output.mp3' in the current directory\n"
      "It has been also opened, so you should hear it now if your speaker is on.")
