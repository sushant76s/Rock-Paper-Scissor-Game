from tkinter import*
from PIL import Image, ImageTk
from random import randint


# main game window
rpsgame = Tk()
rpsgame.title("Rock Paper Scissor")
rpsgame.configure(background="#42CFEF")

# images
rock_user = ImageTk.PhotoImage(Image.open("data\\rock-user.png"))
paper_user = ImageTk.PhotoImage(Image.open("data\\paper-user.png"))
scissor_user = ImageTk.PhotoImage(Image.open("data\\scissors-user.png"))
rock_comp = ImageTk.PhotoImage(Image.open("data\\rock.png"))
paper_comp = ImageTk.PhotoImage(Image.open("data\\paper.png"))
scissor_comp = ImageTk.PhotoImage(Image.open("data\\scissors.png"))

# insertion of images
user_label = Label(rpsgame, image=scissor_user, bg="#42CFEF")
comp_label = Label(rpsgame, image=scissor_comp, bg="#42CFEF")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores
userScore = Label(rpsgame, text = 0, font = 100, bg="#42CFEF", fg="white")
compScore = Label(rpsgame, text = 0, font = 100, bg="#42CFEF", fg="white")
compScore.grid(row=1, column=1)
userScore.grid(row=1, column=3)

# indicators
user_indicator = Label(rpsgame, text = "USER", font = 50, bg="#42CFEF", fg="white")
comp_indicator = Label(rpsgame, text = "COMPUTER", font = 50, bg="#42CFEF", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Message
msg = Label(rpsgame, font=50, bg="#42CFEF", fg="white")
msg.grid(row=3, column=2)

# Update Message
def updateMessage(x):
    msg['text'] = x

# Update user score
def updateUserScore():
    score = int(userScore['text'])
    score += 1
    userScore['text'] = str(score)

# Update comp score
def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)

# Check Winner
def checkWinner(user, computer):
    if user == computer:
        updateMessage("It's a tie !!!")
    elif user == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif user == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif user == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass
    

# Update choices
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
# For computer
    computerChoice = choices[randint(0,2)]
    if computerChoice == "rock":
        comp_label.configure(image=rock_comp)
    elif computerChoice == "paper":
        comp_label.configure(image=paper_comp)
    else:
        comp_label.configure(image=scissor_comp)

# For user
    if x == "rock":
        user_label.configure(image=rock_user)
    elif x == "paper":
        user_label.configure(image=paper_user)
    else:
        user_label.configure(image=scissor_user)
    
    checkWinner(x, computerChoice)


# Buttons
rock = Button(rpsgame, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(rpsgame, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(rpsgame, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)


rpsgame.mainloop()