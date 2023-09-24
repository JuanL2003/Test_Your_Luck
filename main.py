#Start final project
from tkinter import *
import random

#Layout of the window
GlassScreen = Tk()

GlassScreen.geometry('1000x1000')

GlassScreen.configure(bg="Grey")

GlassScreen.title("Guess The Roll")


#frame
my_frame = Frame(GlassScreen)
my_frame.pack(pady=20)


score_label = Label(my_frame, text = "scoregoeshere")

scoreNumber = 0

#Instuction labels

Instruction_Label_1 = Label(GlassScreen, text = "Intructions:")

Instruction_Label_2 = Label(GlassScreen, text = "Enter two numbers, if you guess right, you get a point" )

Instruction_Label_3 = Label(GlassScreen, text = "(Dice 1 on left & Dice 2 on right)")


Instruction_Label_1.pack()
Instruction_Label_2.pack()
Instruction_Label_3.pack()


def Compare():
  #Compare the user input with the actual dice result
  global scoreNumber
  global compare_1
  global compare_2
  compare_1 = int(textbox1.get())
  compare_2 = int(textbox2.get())
  print (sd1, compare_1, sd2, compare_2)
  print (compare_1 == sd1, compare_2 == sd2)

  if compare_1 == sd1 and compare_2 == sd2:
    guess_result.config(text='You guessed both correctly')
    scoreNumber = scoreNumber + 2
    score_label.config(text = (Builtstr, scoreNumber))
  elif compare_1 == sd1 or compare_2 == sd2:
    guess_result.config(text='You guessed one correctly')
    scoreNumber = scoreNumber + 1
    score_label.config(text = (Builtstr, scoreNumber))
  else:
    guess_result.config(text='You guessed none correctly')
    score_label.config(text = (Builtstr, scoreNumber))


#Get Dice Number
def get_number(x):
  if x == '\u2680':
    return(1)
  elif x == '\u2681':
    return(2)
  elif x == '\u2682':
    return(3)
  elif x == '\u2683':
    return(4)
  elif x == '\u2684':
    return(5)
  elif x == '\u2685':
    return(6)


# Rolling the Dice
def roll_dice(): 
  d1 =random.choice(my_Dice)
  d2 =random.choice(my_Dice)

  #Dice Number
  global sd1
  global sd2
  sd1 = get_number(d1)
  sd2 = get_number(d2)

  #Label updates
  dice_label1.config(text=d1)
  dice_label2.config(text=d2)
  
  #Updating Sub Labels
  sub_dice_label1.config(text=sd1)
  sub_dice_label2.config(text=sd2)

#rollCompare function
def rollCompare():
  roll_dice()
  Compare()


#Create dice list 
my_Dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]



#Dice Labels
dice_label1= Label(my_frame, text='', font=("Arial",100))
dice_label1.grid(row=0, column=0, padx=5)
sub_dice_label1 = Label(my_frame, text=" ")
sub_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text='', font=("Arial",100))
dice_label2.grid(row=0, column=1, padx=5)
sub_dice_label2 = Label(my_frame, text=" ")
sub_dice_label2.grid(row=1, column=1)

#Roll Button
my_button = Button(GlassScreen, text="Roll Dice", command=rollCompare)
my_button.pack(pady=20)

#Roll dice
roll_dice()

#Textbox lables
textboxframe = Frame(GlassScreen)

tbl1 = Label(textboxframe, text='dice 1', font=("Arial",10))
tbl2 = Label(textboxframe, text='dice 2', font=("Arial",10))

#Textbox Entry
textbox1 = Entry(textboxframe)
textbox2 = Entry(textboxframe)



#Grid

tbl1.grid(row = 0, column = 0)
tbl2.grid(row = 1, column = 0)

textbox1.grid(row=0, column=1)

textbox2.grid(row=1, column=1)

textboxframe.pack()

#reult labels
resultArea = Frame(GlassScreen)
resultArea.pack(pady=20)
guess_result = Label(resultArea, text='Guess the roll', font=("Arial",10))
guess_result.pack()


#Score Label
Builtstr = "score:" 

score_label.config(text = Builtstr)

score_label.grid(column = 2)


GlassScreen.mainloop()

