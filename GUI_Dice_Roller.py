"""
  Name: GIU_Dice_Roller
  Created by: Owen Graham
  Created: 
  Purpose: Roll a dice as its own little Gui window
"""
# import tkinter for the Gui
from tkinter import *
#from tkinter.ttk import *
import random
import RollLogic
#import sv_ttk
# Fulscreen stuff
# Function to exit fullscree
#def exitFullscreen():
    #return self.root.attributes("-fullscreen", False)
# Create class
fullscreenstatus = False
root = None
class DiceRoller:
    def __init__(self):
        self.root = Tk()
        self.root.title("Dice!")
        self.root.iconbitmap("Dice.ico") # Dice icon at top of screen
        #sv_ttk.set_theme("dark")
        self.root.geometry("400x575")
        self.root.configure(background='grey')
        self.widgets()
        self.root.mainloop()
# TODO: Labels! ----------------------------------------------------------------------#
# Create widgets
    def widgets(self):
        self.label = Label(self.root, text="Dice Roll!", font=("Arial", 14), background='grey') # Title
        self.label.pack(pady=20)
        self.total_label = Label(self.root, text="Total roll: ", background='grey', font=("Arial", 14)) # label for the total of the rolls.
        self.total_label.place(x=150, y=315)
        self.total_label2 = Label(self.root, text="Total roll: ", background="grey", font=("Arial", 14))# Label for the second sets total
        self.total_label3 = Label(self.root, text="Total roll: ", background="grey", font=("Arial", 14))
        self.total_label4 = Label(self.root, text="Total roll: ", background="grey", font=("Arial", 14))
        self.total_label5 = Label(self.root, text="Total roll: ", background="grey", font=("Arial", 14))
        self.total_label6 = Label(self.root, text="Total roll: ", background="grey", font=("Arial", 14))
        #self.set_label = Label(self.root, text="More Sets?", background="grey", font=("Arial", 14))  
        #self.set_label.place(x=150, y=350)
# TODO: Dice visuals ==================================================================#
# Make an area to make squares for the dice and the dots
        self.rollZone = Canvas(self.root, width=300, height=150, background="blue", highlightthickness=2.5, highlightbackground="lime") 
        self.rollZone.pack()
        self.rollZone.place(x=50, y=75)
        self.rollZone2 = Canvas(self.root, width=300, height=150, background="blue", highlightthickness=2.5, highlightbackground="lime")
        self.rollZone3 = Canvas(self.root, width=300, height=150, background="blue", highlightthickness=2.5, highlightbackground="lime")
        self.rollZone4 = Canvas(self.root, width=300, height=150, background="blue", highlightthickness=2.5, highlightbackground="lime")
        self.rollZone5 = Canvas(self.root, width=300, height=150, background="blue", highlightthickness=2.5, highlightbackground="lime")
        self.rollZone6 = Canvas(self.root, width=300, height=150, background="blue", highlightthickness=2.5, highlightbackground="lime")
# Make the squares for the dice
        self.Dice1 = self.rollZone.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")# Squares for the dice
        self.Dice2 = self.rollZone.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# Dots to sart with and for the 1 on the dice
        self.left_dot1 = self.rollZone.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black") # needs centered.
        self.right_dot1 = self.rollZone.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black") 
# TODO create each dice face with dots for the left dice (they will be for future use)
        self.left_dot2 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left_dot3 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black") # the idea here is to move them out of sight then move them into sight when needed
        self.left_dot4 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left_dot5 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left_dot6 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
# TODO create each dice face for the right dice (Currently thinking of making each face and making them white or invisible for now.)
        self.right_dot2 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right_dot3 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right_dot4 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right_dot5 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right_dot6 = self.rollZone.create_oval(0, 0, 0, 0, fill="black", outline="black")
# TODO: Make Dice and Dots for the second set of dice
# Second Set Dice Squares
        self.set2_Dice1 = self.rollZone2.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
        self.set2_Dice2 = self.rollZone2.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# TODO: Second Set Dots
# All Left Dots
        self.left2_dot1 = self.rollZone2.create_oval(68.75, 64.75, 93.75, 89.75, fill="Black", outline="black")
        self.left2_dot2 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left2_dot3 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left2_dot4 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left2_dot5 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left2_dot6 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
# All Right Dots
        self.right2_dot1 = self.rollZone2.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
        self.right2_dot2 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right2_dot3 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right2_dot4 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right2_dot5 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right2_dot6 = self.rollZone2.create_oval(0, 0, 0, 0, fill="black", outline="black")
