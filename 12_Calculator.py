# Python калькулятор

import tkinter as tk


def get_sum():
    a = int(first_entry.get())
    b = int(second_entry.get())
    result_label['text'] = a + b

def get_subtrac():
    a = int(first_entry.get())
    b = int(second_entry.get())
    result_label['text'] = a - b

def get_mult():
    a = int(first_entry.get())
    b = int(second_entry.get())
    result_label['text'] = a * b

def get_div():
    a = int(first_entry.get())
    b = int(second_entry.get())
    if b == 0:
        result_label['text'] = 'Error: division by zero'
    else:
        result_label['text'] = a / b


window = tk.Tk()
window.geometry('300x200')
window.title('Python калькулятор')

first = tk.Label(text='Первое число')
first.grid(column=0, row=0, padx=10, pady=10)
second = tk.Label(text='Второе число')
second.grid(column=0, row=1)
result = tk.Label(text='Результат')
result.grid(column=0, row=2, padx=10, pady=10)

first_entry = tk.Entry(justify='right')
first_entry.grid(column=1, row=0, columnspan=4)
second_entry = tk.Entry(justify='right')
second_entry.grid(column=1, row=1, columnspan=4)
result_label = tk.Label(text='', relief='sunken', bg='azure')
result_label.grid(column=1, row=2, columnspan=4, sticky='ew')

button = tk.Button(window, text='+', command=get_sum, width='3', activebackground='azure2')
button.grid(column=1, row=3, padx=1)
button = tk.Button(window, text='-', command=get_subtrac, width='3', activebackground='azure2')
button.grid(column=2, row=3, padx=1)
button = tk.Button(window, text='*', command=get_mult, width='3', activebackground='azure2')
button.grid(column=3, row=3, padx=1)
button = tk.Button(window, text='/', command=get_div , width='3', activebackground='azure2')
button.grid(column=4, row=3, padx=1)

window.mainloop()
