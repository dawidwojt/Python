#Text to Morse code converter


#Letters Dictionary
code_legend = {    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
            'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
            'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.','o':'---',
            'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
            'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
            'y':'-.--', 'z':'--..',
            '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....',
            '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----',
            ', ':'--..--', '.':'.-.-.-', '?':'..--..','/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}

print("THIS IS A TEXT TO MORSE CODE CONVERTER.")
the_end = False

def converter():
    print("You can use these characters, upper and/or lowercase: \n"
          "'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' \n"
          "'1', '2', '3', '4', '5', '6', '7', '8', '9', '0' \n"
          "',', '.', '?', '/', '-', '(', ')'")
    print("Type your message:")
    text = input()
    text_list = text.split()
    text = text.lower()
    text_morse = []
    word_index = 0
    for mark in text:
        if mark not in code_legend.keys() and mark != " ": # Checking for unsupported characters.
            print("Wrong character provided.")
        else:
            if mark != " ":
                text_morse.append(code_legend[mark])
            else:
                print(f"{text_list[word_index]}: {text_morse}")  # returning each word in a separate line.
                text_morse.clear()
                word_index += 1
        print(f"{text_list[word_index]}: {text_morse}") # returning last word.
    if input("Do you want to translate a message? YES/NO  ").upper() == "NO":
        the_end = True


while the_end != True:
    converter()
