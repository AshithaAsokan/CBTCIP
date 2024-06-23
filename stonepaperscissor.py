# Task1: Stone Paper Scissor Game

import tkinter as tk
import random
from PIL import Image,ImageTk

# Function to determine the winner
def determine_winner(your_choice,computer_choice):
    if your_choice==computer_choice:
        return 'Its a tie'
    elif (your_choice=='stone' and computer_choice=='scissors') or \
         (your_choice=='scissors' and computer_choice=='paper') or \
         (your_choice=='paper' and computer_choice=='stone') :
        return 'You Wins!'
    else:
        return 'Computer Wins!'

# Function to handle button click
def on_choice(your_choice):
    computer_choice=random.choice(['stone','paper','scissors'])
    result=determine_winner(your_choice,computer_choice)

    # Update the labels with choices and result
    computer_choice_image_label.config(image=images[computer_choice])
    result_label.config(text=result)    


# Create the main window
root=tk.Tk()
root.title('Stone Paper Scissor Game')

text_label=tk.Label(root,text='Select Your Choice:',font=('Arial',14))
text_label.grid(row=0,column=0,columnspan=3,pady=10)

#images
images={
    'stone':ImageTk.PhotoImage(Image.open('stone.png').resize((70,70))),
    'paper':ImageTk.PhotoImage(Image.open('paper.png').resize((70,70))),
    'scissors':ImageTk.PhotoImage(Image.open('scissors.png').resize((70,70))),
}

# Create and place the choice buttons
stone_button = tk.Button(root, image=images['stone'], command=lambda: on_choice('stone'))
stone_button.grid(row=1, column=0, padx=10, pady=10)

paper_button = tk.Button(root, image=images['paper'], command=lambda: on_choice('paper'))
paper_button.grid(row=1, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, image=images['scissors'], command=lambda: on_choice('scissors'))
scissors_button.grid(row=1, column=2, padx=10, pady=10)

# Create and place the labels for displaying the computer's choice and result
computer_choice_text_label=tk.Label(root,text='Computer Choice:',font=('Arial',14))
computer_choice_text_label.grid(row=2,column=0,columnspan=3,pady=10)

computer_choice_image_label=tk.Label(root)
computer_choice_image_label.grid(row=3,column=0,columnspan=3,pady=10)

result_label=tk.Label(root,text='',font=('Arial',14))
result_label.grid(row=4,column=0,columnspan=3,pady=10)

# Run The Tkinter event loop
root.mainloop()