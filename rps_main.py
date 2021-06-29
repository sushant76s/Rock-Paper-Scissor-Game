from tkinter import*
from PIL import Image, ImageTk


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
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

# Update comp score
def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)


rpsgame.mainloop()