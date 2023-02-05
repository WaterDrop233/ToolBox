import re
import tkinter
import function
import tkinter.messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, END

def chinese():
    def get_CN():
        content_before = contentVar.get()
        content = function.entries(content_before)
        entry_1.delete('1.0', 'end')
        entry_1.insert(END, content)

    window = Tk()
    window.title("LT --语文")
    window.iconphoto(False, tkinter.PhotoImage(file='assets/ICO/ICO.png'))
    window.geometry("842x595")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=595,
        width=842,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    entry_image_1 = PhotoImage(
        file=r'assets/Chinese/entry_1.png')
    entry_bg_1 = canvas.create_image(
        436.0,
        368.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=150.0,
        y=195.0,
        width=578.0,
        height=346.0
    )
    contentVar = StringVar(window, '')
    entry_image_2 = PhotoImage(
        file=r'assets/Chinese/entry_2.png')
    entry_bg_2 = canvas.create_image(
        368.5,
        77.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=contentVar
    )
    entry_2.place(
        x=140.0,
        y=60.0,
        width=453.0,
        height=37.0
    )

    button_image_1 = PhotoImage(
        file=r'assets/Chinese/button_1.png')
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: get_CN(),
        relief="flat"
    )
    button_1.place(
        x=603.0,
        y=57.0,
        width=130.0,
        height=40.0
    )

    window.resizable(False, False)
    window.mainloop()
    main()


