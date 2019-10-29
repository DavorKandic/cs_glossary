#My Glossary Project

from tkinter import *

#key down function
def click():
    entered_text=textentry.get() #this will collect text from text entry box
    output.delete(0.0, END)
    try:
        definition = my_csdict[entered_text.lower()]
    except:
        definition = 'Sorry, there is no word like that, please try again.'
    output.insert(END,definition)


##### main:
window = Tk()
window.title("My Computer Science Glossary")
window.configure(bg='black')
##### My Photo
photo1 = PhotoImage(file="pygif.gif")
Label(window, image=photo1, bg='black').grid(row=0, column=0, sticky=E)
#create label
Label(window, text='Enter the word you would like definition for:', bg='black',
      fg='white', font='None 12 bold').grid(row=1, column=0, sticky=W)
#create a text-entry box
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)
#add a submit button
Button(window, text='SUBMIT', width=6, command=click).grid(row=3, column=0,
       sticky=W)
#create another label
Label(window, text='\nDefinition:', bg='black', fg='white',
      font='none 12 bold').grid(row=4, column=0, sticky=W)
#create a display-text box
output = Text(window, width=75, height=6, wrap=WORD, bg='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)
#exit label
Label(window, text='click to exit:', bg='black', fg='white', font='none 12 bold').grid(
    row=6, column=0, sticky=W)
#add a exit button
Button(window, text='Exit', width=14, command=window.destroy).grid(row=7,
       column=0, sticky=W)
#starting size of window
window.geometry('600x400')
#the dictionary
my_csdict = {
    'algorithm': 'Step by step instructions to complete a task',
    'aplication': 'Set of codes designed to allow specific task to happen',
    'api': 'Application Programming Interface, platform used by a program to acess different services on the computer system',
    'array': 'similar data saved on a computer system in a squential form',
    'binary': 'base 2 number system',
    'bit': 'Binary Digit, it can be either a 0 or a 1',
    'boolean': 'An expression, the value of which is either true or false',
    'bug': 'a piece of code that causes program to fail',
    'bus': 'Set of wires that enables flow of data from one location of the computer to another',
    'byte': 'Eight bits is equal to one byte',
    'concatenation': 'joining two strings together',
    'conditional': 'an if-statement',
    'decimal': 'base 10 number system',
    'dequeue': 'double-ended queue',
    'dom': 'Document Object Model - tree-like model of HTML document',
    'expression': 'Anything that has a value',
    'hexadecimal': 'base 16 number system',
    'list': 'Linked list is a linear collection of data elements where each element points to the next item\'s location',
    'nesting': 'putting stuff inside other stuff',
    'octal': 'base 8 number system',
    'pointer': 'special type of variable that holds memory address of other variable in C',
    'pop': 'deleting last element from the stack',
    'pixel': 'Picture Element, one point within an image',
    'protocol': 'Set of rules that are followed by two devices while interacting with each other',
    'recursion': 'Approach to solving problems using a function that calls itself as a subroutine',
    'string': 'A sequence of characters',
    'statement': 'line of code',
    'syntax': 'Grammar defining a programming language',
    }

#####run the main loop
window.mainloop()

