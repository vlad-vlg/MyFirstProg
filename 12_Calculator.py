# Python калькулятор

import tkinter as tk


window = tk.Tk()
window.geometry('300x200')
window.title('Python калькулятор')

first = tk.Label(text='Первое число')
first.grid(column=0, row=0, padx=10, pady=10)
second = tk.Label(text='Второе число')
second.grid(column=0, row=1)
result = tk.Label(text='Результат')
result.grid(column=0, row=2, padx=10, pady=10)

first_entry = tk.Entry()
first_entry.grid(column=1, row=0)
second_entry = tk.Entry()
second_entry.grid(column=1, row=1)
result_label = tk.Label(text='')
result_label.grid(column=1, row=2, sticky='w')

def get_sum():
    a = int(first_entry.get())
    b = int(second_entry.get())
    result_label['text'] = a + b

button = tk.Button(window, text='+', command=get_sum)
button.grid(column=1, row=3, sticky='w')
button = tk.Button(window, text='*')
button.grid(column=1, row=3)

window.mainloop()
