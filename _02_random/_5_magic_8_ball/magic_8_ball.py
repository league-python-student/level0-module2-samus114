import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3
    randvar = random.randint(0, 3)
    # If the random number is 0
    if(randvar == 0):
        # tell the user "Yes"
        messagebox.showinfo('', 'yes')
    # If the random number is 1
    elif(randvar == 1):
        # tell the user "No"
        messagebox.showerror('', 'no')
    # If the random number is 2
    elif(randvar == 2):
        # tell the user "Maybe you should ask Google?"
        messagebox.showerror('', 'maybe you should ask Google?')
    # If the random number is 3
    else:
        # write your own answer
        messagebox.showinfo('', 'not my problem')