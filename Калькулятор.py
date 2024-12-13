import tkinter as tk
def add():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 + num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)

def sub():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 - num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)

def mul():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 * num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)

def div():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 / num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)

window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x400')
window.resizable(False,False)
button_add = tk.Button(window, text='Сложить', width=8, height=2, command=add)
button_add.place(x=50, y=175)
button_sub = tk.Button(window, text='Вычесть', width=8, height=2, command=sub)
button_sub.place(x=125, y=175)
button_mul = tk.Button(window, text='Умножить', width=8, height=2, command=mul)
button_mul.place(x=200, y=175)
button_div = tk.Button(window, text='Поделить', width=8, height=2, command=div)
button_div.place(x=275, y=175)
number1_entry = tk.Entry(width=47)
number1_entry.place(x=50, y=75)
number2_entry = tk.Entry(width=47)
number2_entry.place(x=50, y=130)
answer_entry = tk.Entry(width=47)
answer_entry.place(x=50, y=250)
number1 = tk.Label(window, text='Первое число:')
number1.place(x=50, y=50)
number2 = tk.Label(window, text='Второе число:')
number2.place(x=50, y=105)
answer = tk.Label(window, text='Ответ:')
answer.place(x=50, y=225)
window.mainloop()