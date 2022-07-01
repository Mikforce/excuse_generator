from tkinter import *
import random

root = Tk()
root['bg'] = '#7f36f5'
root.title('Генератор отмазок')
root.geometry('800x250')

quotes = ('Я не сделал', 'Я не смог', 'Я не захотел', 'Я не осилил', 'Мне не удалось')
quotes2 = ('выполнить', 'осуществить', 'воплотить идею', 'вдохнуть жизнь')
quotes3 = ('потому что кошка рожала', 'выпал снег', 'упал метеорит', 'не нашел душевных сил', 'встал не с той ноги')
run = random.choice(quotes) + ', ' + random.choice(quotes2) +', ' + random.choice(quotes3) + '.'

def outText():
    x = label.configure(text=run)
    return x

    # label2.configure(text=message2)
    # label3.configure(text=message3)

btn1 = Button(root, command=outText, text="Почему", background="blue", foreground="#fff", pady="2", font="12",
              width=30)
btn1.place(x=250, y=200)

label = Label(root, width=50, font='Times 20', fg='#2a0352')
label.place(x=20, y=20)

# label2 = Label(root)
# label2.place(x=300, y=60)
#
# label3 = Label(root)
# label3.place(x=300, y=100)

root.mainloop()
