from tkinter import*
from PIL import Image, ImageTk
from random import randint
# from playsound import playsound
import pygame

# main game window
rpsgame = Tk()
rpsgame.title("Rock Paper Scissor")
rpsgame.configure(background="#42CFEF")

# sounds
pygame.mixer.init()
#pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play()

# images
rock_user = ImageTk.PhotoImage(Image.open("data\\rock-user.png"))
paper_user = ImageTk.PhotoImage(Image.open("data\\paper-user.png"))
scissor_user = ImageTk.PhotoImage(Image.open("data\\scissors-user.png"))
rock_comp = ImageTk.PhotoImage(Image.open("data\\rock.png"))
paper_comp = ImageTk.PhotoImage(Image.open("data\\paper.png"))
scissor_comp = ImageTk.PhotoImage(Image.open("data\\scissors.png"))
combine_image = (Image.open("data\\rps.png"))
# combine_image = ImageTk.PhotoImage(Image.open("data\\rps.png"))
# for resizing the combined image
# combine_image = combine_image.PhotoImage.resize((250, 250), Image.ANTIALIAS)
resize_image = combine_image.resize((100, 100), Image.ANTIALIAS)
rimg = ImageTk.PhotoImage(resize_image)

# insertion of images
user_label = Label(rpsgame, image=scissor_user, bg="#42CFEF")
comp_label = Label(rpsgame, image=scissor_comp, bg="#42CFEF")
img_label = Label(rpsgame, image=rimg, bg="#42CFEF")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)
img_label.grid(row=1, column=2)

# Scores
userScore = Label(rpsgame, text = 0, font = 100, bg="#42CFEF", fg="white")
compScore = Label(rpsgame, text = 0, font = 100, bg="#42CFEF", fg="white")
compScore.grid(row=1, column=1)
userScore.grid(row=1, column=3)

# indicators
user_indicator = Label(rpsgame, text = "USER", font = 50, bg="#42CFEF", fg="white")
comp_indicator = Label(rpsgame, text = "COMPUTER", font = 50, bg="#42CFEF", fg="white")
user_indicator.grid(row=0, column=4)
comp_indicator.grid(row=0, column=0)

# Message
msg = Label(rpsgame, font=50, bg="#42CFEF", fg="white")
msg.grid(row=2, column=2)

def choiceSelectSound():
    pygame.mixer.music.load('data\\select.mp3')
    pygame.mixer.music.play()


# Update Message
def updateMessage(x):
    msg['text'] = x

# Update user score
def updateUserScore():
    score = int(userScore["text"])
    score += 1
    userScore["text"] = str(score)

# Update comp score
def updateCompScore():
    score = int(compScore["text"])
    score += 1
    compScore["text"] = str(score)

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
        choiceSelectSound()
    elif x == "paper":
        user_label.configure(image=paper_user)
        choiceSelectSound()
    else:
        user_label.configure(image=scissor_user)
        choiceSelectSound()
    
    checkWinner(x, computerChoice)


# Buttons
rock = Button(rpsgame, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=3, column=1)
paper = Button(rpsgame, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=3, column=2)
scissor = Button(rpsgame, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=3, column=3)


rpsgame.mainloop()