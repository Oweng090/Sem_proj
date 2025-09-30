"""
  Name: GIU_Dice_Roller
  Created by: Owen Graham
  Created: 
  Purpose: Roll a dice as its own little Gui window
"""

# import tkinter for the Gui
import tkinter as tk
import random

#Create the individual window.
root = tk.Tk()

# making label.
label = tk.Label(root, text="Dice Roll!", bg='grey', font=("Arial", 14)) # Title
label.pack(pady=20)


total_label = tk.Label(root, text="Total: ", bg='grey', font=("Arial", 14)) # label for the total of the rolls.
total_label.pack(pady=20)
# Make an area to make squares for the dice and the dots

rollZone = tk.Canvas(root, width=300, height=150, bg="blue", highlightthickness=2.5, highlightbackground="lime") 
rollZone.pack()
rollZone.place(x=50, y=75)

# Make the squares for the dice
Dice1 = rollZone.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")# Squares for the dice
Dice2 = rollZone.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")

# Dots to sart with and for the 1 on the dice
left_dot1 = rollZone.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black") # needs centered.
right_dot1 = rollZone.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black") 
# TODO create each dice face with dots for the left dice (they will be for future use)
left_dot2 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
left_dot3 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black") # the idea here is to move them out of sight then move them into sight when needed
left_dot4 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
left_dot5 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
left_dot6 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
# TODO create each dice face for the right dice (Currently thinking of making each face and making them white or invisible for now.)
right_dot2 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
right_dot3 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
right_dot4 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
right_dot5 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
right_dot6 = rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
# Button(s)
roll_Button = tk.Button(root, text="Roll Dice", bg='lime', width=20, command=lambda: roll_dice("Roll!")) # defining a button for the GUI
roll_Button.place(x=125, y=250) # making it so the program displays the button where i need it.
theme_button = tk.Button(root, text="Theme 1", bg="#3E3E3E",fg="#FFFFFF", width=20, command=lambda: theme_1())
theme_button.place(x=125, y=285)

