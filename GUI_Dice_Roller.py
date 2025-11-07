"""
  Name: GIU_Dice_Roller
  Created by: Owen Graham
  Created: 
  Purpose: Roll a dice as its own little Gui window
"""

# import tkinter for the Gui
import tkinter as tk
import random
import RollLogic



#Create the individual window.
root = tk.Tk()

# TODO: Labels! ----------------------------------------------------------------------#
label = tk.Label(root, text="Dice Roll!", bg='grey', font=("Arial", 14)) # Title
label.pack(pady=20)

total_label = tk.Label(root, text=" ", bg='grey', font=("Arial", 14)) # label for the total of the rolls.
total_label.place(x=150, y=345)
total_label2 = tk.Label(root, text=" ", bg="grey", font=("Arial", 14))# Label for the second sets total
total_label3 = tk.Label(root, text=" ", bg="grey", font=("Arial", 14))
total_label4 = tk.Label(root, text=" ", bg="grey", font=("Arial", 14))
total_label5 = tk.Label(root, text=" ", bg="grey", font=("Arial", 14))

set_label = tk.Label(root, text="More Sets?", bg="grey", font=("Arial", 14))  
set_label.place(x=150, y=350)

# TODO: Dice visuals ==================================================================#
# Make an area to make squares for the dice and the dots

