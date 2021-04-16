import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    num1 = random.randint(1, 1000000)
    num2 = random.randint(1, 1000000)
    num3 = random.randint(1, 1000000)
    num4 = random.randint(1, 1000000)
    num5 = random.randint(1, 1000000)
    num6 = random.randint(1, 1000000)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo('lottery ticket', str(num1) + ' \n ' + str(num2) + ' \n ' + str(num3) + ' \n ' + str(num4) + ' \n ' + str(num5) + ' \n ' + str(num6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
