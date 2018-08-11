from tkinter import *

main = Tk()
main.title('Item Price')
main.geometry('250x250')
main.resizable(height=False, width=False)
main.configure(bg='#82B1FF')

itemValue = IntVar()
itemResult = IntVar()

def calculate_result():
    value = int(itemValue.get())

    if value == 0:
        itemResult.set(int(Quantity.get()) * 120)
    elif value == 1:
        itemResult.set(int(Quantity.get()) * 64)
    elif value == 2:
        itemResult.set(int(Quantity.get()) * 2500)


Head = Label(main, text='Price App', background='#82B1FF')
labelfont = ('times', 14)
Head.config(font=labelfont)
Head.place(x=80, y=2)

Item1 = Radiobutton(main, text='Football', variable=itemValue, value=0)
Item1.config(background='#82B1FF', font='times')
Item1.place(x=1, y=40)

Item2 = Radiobutton(main, text='Manchester United 2018-19 Kit', variable=itemValue, value=1)
Item2.config(background='#82B1FF', font='times')
Item2.place(x=1, y=65)

Item3 = Radiobutton(main, text='United Season Ticket', variable=itemValue, value=2)
Item3.config(background='#82B1FF', font='times')
Item3.place(x=1, y=90)


QuantityLabel = Label(main, text='Quantity: ')
QuantityLabel.config(background='#82B1FF')
QuantityLabel.place(x=2, y=140)
Quantity = Entry(main, width=25)
Quantity.place(x=60, y=140)
Quantity.config(border=2)

ResultLabel = Label(main, text='Result: ')
ResultLabel.config(background='#82B1FF')
ResultLabel.place(x=2, y=170)
Result = Entry(main, width=25, textvariable=itemResult)
Result.place(x=60, y=170)
Result.config(border=2)


btn = Button(main, text='Calculate', command=lambda : calculate_result())
btn.place(x=85, y=200)
btn.config(background='#2962FF', foreground='#ffffff', font='times', relief=GROOVE)

main.mainloop()