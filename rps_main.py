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

rpsgame.mainloop()