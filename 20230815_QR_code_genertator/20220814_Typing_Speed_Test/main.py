from tkinter import *
import os
import random
import math

FONT_TYPE = "Courier"
BG_COLOR = "#206A5D"
FG_COLOR = "#EBECF1"
WARNING_COLOR = "#F05454"
user_words = []
is_correct = []
previous_len = 0
curr_word = 0
word_start = 0
word_end = 30
underline = "\u0332"


# Getting random text from .txt files.
def getting_text():
    text_file = random.choice(os.listdir("texts"))
    global the_text
    the_text = []
    with open(f"texts/{text_file}") as f:
        for word in f.read().split():
            the_text.append(word)


# Preparing text into format needed in the pop-up.
def display_text(start_index, stop_index):
    a = 1
    output = ""
    the_text_loop = the_text[start_index : stop_index]
    for word in the_text_loop:
        if curr_word < 10 and curr_word == a -1:
            output += underline + word
        elif curr_word >= 10 and (curr_word - math.floor(curr_word/10)*10) == a - 1:
            output += underline + word
        else:
            output += word
        if a % 10 == 0:
            output += "\n"
        else:
            output += " "
        a += 1
    canvas.itemconfig(word_show, text=output)


# Finding user's input and storing it into a table.
def user_input(event):
    global word_start, word_end, previous_len, curr_word
    user_words.append((entry_box.get())[previous_len:].strip())
    previous_len = len(entry_box.get())
    curr_word += 1
    if len(user_words) % 10 == 0 and len(user_words) > 0:
        word_start += 10
        word_end += 10
        entry_box.delete(0, "end")
    display_text(word_start, word_end)


# Timer
def timer_mech(count):
    if count > 0:
        window.after_id = window.after(1000, timer_mech, count - 1)
    else:
        window.after_id = None
    if count < 10:
        count = f"0{count}"
        timer.config(font=(18), fg=WARNING_COLOR)
    if count == "00":
        compare()
        window.bind("<Return>", playing)
    timer.config(text=f"{count}", font=(16))


# Starting the timer.
def start_timer():
    if window.after_id is not None:
        window.after_cancel(window.after_id)
    timer_mech(60)


# Triggering the same.
def playing(event):
    global user_words
    user_words = []
    entry_box.config(state="normal")
    getting_text()
    start_timer()
    display_text(word_start, word_end)
    window.unbind("<Return>")


# Comparing results.
def compare():
    the_index = 0
    words_correct = 0
    entry_box.config(state="disabled")
    for i in user_words:
        if the_index < 5:
            l = 0
        else:
            l = the_index - 5
        if i in the_text[l : the_index + 5]:
            words_correct += 1
        the_index += 1
    canvas.itemconfig(word_show, text=f"TIME'S UP! \n Your score is {words_correct} words per minute.\n"
                                      f"Exit to see it word by word.")


# Main window settings.
window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.after_id = None
canvas = Canvas(window, width=700, height=300, bg=BG_COLOR, highlightthickness=0)

word_show = canvas.create_text(350, 150,
                               text="This is a Machine that tests your typing speed\n"
                                    "You will have 60 seconds to type as many words as possible\n"
                                    "You need to be careful, watch if the letter is lower or uppercase, type commas "
                                    "and dots.\n\n\n "
                                    "CLICK ENTER TO START",
                               font=(FONT_TYPE, 12, "bold"), fill="white", justify="center", width=680)
canvas.grid(row=2, column=1, columnspan=6)

timer = Label(text="Timer...", font=(FONT_TYPE, 12), fg=FG_COLOR, bg=BG_COLOR)
timer.place(relx=0.45, rely=0)

entry_box = Entry(window, bg=FG_COLOR, bd=0, font=(FONT_TYPE, 12), justify="left", width=55)
entry_box.focus()
entry_box.place(relx=0.10, rely=0.8)
window.bind("<space>", user_input)
window.bind("<Return>", playing)

window.mainloop()


# Listing more info about the result in the console, after closing the window.
for i in range(0, len(user_words)):
    if user_words[i] == the_text[i]:
        is_correct.append("YES")
    else:
        is_correct.append("NO")
print(f"Sample text: {the_text[0:len(user_words)]}")
print(f"Your text:   {user_words}")
print(f"Correct?     {is_correct}")

