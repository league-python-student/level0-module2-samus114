import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)


    for i in range(10):
        if (random_number == 1):
            messagebox.showinfo('', "you can do it")
        elif (random_number == 2):
            messagebox.showinfo('', "nice hair")
        elif (random_number == 3):
            messagebox.showinfo('', "cool kicks")
        elif (random_number == 4):
            messagebox.showinfo('', "well done")
        elif (random_number == 5):
            messagebox.showinfo('', 'as old people once said, you rocketh')
        random_number = random.randint(1, 5)
    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
