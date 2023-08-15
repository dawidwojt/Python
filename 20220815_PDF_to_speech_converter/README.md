# 20220815_PDF_to_Speech
This is a short but efficient and helpfull method to convert pdf files into speech.
Steps:
- Asking user for a filename they want to convert.
- Opening and extracting data from pdf file using PyPDF2
- Converting it into speech using Google Text to Speech (gTTS)
- Saving speech to a mp3 file in a current directory
- Opening it up automatically using webbrowser.
