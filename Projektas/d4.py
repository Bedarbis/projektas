from tkinter import *
from random import randrange

class DiceRoller:
    def __init__(self, master):
        self.master = master
        self.master.geometry("750x250")
        self.master.title("Welcome to the Dice Roller. May the odds be ever in your favor")

        # Create a label to display the result
        self.result_label = Label(self.master, text="", font=("Comic Sans", 16), height=5, width=30)
        self.result_label.pack(pady=20)

        # Create buttons for each type of die
        self.create_buttons()

    def create_buttons(self):
        # Buttons for each type of dice
        Button(self.master, text="Die 4", command=self.click_d4, font=("Comic Sans", 20)).place(x=30, y=30)
        Button(self.master, text="Die 6", command=self.click_d6, font=("Comic Sans", 20)).place(x=120, y=30)
        Button(self.master, text="Die 8", command=self.click_d8, font=("Comic Sans", 20)).place(x=210, y=30)
        Button(self.master, text="Die 10", command=self.click_d10, font=("Comic Sans", 20)).place(x=300, y=30)
        Button(self.master, text="Die 12", command=self.click_d12, font=("Comic Sans", 20)).place(x=405, y=30)
        Button(self.master, text="Die 20", command=self.click_d20, font=("Comic Sans", 20)).place(x=510, y=30)
        Button(self.master, text="Die 100", command=self.click_d100, font=("Comic Sans", 20)).place(x=615, y=30)

    def click_d4(self):
        self.roll_dice(4)

    def click_d6(self):
        self.roll_dice(6)

    def click_d8(self):
        self.roll_dice(8)

    def click_d10(self):
        self.roll_dice(10)

    def click_d12(self):
        self.roll_dice(12)

    def click_d20(self):
        self.roll_dice(20)

    def click_d100(self):
        self.roll_dice(100)

    def roll_dice(self, sides):
        # Roll the dice with the given number of sides
        result = randrange(1, sides + 1)
        result_text = f"You rolled {result}\n"
        
        # Determine the outcome
        if result == sides:
            result_text += "You are very lucky"
        elif result >= 2:
            result_text += "Not bad"
        else:
            result_text += "Bad luck"
        
        # Update the label with the result
        self.result_label.config(text=result_text)

# Create the main application window
root = Tk()

# Instantiate the DiceRoller class
dice_roller = DiceRoller(root)

# Start the Tkinter event loop
root.mainloop()