# Set 3 dice
        self.set3_dice1 = self.rollZone3.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
        self.set3_dice2 = self.rollZone3.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# set 3 dots
        self.left3_dot1 = self.rollZone3.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black")
        self.left3_dot2 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left3_dot3 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left3_dot4 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left3_dot5 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left3_dot6 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
# right dots
        self.right3_dot1 = self.rollZone3.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
        self.right3_dot2 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right3_dot3 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right3_dot4 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right3_dot5 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right3_dot6 = self.rollZone3.create_oval(0, 0, 0, 0, fill="black", outline="black")
# Set 4
        self.set4_dice1 = self.rollZone4.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
        self.set4_dice2 = self.rollZone4.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# Set 4 dots (Left)
        self.left4_dot1 = self.rollZone4.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black")
        self.left4_dot2 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
        self.left4_dot3 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
        self.left4_dot4 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
        self.left4_dot5 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
        self.left4_dot6 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
# Set 4 dots (Right)
        self.right4_dot1 = self.rollZone4.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
        self.right4_dot2 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
        self.right4_dot3 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
        self.right4_dot4 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
        self.right4_dot5 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
        self.right4_dot6 = self.rollZone4.create_oval(0, 0, 0, 0, fil="black", outline="black")
# Set 5 squares
        self.set5_dice1 = self.rollZone5.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
        self.set5_dice2 = self.rollZone5.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# Set 5 dots left
        self.left5_dot1 = self.rollZone5.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black")
        self.left5_dot2 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left5_dot3 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left5_dot4 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left5_dot5 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left5_dot6 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
# Set 5 right dots
        self.right5_dot1 = self.rollZone5.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
        self.right5_dot2 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right5_dot3 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right5_dot4 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right5_dot5 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right5_dot6 = self.rollZone5.create_oval(0, 0, 0, 0, fill="black", outline="black")
# set 6 dice
        self.set6_dice1 = self.rollZone6.create_rectangle(169, 20, 292.5, 140, fill="white", outline="black")
        self.set6_dice2 = self.rollZone6.create_rectangle(18.5, 20, 142.5, 140, fill="white", outline="black")
# set 6 dots
        self.left6_dot1 = self.rollZone6.create_oval(68.75, 64.75, 93.75, 89.75, fill="black", outline="black")
        self.left6_dot2 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left6_dot3 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left6_dot4 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left6_dot5 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.left6_dot6 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
# right
        self.right6_dot1 = self.rollZone6.create_oval(220, 64.75, 245, 89.75, fill="black", outline="black")
        self.right6_dot2 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right6_dot3 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right6_dot4 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right6_dot5 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
        self.right6_dot6 = self.rollZone6.create_oval(0, 0, 0, 0, fill="black", outline="black")
# TODO: Buttons ====================================================================#
# Full Screen button
        #self.fullButton = Button(self.root, text="Fullscreen Toggle", bg="blue", width=20, command=lambda: self.fullScreen())
        #self.fullButton.place(x=125, y=350)
# Roll Buttons
        self.roll_Button = Button(self.root, text="Roll Dice", bg="lime", width=20, command=lambda: self.roll_dice()) # defining a button for the GUI
        self.roll_Button.place(x=125, y=250) # making it so the program displays the button where i need it.
# Theme Buttons
        self.theme_button = Button(self.root, text="Theme 1", bg="#5A5A5A", fg="white", width=20, command=lambda: self.theme_1())
        self.theme_button.place(x=25, y=285)
        self.theme_button2 = Button(self.root, text="Theme 2",bg="#5A5A5A", fg="white", width=20, command=lambda: self.theme_2())
        self.theme_button2.place(x=225, y=285)
# Set Buttons
        self.set_button1 = Button(self.root, text="1 Set", bg="lime", width=20, command=lambda: self.set1())
        self.set_button1.place(x=125, y=385)
        self.set_button2 = Button(self.root, text="2 Sets", bg="lime", width=20, command=lambda: self.set2())
        self.set_button2.place(x=125, y=415)
        self.set_button3 = Button(self.root, text="3 Sets", bg="lime", width=20, command=lambda: self.set3())
        self.set_button3.place(x=125, y=445)
        self.set_button4 = Button(self.root, text="4 Sets", bg="lime", width=20, command=lambda: self.set4())
        self.set_button4.place(x=125, y=475)
        self.set_button5 = Button(self.root, text="5 Sets", bg="lime", width=20, command=lambda: self.set5())
        self.set_button5.place(x=125, y=505)
        self.set_button6 = Button(self.root, text="6 Sets", bg="lime", width=20, command=lambda: self.set6())
        self.set_button6.place(x=125, y=535)
        # -------- KEYBINDS -----------------#
        self.root.bind("<f>", self.fullScreen)
        self.root.bind("<Escape>", self.close)