root.title("Dice!")
root.geometry("400x400") # temporary window sizeot
root.configure(bg='grey')
# create a function for the dice rolling
def roll_dice(side):
    sides = [1, 2, 3, 4, 5, 6]
    side = random.choice(sides) 
    # first dice rolling decision matrix
    if (side == 1):  # Note: maybe build each dice face for each if scenario ( if side = 1 then build the dice with one dot.)
        # the side will be 1
        rollZone.coords(left_dot1, 68.75, 64.75, 93.75, 89.75) # middle
        rollZone.coords(left_dot2, 0, 0, 0, 0) # moving every dot back to 0s so when you roll multiple times it can still show one.
        rollZone.coords(left_dot3, 0, 0, 0, 0)
        rollZone.coords(left_dot4, 0, 0, 0, 0)
        rollZone.coords(left_dot5, 0, 0, 0, 0)
        rollZone.coords(left_dot6, 0, 0, 0, 0)
    elif(side == 2): # make some bug prevention ( move things to their original spot or to 0,0,0,0) (for when it goes froma high number to a low number.)
        # the side will be 2
        # Need to move left_dot2 and left_dot1 to show a classic 2 on the dice face
        rollZone.coords(left_dot1, 25.75, 110.25, 50.75, 135.25) # for proportions have x1 and x2 25 apart and the same for y1 and 2
        rollZone.coords(left_dot2, 113.75, 24.25, 138.75, 49.25)
        rollZone.coords(left_dot3, 0, 0, 0, 0)
        rollZone.coords(left_dot4, 0, 0, 0, 0)
        rollZone.coords(left_dot5, 0, 0, 0, 0)
        rollZone.coords(left_dot6, 0, 0, 0, 0)
    elif(side == 3):
        # the side will be 3
        rollZone.coords(left_dot1, 68.75, 64.75, 93.75, 89.75)
        rollZone.coords(left_dot2, 25.75, 110.25, 50.75, 135.25)
        rollZone.coords(left_dot3, 113.75, 24.25, 138.75, 49.25)
        rollZone.coords(left_dot4, 0, 0, 0, 0)
        rollZone.coords(left_dot5, 0, 0, 0, 0)
        rollZone.coords(left_dot6, 0, 0, 0, 0)
    elif(side == 4):
        #the side will be 4
        rollZone.coords(left_dot1, 25.75, 110.25, 50.75, 135.25) # bottom left
        rollZone.coords(left_dot2, 113.75, 24.25, 138.75, 49.25) # top right
        rollZone.coords(left_dot3, 113.75, 110.25, 138.75, 135.25) # bottom right
        rollZone.coords(left_dot4, 25.75, 24.25, 50.75, 49.25) # top left
        rollZone.coords(left_dot5, 0, 0, 0, 0)
        rollZone.coords(left_dot6, 0, 0, 0, 0)
    elif(side == 5):
        # the side will be 5
        rollZone.coords(left_dot1, 25.75, 110.25, 50.75, 135.25) # bottom left
        rollZone.coords(left_dot2, 113.75, 24.25, 138.75, 49.25) # top right
        rollZone.coords(left_dot3, 113.75, 110.25, 138.75, 135.25) # bottom right
        rollZone.coords(left_dot4, 25.75, 24.25, 50.75, 49.25) # top left
        rollZone.coords(left_dot5, 68.75, 64.75, 93.75, 89.75) # middle
        rollZone.coords(left_dot6, 0, 0, 0, 0)
    else:
        # the side will be 6
        rollZone.coords(left_dot1, 25.75, 110.25, 50.75, 135.25) # bottom left
        rollZone.coords(left_dot2, 113.75, 24.25, 138.75, 49.25) # top right
        rollZone.coords(left_dot3, 113.75, 110.25, 138.75, 135.25) # bottom right
        rollZone.coords(left_dot4, 25.75, 24.25, 50.75, 49.25) # top left
        rollZone.coords(left_dot5, 25.75, 64.75, 50.75, 89.75) # middle left
        rollZone.coords(left_dot6, 113.75, 64.75, 138.75, 89.75) # middle right
    # second dice decision matrix
    sides2 = [1, 2, 3, 4, 5, 6]
    side2 = random.choice(sides2)

    if(side2 == 1):
        rollZone.coords(right_dot1, 220, 64.75, 245, 89.75) # middle
        rollZone.coords(right_dot2, 0, 0, 0, 0)
        rollZone.coords(right_dot3, 0, 0, 0, 0)
        rollZone.coords(right_dot4, 0, 0, 0, 0)
        rollZone.coords(right_dot5, 0, 0, 0, 0)
        rollZone.coords(right_dot6, 0, 0, 0, 0)
    elif(side2 == 2):
        rollZone.coords(right_dot1, 177, 110.25, 202, 135.25) # bottom left
        rollZone.coords(right_dot2, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(right_dot3, 0, 0, 0, 0)
        rollZone.coords(right_dot4, 0, 0, 0, 0)
        rollZone.coords(right_dot5, 0, 0, 0, 0)
        rollZone.coords(right_dot6, 0, 0, 0, 0)
    elif(side2 == 3):
        rollZone.coords(right_dot1, 177, 110.25, 202, 135.25)# bottom left
        rollZone.coords(right_dot2, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(right_dot3, 220, 64.75, 245, 89.75) # middle
        rollZone.coords(right_dot4, 0, 0, 0, 0)
        rollZone.coords(right_dot5, 0, 0, 0, 0)
        rollZone.coords(right_dot6, 0, 0, 0, 0)
    elif(side2 == 4):
        rollZone.coords(right_dot1, 177, 110.25, 202, 135.25) # bottom left
        rollZone.coords(right_dot2, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(right_dot3, 265, 110.25, 290, 135.25) # bottom right
        rollZone.coords(right_dot4, 177, 24.25, 202, 49.25) # top left
        rollZone.coords(right_dot5, 0, 0, 0, 0)
        rollZone.coords(right_dot6, 0, 0, 0, 0)
    elif(side2 == 5):
        rollZone.coords(right_dot1, 177, 110.25, 202, 135.25) # bottom left
        rollZone.coords(right_dot2, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(right_dot3, 265, 110.25, 290, 135.25) # bottom right
        rollZone.coords(right_dot4, 177, 24.25, 202, 49.25) # top left
        rollZone.coords(right_dot5, 220, 64.75, 245, 89.75) # middle 
        rollZone.coords(right_dot6, 0, 0, 0, 0)
    else:
        rollZone.coords(right_dot1, 177, 110.25, 202, 135.25) # bottom left
        rollZone.coords(right_dot2, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(right_dot3, 265, 110.25, 290, 135.25) # bottom right
        rollZone.coords(right_dot4, 177, 24.25, 202, 49.25) # top left
        rollZone.coords(right_dot5, 177, 64.75, 202, 89.75) # middle left
        rollZone.coords(right_dot6, 265, 64.75, 290, 89.75) # middle right
        
    total_roll = side + side2
    total_label.config(text=f"Total roll: {total_roll}")
    total_label.place(x=140, y=325)
# Function for the theme 1 button 
def theme_1():
    root.configure(bg="#FF0000") # Making window red
    rollZone.config(bg="#FFFB00", highlightbackground="#000000") # Making rollZone yeelow with black outline
    label.config(bg="#FF0000") # making label match backround
    total_label.config(bg="#FF0000")

root.mainloop() # this will be moved to the end of the program later.