def math():
    def onclick(self):
        operation = ('+', '-', '*', '/', '**', '//')
        content = contentVar.get()
        if content.startswith('.'):
            content = '0' + content
        if self in '0123456789':
            content += self
        elif self == '.':
            lastPart = re.split(r"\+|-|\*|/", content)[-1]
            if '.' in lastPart:
                tkinter.messagebox.showerror('错误', '重复出现的小数点')
                return
            else:
                content += self
        elif self == 'C':
            content = ''
        elif self == '=':
            try:
                content = str(eval(content))
            except:
                tkinter.messagebox.showerror('错误', '表达式有误')
                return
        elif self in operation:
            if content.endswith(operation):
                tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
                return
            content += self
        elif self == '√':
            n = content.split('.')
            if all(map(lambda x: x.isdigit(), n)):
                content = eval(content) ** 0.5
            else:
                tkinter.messagebox.showerror('错误', '表达式错误')
                return
        contentVar.set(content)

    window = Tk()
    window.title("LT --数学")
    window.iconphoto(False, tkinter.PhotoImage(file='assets/ICO/ICO.png'))
    window.geometry("363x412")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=412,
        width=363,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    contentVar = StringVar(window, '')
    entry_image_1 = PhotoImage(
        file="assets/Math/entry_1.png")
    entry_bg_1 = canvas.create_image(
        180.5,
        34.10425567626953,
        image=entry_image_1,
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=contentVar
    )
    entry_1['state'] = 'readonly'
    entry_1.place(
        x=8.0,
        y=1.0,
        width=345.0,
        height=66.20851135253906
    )

    button_image_1 = PhotoImage(
        file="assets/Math/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("."),
        relief="flat"
    )
    button_1.place(
        x=284.0,
        y=370.0,
        width=77.0,
        height=41.0
    )

    button_image_2 = PhotoImage(
        file="assets/Math/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("//"),
        relief="flat"
    )
    button_2.place(
        x=189.0,
        y=370.0,
        width=77.0,
        height=41.0
    )

    button_image_3 = PhotoImage(
        file="assets/Math/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("√"),
        relief="flat"
    )
    button_3.place(
        x=94.0,
        y=370.0,
        width=77.0,
        height=41.0
    )

    button_image_4 = PhotoImage(
        file="assets/Math/button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("**"),
        relief="flat"
    )
    button_4.place(
        x=0.0,
        y=370.0,
        width=77.0,
        height=40.0
    )

    button_image_5 = PhotoImage(
        file="assets/Math/button_5.png")
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("C"),
        relief="flat"
    )
    button_5.place(
        x=284.0,
        y=304.0,
        width=77.0,
        height=41.0
    )

    button_image_6 = PhotoImage(
        file="assets/Math/button_6.png")
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("/"),
        relief="flat"
    )
    button_6.place(
        x=189.0,
        y=304.0,
        width=77.0,
        height=41.0
    )

    button_image_7 = PhotoImage(
        file="assets/Math/button_7.png")
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("*"),
        relief="flat"
    )
    button_7.place(
        x=94.0,
        y=304.0,
        width=77.0,
        height=41.0
    )

    button_image_8 = PhotoImage(
        file="assets/Math/button_8.png")
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("0"),
        relief="flat"
    )
    button_8.place(
        x=0.0,
        y=303.0,
        width=77.0,
        height=41.0
    )

    button_image_9 = PhotoImage(
        file="assets/Math/button_9.png")
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("="),
        relief="flat"
    )
    button_9.place(
        x=284.0,
        y=237.0,
        width=77.0,
        height=41.0
    )

    button_image_10 = PhotoImage(
        file="assets/Math/button_10.png")
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("9"),
        relief="flat"
    )
    button_10.place(
        x=189.0,
        y=237.0,
        width=77.0,
        height=41.0
    )

    button_image_11 = PhotoImage(
        file="assets/Math/button_11.png")
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("8"),
        relief="flat"
    )
    button_11.place(
        x=94.0,
        y=237.0,
        width=77.0,
        height=41.0
    )

    button_image_12 = PhotoImage(
        file="assets/Math/button_12.png")
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("7"),
        relief="flat"
    )
    button_12.place(
        x=0.0,
        y=237.0,
        width=77.0,
        height=40.0
    )

    button_image_13 = PhotoImage(
        file="assets/Math/button_13.png")
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("-"),
        relief="flat"
    )
    button_13.place(
        x=284.0,
        y=170.0,
        width=77.0,
        height=40.0
    )

    button_image_14 = PhotoImage(
        file="assets/Math/button_14.png")
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("6"),
        relief="flat"
    )
    button_14.place(
        x=189.0,
        y=170.0,
        width=77.0,
        height=40.0
    )

    button_image_15 = PhotoImage(
        file="assets/Math/button_15.png")
    button_15 = Button(
        image=button_image_15,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("5"),
        relief="flat"
    )
    button_15.place(
        x=94.0,
        y=170.0,
        width=77.0,
        height=40.0
    )

    button_image_16 = PhotoImage(
        file="assets/Math/button_16.png")
    button_16 = Button(
        image=button_image_16,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("4"),
        relief="flat"
    )
    button_16.place(
        x=0.0,
        y=169.0,
        width=77.0,
        height=41.0
    )

    button_image_17 = PhotoImage(
        file="assets/Math/button_17.png")
    button_17 = Button(
        image=button_image_17,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("+"),
        relief="flat"
    )
    button_17.place(
        x=284.0,
        y=103.0,
        width=77.0,
        height=41.0
    )

    button_image_18 = PhotoImage(
        file="assets/Math/button_18.png")
    button_18 = Button(
        image=button_image_18,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("3"),
        relief="flat"
    )
    button_18.place(
        x=189.0,
        y=103.0,
        width=77.0,
        height=41.0
    )

    button_image_19 = PhotoImage(
        file="assets/Math/button_19.png")
    button_19 = Button(
        image=button_image_19,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("2"),
        relief="flat"
    )
    button_19.place(
        x=94.0,
        y=103.0,
        width=77.0,
        height=41.0
    )

    button_image_20 = PhotoImage(
        file="assets/Math/button_20.png")
    button_20 = Button(
        image=button_image_20,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onclick("1"),
        relief="flat"
    )
    button_20.place(
        x=0.0,
        y=103.0,
        width=77.0,
        height=40.0
    )
    window.resizable(False, False)
    window.mainloop()
    main()