#===================================================================================#
# create a function for the dice rolling
    def roll_dice(self):
        # Set 1
        self.sides = [1, 2, 3, 4, 5, 6]
        self.side = random.choice(self.sides)
        RollLogic.rollLogic(self.side, self.rollZone, self.left_dot1, self.left_dot2, self.left_dot3, self.left_dot4, self.left_dot5, self.left_dot6)
        self.side2 = random.choice(self.sides)
        RollLogic.rollLogic2(self.side2, self.rollZone, self.right_dot1, self.right_dot2, self.right_dot3, self.right_dot4, self.right_dot5, self.right_dot6)
        # Set 2
        self.set2_side1 = random.choice(self.sides)
        self.set2_side2 = random.choice(self.sides)
        RollLogic.rollLogic(self.set2_side1, self.rollZone2, self.left2_dot1, self.left2_dot2, self.left2_dot3, self.left2_dot4, self.left2_dot5, self.left2_dot6)
        RollLogic.rollLogic2(self.set2_side2, self.rollZone2, self.right2_dot1, self.right2_dot2, self.right2_dot3, self.right2_dot4, self.right2_dot5, self.right2_dot6) 
        # Set 3
        self.set3_side1 = random.choice(self.sides)
        self.set3_side2 = random.choice(self.sides)
        RollLogic.rollLogic(self.set3_side1, self.rollZone3, self.left3_dot1, self.left3_dot2, self.left3_dot3, self.left3_dot4, self.left3_dot5, self.left3_dot6)
        RollLogic.rollLogic2(self.set3_side2, self.rollZone3, self.right3_dot1, self.right3_dot2, self.right3_dot3, self.right3_dot4, self.right3_dot5, self.right3_dot6)
        # Set 4
        self.set4_side1 = random.choice(self.sides)
        self.set4_side2 = random.choice(self.sides)
        RollLogic.rollLogic(self.set4_side1, self.rollZone4, self.left4_dot1, self.left4_dot2, self.left4_dot3, self.left4_dot4, self.left4_dot5, self.left4_dot6)
        RollLogic.rollLogic2(self.set4_side2, self.rollZone4, self.right4_dot1, self.right4_dot2, self.right4_dot3, self.right4_dot4, self.right4_dot5, self.right4_dot6)
        # Set 5
        self.set5_side1 = random.choice(self.sides)
        self.set5_side2 = random.choice(self.sides)
        RollLogic.rollLogic(self.set5_side1, self.rollZone5, self.left5_dot1, self.left5_dot2, self.left5_dot3, self.left5_dot4, self.left5_dot5, self.left5_dot6)
        RollLogic.rollLogic2(self.set5_side2, self.rollZone5, self.right5_dot1, self.right5_dot2, self.right5_dot3, self.right5_dot4, self.right5_dot5, self.right5_dot6)
        # Set 6
        self.set6_side1 = random.choice(self.sides)
        self.set6_side2 = random.choice(self.sides)
        RollLogic.rollLogic(self.set6_side1, self.rollZone6, self.left6_dot1, self.left6_dot2, self.left6_dot3, self.left6_dot4, self.left6_dot5, self.left6_dot6)
        RollLogic.rollLogic2(self.set6_side2, self.rollZone6, self.right6_dot1, self.right6_dot2, self.right6_dot3, self.right6_dot4, self.right6_dot5, self.right6_dot6)
        # Total labels
        self.total_roll = self.side + self.side2
        self.total_label.config(text=f"Total roll: {self.total_roll}")
        self.total_roll2 = self.set2_side1 + self.set2_side2
        self.total_label2.config(text=f"Total roll: {self.total_roll2}")
        self.total_roll3 = self.set3_side1 + self.set3_side2
        self.total_label3.config(text=f"Total roll: {self.total_roll3}")
        self.total_roll4 = self.set4_side1 + self.set4_side2
        self.total_label4.config(text=f"Total roll: {self.total_roll4}")
        self.total_roll5 = self.set5_side1 + self.set5_side2
        self.total_label5.config(text=f"Total roll: {self.total_roll5}")
        self.total_roll6 = self.set6_side1 + self.set6_side2
        self.total_label6.config(text=f"Total roll: {self.total_roll6}")
    # Function for fullscreen
    def fullScreen(self, *args):
        global fullscreenstatus, root
        fullscreenstatus = not fullscreenstatus
        self.root.attributes('-fullscreen', fullscreenstatus)
    def close(self, *args):
        self.root.destroy()
    # Function for the theme 1 button 
    def theme_1(self):
        self.root.configure(background="#FF0000") # Making window red
        self.rollZone.config(background="#FFFB00", highlightbackground="#000000") # Making rollZones yeelow with black outline
        self.rollZone2.config(background="#FFFB00", highlightbackground="#000000")
        self.rollZone3.config(background="#FFFB00", highlightbackground="#000000")
        self.rollZone4.config(background="#FFFB00", highlightbackground="#000000")
        self.rollZone5.config(background="#FFFB00", highlightbackground="#000000")
        self.rollZone6.config(background="#FFFB00", highlightbackground="#000000")
        self.label.config(background="#FF0000") # making label match backround
        self.total_label.config(background="#FF0000")
        self.total_label2.config(background="#FF0000")
        self.total_label3.config(background="#FF0000")
        self.total_label4.config(background="#FF0000")
        self.total_label5.config(background="#FF0000")
        #total_label6.config(background=="#FF0000")
        #self.set_label.config(background="#FF0000")  
    # Function for theme button 2.
    def theme_2(self):
        self.root.configure(background="#AAAAAA")
        self.rollZone.config(background="#808080", highlightbackground="#000000")
        self.rollZone2.config(background="#808080", highlightbackground="#000000")
        self.rollZone3.config(background="#808080", highlightbackground="#000000")
        self.rollZone4.config(background="#808080", highlightbackground="#000000")
        self.rollZone5.config(background="#808080", highlightbackground="#000000")
        self.rollZone6.config(background="#808080", highlightbackground="#000000")
        self.label.config(background="#AAAAAA")
        self.total_label.config(background="#AAAAAA")
        self.total_label2.config(background="#AAAAAA")
        self.total_label3.config(background="#AAAAAA")
        self.total_label4.config(background="#AAAAAA")
        self.total_label5.config(background="#AAAAAA")
        #self.set_label.config(background="#AAAAAA")
    def set1(self):
        self.root.geometry("400x575")
        self.rollZone2.place_forget()
        self.rollZone3.place_forget()
        self.rollZone4.place_forget()
        self.rollZone5.place_forget()
        self.rollZone6.place_forget()
        self.roll_Button.place(x=125, y=250)
        self.theme_button.place(x=25, y=285)
        self.theme_button2.place(x=225, y=285)
        self.set_button1.place(x=125, y=385)
        self.set_button2.place(x=125, y=415)
        self.set_button3.place(x=125, y=445)
        self.set_button4.place(x=125, y=475)
        self.set_button5.place(x=125, y=505)
        self.set_button6.place(x=125, y=535)
        #self.set_label.place(x=150, y=350)
        self.total_label.place(x=150, y=315)
        self.total_label2.place_forget()
        self.total_label3.place_forget()
        self.total_label4.place_forget()
        self.total_label5.place_forget()
        self.total_label6.place_forget()
    def set2(self):
        self.root.geometry("800x575") # making window bigger for second set of dice
        self.rollZone2.place(x=450, y=75) # Moving the second rollzone to its place
        self.rollZone3.place_forget()
        self.rollZone4.place_forget()
        self.rollZone5.place_forget()
        self.rollZone6.place_forget()
        self.roll_Button.place(x=325, y=250) # Moving all labels and buttons to the center of the window
        self.theme_button.place(x=225, y=285)
        self.theme_button2.place(x=425, y=285)
        self.set_button1.place(x=325, y=385)
        self.set_button2.place(x=325, y=415)
        self.set_button3.place(x=325, y=445)
        self.set_button4.place(x=325, y=475)
        self.set_button5.place(x=325, y=505)
        self.set_button6.place(x=325, y=535)
        #self.set_label.place(x=350, y=350)
        self.total_label.place(x=150, y=250)
        self.total_label2.place(x=560, y=250)
        self.total_label3.place_forget()
        self.total_label4.place_forget()
        self.total_label5.place_forget()
        self.total_label6.place_forget()
    def set3(self):
        self.root.geometry("1200x575")
        self.rollZone2.place(x=450, y=75)  # Moving the second rollzone to its place
        self.rollZone3.place(x=850, y=75)
        self.rollZone4.place_forget() # temporarily remove roll zone 4
        self.rollZone5.place_forget()
        self.rollZone6.place_forget()
        self.roll_Button.place(x=535, y=325) # Moving all labels and buttons to the center of the window
        self.theme_button.place(x=435, y=285)
        self.theme_button2.place(x=635, y=285)
        self.set_button1.place(x=535, y=385)
        self.set_button2.place(x=535, y=415)
        self.set_button3.place(x=535, y=445)
        self.set_button4.place(x=535, y=475)
        self.set_button5.place(x=535, y=505)
        self.set_button6.place(x=535, y=535)
        #self.set_label.place(x=550, y=350)
        self.total_label.place(x=150, y=250)
        self.total_label2.place(x=560, y=250)
        self.total_label3.place(x=960, y=250)
        self.total_label4.place_forget()
        self.total_label5.place_forget()
        self.total_label6.place_forget()
    def set4(self):
        self.root.geometry("1200x575")
        self.rollZone2.place(x=450, y=75)
        self.rollZone3.place(x=850, y=75)
        self.rollZone4.place(x=450, y=275)
        self.rollZone5.place_forget()
        self.rollZone6.place_forget()
        self.roll_Button.place(x=125, y=270) # Moving all labels and buttons to the center of the window
        self.theme_button.place(x=25, y=305)
        self.theme_button2.place(x=225, y=305)
        self.set_button1.place(x=125, y=405)
        self.set_button2.place(x=125, y=435)
        self.set_button3.place(x=125, y=465)
        self.set_button4.place(x=125, y=495)
        self.set_button5.place(x=125, y=525)
        self.set_button6.place(x=125, y=555)
        #self.set_label.place(x=150, y=355)
        self.total_label.place(x=150, y=235)
        self.total_label2.place(x=560, y=235)
        self.total_label3.place(x=960, y=235)
        self.total_label4.place(x=560, y=435)
        self.total_label5.place_forget()
        self.total_label6.place_forget()
    def set5(self):
        self.root.geometry("1200x575")
        self.rollZone2.place(x=450, y=75)
        self.rollZone3.place(x=850, y=75)
        self.rollZone4.place(x=450, y=275)
        self.rollZone5.place(x=850, y=275)
        self.rollZone6.place_forget()
        self.roll_Button.place(x=125, y=270) # Moving all labels and buttons to the center of the window
        self.theme_button.place(x=25, y=305)
        self.theme_button2.place(x=225, y=305)
        self.set_button1.place(x=125, y=405)
        self.set_button2.place(x=125, y=435)
        self.set_button3.place(x=125, y=465)
        self.set_button4.place(x=125, y=495)
        self.set_button5.place(x=125, y=525)
        self.set_button6.place(x=125, y=555)
        #self.set_label.place(x=150, y=355)
        self.total_label.place(x=150, y=235)
        self.total_label2.place(x=560, y=235)
        self.total_label3.place(x=960, y=235)
        self.total_label4.place(x=560, y=435)
        self.total_label5.place(x=960, y=435)
        self.total_label6.place_forget()
    def set6(self):
        self.root.geometry("1200x675")
        self.rollZone2.place(x=450, y=75)
        self.rollZone3.place(x=850, y=75)
        self.rollZone4.place(x=450, y=275)
        self.rollZone5.place(x=850, y=275)
        self.rollZone6.place(x=50, y=275)
        self.roll_Button.place(x=530, y=465) # Moving all labels and buttons to the center of the window
        self.theme_button.place(x=430, y=500)
        self.theme_button2.place(x=630, y=500)
        self.set_button1.place(x=430, y=550)
        self.set_button2.place(x=630, y=550)
        self.set_button3.place(x=430, y=580)
        self.set_button4.place(x=630, y=580)
        self.set_button5.place(x=430, y=610)
        self.set_button6.place(x=630, y=610)
        #self.set_label.place(x=150, y=355)
        self.total_label.place(x=150, y=235)
        self.total_label2.place(x=560, y=235)
        self.total_label3.place(x=960, y=235)
        self.total_label4.place(x=560, y=435)
        self.total_label5.place(x=960, y=435)
        self.total_label6.place(x=150, y=435)

DiceRoller = DiceRoller()