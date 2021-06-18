# Importing all from tkinter
from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Creating Main Window or Container
# root is the name of the main window object
root = Tk()

# Changing the title of the application
root.title("Rock Paper Scissor")

# Background color for the application
root.configure(background="#f5eedc")


# Pictures
rock_img = ImageTk.PhotoImage(Image.open(
    r"C:\Users\pooja\OneDrive\Documents\Learning\Python\Games\R_P_S\rock.png").resize((130, 160)))
rock_img_user = ImageTk.PhotoImage(Image.open(
    r"C:\Users\pooja\OneDrive\Documents\Learning\Python\Games\R_P_S\rock-user.png").resize((130, 160)))
paper_img = ImageTk.PhotoImage(Image.open(
    r"C:\Users\pooja\OneDrive\Documents\Learning\Python\Games\R_P_S\paper.jpg").resize((130, 160)))
paper_img_user = ImageTk.PhotoImage(Image.open(
    r"C:\Users\pooja\OneDrive\Documents\Learning\Python\Games\R_P_S\paper-user.jpg").resize((130, 160)))
scissor_img = ImageTk.PhotoImage(Image.open(
    r"C:\Users\pooja\OneDrive\Documents\Learning\Python\Games\R_P_S\scissor.png").resize((130, 160)))
scissor_img_user = ImageTk.PhotoImage(Image.open(
    r"C:\Users\pooja\OneDrive\Documents\Learning\Python\Games\R_P_S\scissor-user.png").resize((130, 160)))

# Inserting Pictures
user_label = Label(root, image=scissor_img_user, bg="#f5eedc")
comp_label = Label(root, image=scissor_img, bg="#f5eedc")

# place images in window at fixed position
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=7)

# Scores of user and computer
user_score = Label(root, text=0, font='Helvetica 18 bold', fg="black")
comp_score = Label(root, text=0, font='Helvetica 18 bold', fg="black")

# fix score in window
comp_score.grid(row=1, column=1)
user_score.grid(row=1, column=3)

# Indicator for side of computer and user
user_indicator = Label(root, font='Georgia 15 bold', bg="#f5eedc",
                       text="USER").grid(row=0, column=3)
comp_indicator = Label(root, font='Georgia 15 bold', bg="#f5eedc",
                       text="COMPUTER").grid(row=0, column=1)

# Message for Result
msg = Label(root, font='Helvetica 18 bold', bg="#f5eedc", fg="black")
msg.grid(row=7, column=2)


# Button for play
rock = Button(root, width=20, height=2, text="ROCK",
              fg="white", bg="#8f8f8f", font='Helvetica 10 bold', command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2,
               text="PAPER", fg="white", bg="#e3827b", font='Helvetica 10 bold',  command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2,
                 text="SCISSOR", fg="white", bg="#84a6e8", font='Helvetica 10 bold', command=lambda: updateChoice("scissor")).grid(row=2, column=3)


# Choices list for Computer
choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    # Update Choice by Computer Randomly: "from random import randint"
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissor_img)

    # Update Choices when button clicked by user
    # To call this function in button simply pass the argument in command in buttons like:  command = lambda:updateChoice("paper")
    if x == "rock":
        user_label.configure(image=rock_img_user)
    elif x == "paper":
        user_label.configure(image=paper_img_user)
    else:
        user_label.configure(image=scissor_img_user)

    checkWin(x, compChoice)


# Update message according to the result
def updateMessage(x):
    msg['text'] = x


# Update Score of Computer
def updateCompScore():
    score = int(comp_score["text"])
    score += 1
    comp_score['text'] = str(score)

# Update Score of user


def updateUserScore():
    score = int(user_score["text"])
    score += 1
    user_score["text"] = str(score)


# Check the Winner
def checkWin(user, comp):
    if user == comp:
        updateMessage("Keep calm, It's a Tie Game...")
    elif user == "rock":
        if comp == "paper":
            updateMessage("WOW, You Lose...")
            updateCompScore()
        else:
            updateMessage("Yes, You Won...")
            updateUserScore()
    elif user == "paper":
        if comp == "scissor":
            updateMessage("WOW, You Lose...")
            updateCompScore()
        else:
            updateMessage("Yes, You Won...")
            updateUserScore()
    elif user == "scissor":
        if comp == "rock":
            updateMessage("WOW, You Lose...")
            updateCompScore()
        else:
            updateMessage("Yes, You Won...")
            updateUserScore()
    else:
        pass


# mainloop(): Its an infinite loop used to run application
# & wait for an event to occur and process the event as long as the window is not closed.
root.mainloop()