rollZone = tk.Canvas(root, width=300, height=150, bg="blue", highlightthickness=2.5, highlightbackground="lime") 
rollZone.pack()
rollZone.place(x=50, y=75)
rollZone2 = tk.Canvas(root, width=300, height=150, bg="blue", highlightthickness=2.5, highlightbackground="lime")
rollZone3 = tk.Canvas(root, width=300, height=150, bg="blue", highlightthickness=2.5, highlightbackground="lime")
rollZone4 = tk.Canvas(root, width=300, height=150, bg="blue", highlightthickness=2.5, highlightbackground="lime")
rollZone5 = tk.Canvas(root, width=300, height=150, bg="blue", highlightthickness=2.5, highlightbackground="lime")
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
# TODO: Make Dice and Dots for the second set of dice
# Second Set Dice Squares
set2_Dice1 = rollZone2.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
set2_Dice2 = rollZone2.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# TODO: Second Set Dots
# All Left Dots
left2_dot1 = rollZone2.create_oval(68.75, 64.75, 93.75, 89.75, fill="Black", outline="black")
left2_dot2 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
left2_dot3 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
left2_dot4 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
left2_dot5 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
left2_dot6 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
# All Right Dots
right2_dot1 = rollZone2.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
right2_dot2 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
right2_dot3 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
right2_dot4 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
right2_dot5 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
right2_dot6 = rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
# Set 3 dice
set3_dice1 = rollZone3.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
set3_dice2 = rollZone3.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# set 3 dots
left3_dot1 = rollZone3.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black")
left3_dot2 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
left3_dot3 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
left3_dot4 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
left3_dot5 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
left3_dot6 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
# right dots
right3_dot1 = rollZone3.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
right3_dot2 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
right3_dot3 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
right3_dot4 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
right3_dot5 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
right3_dot6 = rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
# Set 4
set4_dice1 = rollZone4.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
set4_dice2 = rollZone4.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# Set 4 dots (Left)
left4_dot1 = rollZone4.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black")
left4_dot2 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
left4_dot3 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
left4_dot4 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
left4_dot5 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
left4_dot6 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
# Set 4 dots (Right)
right4_dot1 = rollZone4.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
right4_dot2 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
right4_dot3 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
right4_dot4 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
right4_dot5 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
right4_dot6 = rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
# Set 5 squares
set5_dice1 = rollZone5.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
set5_dice2 = rollZone5.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# Set 5 dots left
left5_dot1 = rollZone5.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black")
left5_dot2 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
left5_dot3 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
left5_dot4 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
left5_dot5 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
left5_dot6 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
# Set 5 right dots
right5_dot1 = rollZone5.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
right5_dot2 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
right5_dot3 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
right5_dot4 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
right5_dot5 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
right5_dot6 = rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
# TODO: Buttons ====================================================================#
# Roll Buttons
roll_Button = tk.Button(root, text="Roll Dice", bg='lime', width=20, command=lambda: roll_dice("Roll!")) # defining a button for the GUI
roll_Button.place(x=125, y=250) # making it so the program displays the button where i need it.
# Theme Buttons
theme_button = tk.Button(root, text="Theme 1", bg="#3E3E3E",fg="#FFFFFF", width=20, command=lambda: theme_1())
theme_button.place(x=25, y=285)
theme_button2 = tk.Button(root, text="Theme 2", bg="#3E3E3E", fg="#FFFFFF", width=20, command=lambda: theme_2())
theme_button2.place(x=225, y=285)
# Set Buttons
set_button1 = tk.Button(root, text="1 Set", bg="lime", width=20, command=lambda: set1())
set_button1.place(x=125, y=385)
set_button2 = tk.Button(root, text="2 Sets", bg="lime", width=20, command=lambda: set2())
set_button2.place(x=125, y=415)
set_button3 = tk.Button(root, text="3 Sets", bg="lime", width=20, command=lambda: set3())
set_button3.place(x=125, y=445)
set_button4 = tk.Button(root, text="4 Sets", bg="lime", width=20, command=lambda: set4())
set_button4.place(x=125, y=475)
set_button5 = tk.Button(root, text="5 Sets", bg="lime", width=20, command=lambda: set5())
set_button5.place(x=125, y=505)
#===================================================================================#
root.title("Dice!")
root.geometry("400x575")
root.configure(bg='grey')
# create a function for the dice rolling
def roll_dice(side):
    # Set 1
    sides = [1, 2, 3, 4, 5, 6]
    side = random.choice(sides)
    RollLogic.rollLogic(side, rollZone, left_dot1, left_dot2, left_dot3, left_dot4, left_dot5, left_dot6)
    side2 = random.choice(sides)
    RollLogic.rollLogic2(side2, rollZone, right_dot1, right_dot2, right_dot3, right_dot4, right_dot5, right_dot6)

    # Set 2
    set2_side1 = random.choice(sides)
    set2_side2 = random.choice(sides)
    RollLogic.rollLogic(set2_side1, rollZone2, left2_dot1, left2_dot2, left2_dot3, left2_dot4, left2_dot5, left2_dot6)
    RollLogic.rollLogic2(set2_side2, rollZone2, right2_dot1, right2_dot2, right2_dot3, right2_dot4, right2_dot5, right2_dot6) 

    # Set 3
    set3_side = random.choice(sides)
    set3_side2 = random.choice(sides)
    RollLogic.rollLogic(set3_side, rollZone3, left3_dot1, left3_dot2, left3_dot3, left3_dot4, left3_dot5, left3_dot6)
    RollLogic.rollLogic2(set3_side2, rollZone3, right3_dot1, right3_dot2, right3_dot3, right3_dot4, right3_dot5, right3_dot6)
    # Set 4
    set4_side1 = random.choice(sides)
    set4_side2 = random.choice(sides)

    RollLogic.rollLogic(set4_side1, rollZone4, left4_dot1, left4_dot2, left4_dot3, left4_dot4, left4_dot5, left4_dot6)
    RollLogic.rollLogic2(set4_side2, rollZone4, right4_dot1, right4_dot2, right4_dot3, right4_dot4, right4_dot5, right4_dot6)

    set5_side1 = random.choice(sides)
    set5_side2 = random.choice(sides)

    RollLogic.rollLogic(set5_side1, rollZone5, left5_dot1, left5_dot2, left5_dot3, left5_dot4, left5_dot5, left5_dot6)
    RollLogic.rollLogic2(set5_side2, rollZone5, right5_dot1, right5_dot2, right5_dot3, right5_dot4, right5_dot5, right5_dot6)

    total_roll = side + side2
    total_label.config(text=f"Total roll: {total_roll}")
    total_roll2 = set2_side1 + set2_side2
    total_label2.config(text=f"Total roll: {total_roll2}")
    total_roll3 = set3_side + set3_side2
    total_label3.config(text=f"Total roll: {total_roll3}")
    total_roll4 = set4_side1 + set4_side2
    total_label4.config(text=f"Total roll: {total_roll4}")
    total_roll5 = set5_side1 + set5_side2
    total_label5.config(text=f"Total roll: {total_roll5}")
# Function for the theme 1 button 
def theme_1():
    root.configure(bg="#FF0000") # Making window red
    rollZone.config(bg="#FFFB00", highlightbackground="#000000") # Making rollZones yeelow with black outline
    rollZone2.config(bg="#FFFB00", highlightbackground="#000000")
    rollZone3.config(bg="#FFFB00", highlightbackground="#000000")
    rollZone4.config(bg="#FFFB00", highlightbackground="#000000")
    label.config(bg="#FF0000") # making label match backround
    total_label.config(bg="#FF0000")
    total_label2.config(bg="#FF0000")
    total_label3.config(bg="#FF0000")
    total_label4.config(bg="#FF0000")
    set_label.config(bg="#FF0000")  
