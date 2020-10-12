import random
import tkinter
from tkinter import messagebox

# 判断函数
def Guess():
    num = random.randint(0, 1000)#随机生成一个数字
    try:
        num1 = var.get()#获得输入的值
        isinstance(num1, int)#判断是不是int型
    except Exception:
        messagebox.showwarning("Tip",'Please input only number!')#不是int型弹出警告弹框
    else:
        while True:
            if num1!=num:#判断输入值和随机数的大小
                if num1>num:
                    messagebox.showinfo("Tip","Please input a smaller number!")
                elif num1<num:
                    messagebox.showinfo("Tip","Please input a larger number!")
            else:#相等时，完成
                messagebox.showinfo("Tip","Congratulations! that's right!")
            break

tk=tkinter.Tk()
tk.title("GAME")
canvas=tkinter.Canvas(tk,width=400,height=400)#创建一个画布，声明宽和高
canvas.create_text(200,50,text="GuessNumber Game",fill="blue")
canvas.pack()
var=tkinter.IntVar()
num2=tkinter.Entry(tk,textvariable=var)#创建一个输入框
num2.place(relx=0.32,rely=0.5)
b=tkinter.Button(text="OK", width=15, height=2, command=Guess)#创建一个button，调用guess函数
b.place(relx=0.35, rely=0.7)
tk.mainloop()