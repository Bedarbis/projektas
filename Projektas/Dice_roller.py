from tkinter import *
from tkinter import ttk
from random import randrange


def click_d4():
    result = randrange(1, 5)
    print(f"You rolled {result}")
    if result == 4:
        print("You are very lucky")
    elif result >= 2:
        print("Not bad")
    else:
        print("Bad luck")

def click_d6():
    result = randrange(1, 7)
    print(f"You rolled {result}")
    if result == 6:
        print("You are very lucky")
    elif result >= 2:
        print("Not bad")
    else:
        print("Bad luck")

def click_d8():
    result = randrange(1, 9)
    print(f"You rolled {result}")
    if result == 8:
        print("You are very lucky")
    elif result >= 2:
        print("Not bad")
    else:
        print("Bad luck")

def click_d10():
    result = randrange(1, 11)
    print(f"You rolled {result}")
    if result == 10:
        print("You are very lucky")
    elif result >= 2:
        print("Not bad")
    else:
        print("Bad luck")

def click_d12():
    result = randrange(1, 13)
    print(f"You rolled {result}")
    if result == 12:
        print("You are very lucky")
    elif result >= 2:
        print("Not bad")
    else:
        print("Bad luck")

def click_d20():
    result = randrange(1, 21)
    print(f"You rolled {result}")
    if result == 20:
        print("You are very lucky")
    elif result >= 2:
        print("Not bad")
    else:
        print("Bad luck")

def click_d100():
    result = randrange(1, 101)
    print(f"You rolled {result}")
    if result == 100:
        print("You are very lucky")
    elif result >= 2:
        print("Not bad")
    else:
        print("Bad luck")

langas = Tk()

langas.geometry("750x250")
langas.title("Welcome to the Dice Roller. May the odds be ever in your favor")


button_d4 = Button(langas,
                text="Die 4",
                command = click_d4,
                font = ("Comic Sans", 20))
button_d4.pack()
button_d4.place(x=30, y=30)


button_d6 = Button(langas,
                text="Die 6",
                command = click_d6,
                font = ("Comic Sans", 20))
button_d6.pack()
button_d6.place(x=120, y=30)

button_d8 = Button(langas,
                text="Die 8",
                command = click_d8,
                font = ("Comic Sans", 20))
button_d8.pack()
button_d8.place(x=210, y=30)

button_d10 = Button(langas,
                text="Die 10",
                command = click_d10,
                font = ("Comic Sans", 20))
button_d10.pack()
button_d10.place(x=300, y=30)

button_d12 = Button(langas,
                text="Die 12",
                command = click_d12,
                font = ("Comic Sans", 20))
button_d12.pack()
button_d12.place(x=405, y=30)

button_d20 = Button(langas,
                text="Die 20",
                command = click_d20,
                font = ("Comic Sans", 20))
button_d20.pack()
button_d20.place(x=510, y=30)

button_d100 = Button(langas,
                text="Die 100",
                command = click_d100,
                font = ("Comic Sans", 20))
button_d100.pack()
button_d100.place(x=615, y=30)

langas.mainloop()