# Function for theme button 2.
def theme_2():
    root.configure(bg="#AAAAAA")
    rollZone.config(bg="#808080", highlightbackground="#000000")
    rollZone2.config(bg="#808080", highlightbackground="#000000")
    rollZone3.config(bg="#808080", highlightbackground="#000000")
    rollZone4.config(bg="#808080", highlightbackground="#000000")
    label.config(bg="#AAAAAA")
    total_label.config(bg="#AAAAAA")
    total_label2.config(bg="#AAAAAA")
    total_label3.config(bg="#AAAAAA")
    total_label4.config(bg="#AAAAAA")
    set_label.config(bg="#AAAAAA")

def set1():
    root.geometry("400x575")
    rollZone2.place_forget()
    rollZone3.place_forget()
    rollZone4.place_forget()
    rollZone5.place_forget()
    roll_Button.place(x=125, y=250)
    theme_button.place(x=25, y=285)
    theme_button2.place(x=225, y=285)
    set_button1.place(x=125, y=385)
    set_button2.place(x=125, y=415)
    set_button3.place(x=125, y=445)
    set_button4.place(x=125, y=475)
    set_button5.place(x=125, y=505)
    set_label.place(x=150, y=350)
    total_label.place(x=150, y=250)
    total_label2.place_forget()
    total_label3.place_forget()
    total_label4.place_forget()
    total_label5.place_forget()

def set2():
    root.geometry("800x575") # making window bigger for second set of dice
    rollZone2.place(x=450, y=75) # Moving the second rollzone to its place
    rollZone3.place_forget()
    rollZone4.place_forget()
    rollZone5.place_forget()
    roll_Button.place(x=325, y=250) # Moving all labels and buttons to the center of the window
    theme_button.place(x=225, y=285)
    theme_button2.place(x=425, y=285)
    set_button1.place(x=325, y=385)
    set_button2.place(x=325, y=415)
    set_button3.place(x=325, y=445)
    set_button4.place(x=325, y=475)
    set_button5.place(x=325, y=505)
    set_label.place(x=350, y=350)
    total_label.place(x=150, y=250)
    total_label2.place(x=560, y=250)
    total_label3.place_forget()
    total_label4.place_forget()
    total_label5.place_forget()
def set3():
    root.geometry("1200x575")
    rollZone2.place(x=450, y=75)  # Moving the second rollzone to its place
    rollZone3.place(x=850, y=75)
    rollZone4.place_forget() # temporarily remove roll zone 4
    rollZone5.place_forget()
    roll_Button.place(x=535, y=325) # Moving all labels and buttons to the center of the window
    theme_button.place(x=435, y=285)
    theme_button2.place(x=635, y=285)
    set_button1.place(x=535, y=385)
    set_button2.place(x=535, y=415)
    set_button3.place(x=535, y=445)
    set_button4.place(x=535, y=475)
    set_button5.place(x=535, y=505)
    set_label.place(x=550, y=350)
    total_label.place(x=150, y=250)
    total_label2.place(x=560, y=250)
    total_label3.place(x=960, y=250)
    total_label4.place_forget()
    total_label5.place_forget()
def set4():
    root.geometry("1200x575")
    rollZone2.place(x=450, y=75)
    rollZone3.place(x=850, y=75)
    rollZone4.place(x=450, y=275)
    rollZone5.place_forget()
    roll_Button.place(x=125, y=270) # Moving all labels and buttons to the center of the window
    theme_button.place(x=25, y=305)
    theme_button2.place(x=225, y=305)
    set_button1.place(x=125, y=405)
    set_button2.place(x=125, y=435)
    set_button3.place(x=125, y=465)
    set_button4.place(x=125, y=495)
    set_button5.place(x=125, y=525)
    set_label.place(x=150, y=355)
    total_label.place(x=150, y=210)
    total_label2.place(x=560, y=235)
    total_label3.place(x=960, y=235)
    total_label4.place(x=560, y=435)
    total_label5.place_forget()

def set5():
    root.geometry("1200x575")
    rollZone2.place(x=450, y=75)
    rollZone3.place(x=850, y=75)
    rollZone4.place(x=450, y=275)
    rollZone5.place(x=850, y=275)
    roll_Button.place(x=125, y=270) # Moving all labels and buttons to the center of the window
    theme_button.place(x=25, y=305)
    theme_button2.place(x=225, y=305)
    set_button1.place(x=125, y=405)
    set_button2.place(x=125, y=435)
    set_button3.place(x=125, y=465)
    set_button4.place(x=125, y=495)
    set_button5.place(x=125, y=525)
    set_label.place(x=150, y=355)
    total_label.place(x=150, y=235)
    total_label2.place(x=560, y=235)
    total_label3.place(x=960, y=235)
    total_label4.place(x=560, y=435)
    total_label5.place(x=960, y=435)

root.mainloop() 