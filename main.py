"""
Typing speed app.
Initial release: 24.12.2021

Simple gui and console printed results.
Could be more OOP, as usual...

Installs:
pip install pynput
"""

import pynput
import random
import time
from tkinter import Tk, Label

start = 0
counter = 0
mistakes = 0
string = ''
NO_OF_WORDS = 20


words = ['some', 'random', 'english', 'words', 'that', 'can', 'be', 'used', 'to', 'measure', 'typing', 'speed', 'home',
         'christmas', 'airplane', 'flight', 'elevator', 'girl', 'wife', 'clothes', 'food', 'computer', 'tree', 'car',
         'greed', 'money', 'bitcoin', 'excavation', 'museum', 'travel', 'beach', 'palm', 'sand', 'dog', 'cat', 'soap',
         'dinosaurs', 'chair', 'table', 'fork', 'spoon', 'stairway', 'mammal', 'jungle', 'birds', 'entertain', 'bike']

# make a string of words
for _ in range(NO_OF_WORDS):
    string += random.choice(words)
    if _ == NO_OF_WORDS-1:
        break
    string += ' '


text_left = ''
text_middle = string[0]
text_right = string[1:]
print(string)


def on_press(key):
    global counter, mistakes, start
    if counter == 0:
        # start timer
        start = time.time()
    try:
        # check if alphanumeric character
        if key.char == string[counter]:
            print(key.char, end='')
            color = 'green'
        else:
            mistakes += 1
            print('*', end='')
            color = 'red'
    except AttributeError:
        # check if space
        if str(key)[4:] == 'space' and string[counter] == ' ':
            print(' ', end='')
            color = 'green'
        else:
            mistakes += 1
            print('*', end='')
            color = 'red'
    if counter == len(string)-1:
        # check if end, if so - show stats
        print('\n END')
        timer = time.time() - start
        print('\n', timer, " seconds")
        print(f"Characters: {len(string)}")
        print(f"Characters per second: {round(len(string) / timer)}")
        print(f"Mistakes: {mistakes}")
        return False
    counter += 1
    left_label.config(text=string[:counter])
    middle_label.config(text=string[counter], fg=color)
    right_label.config(text=string[counter+1:])



def on_release(key):
    pass


window = Tk()
window.title("Measure your typing speed")
window.config(padx=50, pady=50, bg='#FAEDF0')
window.geometry("1000x150")

# Text
left_label = Label(text=text_left, fg='black', bg='#FAEDF0', font=("Courier", 35, "bold"))
left_label.place(x=470, y=29, anchor='e',)
middle_label = Label(text=text_middle, fg='black', bg='#FAEDF0', font=("Courier", 35, "bold"))
middle_label.place(x=470, y=0)
right_label = Label(text=text_right, fg='black', bg='#FAEDF0', font=("Courier", 35, "bold"))
right_label.place(x=500, y=0)

# Start listener
listener = pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
listener.start()

window.mainloop()