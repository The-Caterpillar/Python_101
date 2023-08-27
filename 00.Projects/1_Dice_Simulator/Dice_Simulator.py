import tkinter as tk # Used to create desktop application
from PIL import Image, ImageTk # Python ki imaging library
import random

window = tk.Tk()
window.geometry("600x400")
window.title("Dice Roll")

dice = ["1.png","2.png","3.png",'4.png','5.png','6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x=60,y=100)
label2.place(x=320,y=100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2

button = tk.Button(window,text="ROLL", bg="green", fg="white", font="Times 15 bold", command=dice_roll)
button.place(x = 250, y=10)

window.mainloop()