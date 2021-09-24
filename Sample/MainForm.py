import tkinter as tk


window = tk.Tk()

window.title('window')

window.geometry('500x100')

lbl_1 = tk.Label(window, text='This is a testing', bg='Yellow', fg='#263238', font=('Arial', 18))

lbl_1.grid(column=0, row=0)

window.mainloop()