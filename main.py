import func_win
import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

window = Tk()
window.geometry("1440x890")
window.iconphoto(False, tkinter.PhotoImage(file='assets/ICO/ICO.png'))
window.configure(bg="#FFFFFF")
window.title("LearnTools   Designer by 水滴Waterrrr")


def Creat(version):
    if version == 1:
        window.destroy()
        func_win.english()
    elif version == 2:
        window.destroy()
        func_win.math()
    elif version == 3:
        window.destroy()
        func_win.chinese()


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=890,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    530.0,
    829.0,
    anchor="nw",
    text="Designer by 水滴Waterrrr",
    fill="#000000",
    font=("Inter", 32 * -1)
)

image_image_1 = PhotoImage(
    file="assets/Main/image_1.png")
image_1 = canvas.create_image(
    1151.0,
    336.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file="assets/Main/image_2.png")
image_2 = canvas.create_image(
    720.0,
    336.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file="assets/Main/image_3.png")
image_3 = canvas.create_image(
    289.0,
    336.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file="assets/Main/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Creat(1),
    relief="flat"
)
button_1.place(
    x=1003.0,
    y=554.0,
    width=296.0,
    height=68.662109375
)

button_image_2 = PhotoImage(
    file="assets/Main/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Creat(2),
    relief="flat"
)
button_2.place(
    x=572.0,
    y=554.0,
    width=296.0,
    height=68.662109375
)

button_image_3 = PhotoImage(
    file="assets/Main/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Creat(3),
    relief="flat"
)
button_3.place(
    x=141.0,
    y=554.0,
    width=296.0,
    height=68.662109375
)
window.resizable(False, False)
window.mainloop()