def english():
    def button_click():
        content_before = contentVar.get()
        content = function.translation(content_before)
        content = content.get("data")
        contentVar2.set(content_before)
        contentVar3.set(content[0].get("v"))
        entry_4.delete('1.0', 'end')
        for i in range(len(content[0])):
            content_after = content[i].get("k") + ' ' + content[i].get("v") + '\n'
            entry_4.insert(END, content_after)

    window = Tk()
    window.geometry("560x384")
    window.title("LT --英语")
    window.iconphoto(False, tkinter.PhotoImage(file='assets/ICO/ICO.png'))
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=384,
        width=560,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    contentVar = StringVar(window, '')
    entry_image_1 = PhotoImage(
        file="assets/English/entry_1.png")
    entry_bg_1 = canvas.create_image(
        222.47796630859375,
        35.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=contentVar
    )
    entry_1.place(
        x=25.0,
        y=17.0,
        width=394.9559326171875,
        height=39.0
    )

    button_image_1 = PhotoImage(
        file="assets/English/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(),
        relief="flat"
    )
    button_1.place(
        x=431.0,
        y=15.0,
        width=111.0,
        height=40.0
    )

    image_image_1 = PhotoImage(
        file="assets/English/image_1.png")
    image_1 = canvas.create_image(
        279.0,
        220.0,
        image=image_image_1
    )

    contentVar2 = StringVar(window, '')
    entry_image_2 = PhotoImage(
        file="assets/English/entry_2.png")
    entry_bg_2 = canvas.create_image(
        194.16942596435547,
        122.33242797851562,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=contentVar2
    )
    entry_2.place(
        x=74.17355346679688,
        y=98.21978759765625,
        width=239.9917449951172,
        height=48.22528076171875
    )
    entry_2['state'] = 'readonly'

    contentVar3 = StringVar(window, '')
    entry_image_3 = PhotoImage(
        file="assets/English/entry_3.png")
    entry_bg_3 = canvas.create_image(
        194.16942596435547,
        172.55768966674805,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=contentVar3
    )
    entry_3.place(
        x=74.17355346679688,
        y=148.44505310058594,
        width=239.9917449951172,
        height=48.22527313232422
    )
    entry_3['state'] = 'readonly'

    # contentVar4 = StringVar(window, '')
    entry_image_4 = PhotoImage(
        file="assets/English/entry_4.png")
    entry_bg_4 = canvas.create_image(
        296.8553771972656,
        264.6373519897461,
        image=entry_image_4
    )
    entry_4 = Text(
        bd=0,
        bg="#F0F0F0",
        fg="#000716",
        highlightthickness=0,
    )
    entry_4.place(
        x=74.17355346679688,
        y=198.67031860351562,
        width=445.3636474609375,
        height=131.93406677246094
    )

    window.resizable(False, False)
    window.mainloop()
    main()


def main():
    window = Tk()
    window.geometry("1000x500")
    window.iconphoto(False, tkinter.PhotoImage(file='assets/ICO/ICO.png'))
    window.configure(bg="#F0F0F0")
    window.title("LearnTools")

    def Creat(version):
        if version == 1:
            window.destroy()
            english()
        elif version == 2:
            window.destroy()
            math()
        elif version == 3:
            window.destroy()
            chinese()

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=500,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    button_image_1 = PhotoImage(
        file="assets/Main/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Creat(2),
        relief="flat"
    )
    button_1.place(
        x=700.0,
        y=213.0,
        width=200.0,
        height=75.0
    )

    button_image_2 = PhotoImage(
        file="assets/Main/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Creat(1),
        relief="flat"
    )
    button_2.place(
        x=400.0,
        y=213.0,
        width=200.0,
        height=75.0
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
        x=100.0,
        y=213.0,
        width=200.0,
        height=75.0
    )

    window.resizable(False, False)
    window.mainloop()

main()