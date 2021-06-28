from tkinter import*
from PIL import Image, ImageTk


# main game window
rpsgame = Tk()
rpsgame.title("Rock Paper Scissor")
rpsgame.configure(background="#42CFEF")

# images
rock_img_user = ImageTk.PhotoImage(Image.open("rock-user.png"))



rpsgame.mainloop()