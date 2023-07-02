# Random Module Imported For randint() function
from random import randint
# tkinter GUI module imported for graphical - user - interface
from tkinter import *

name = ["Neha", "Lee", "Sam"]
verb = ["buys", "rides", "kicks", "loves", "wears"]
noun = ["lion", "bicycle", "plane", "dog", "helmet"]

def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked

def generate_sentence():
    sentence = f"{pick(name)} {pick(verb)} a {pick(noun)}\n"
    text.delete(0.0, END)
    text.insert(END, sentence)

window = Tk()
window.title("Silly Sentences Generator")

buttonA = Button(window, text="Generate Sentence", command=generate_sentence)
buttonA.pack(pady=10)

text = Text(window, width=40, height=5)
text.pack()

window.mainloop()


