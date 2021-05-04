# #exercise1
#adding of two numbers displayed in third entry with clear and exit buttons
# import tkinter
# import tkinter as tk
#
#
# root= tk.Tk()
# root.geometry("500x250")
# label1 = tk.Label(root, text = "Please enter the first number")
# label1.grid(row=0, column=0)
# label2 = tk.Label(root, text = "Please enter second number")
# label2.grid(row=1, column=0)
# label3 = tk.Label(root, text = "sum of two numbers is:")
# label3.grid(row=2, column=0)
# def clear():
#     entry1.delete(0,tkinter.END)
#     entry2.delete(0,tkinter.END)
#     entry3.delete(0,tkinter.END)
# button2 = tk.Button(root, text = "clear", command = clear)
# button2.grid(row=4, column=1)
# button3 = tk.Button(root, text = "exit", command = exit)
# button3.grid(row=4, column= 2)
# entry1 = tk.Entry(root)
# entry1.grid(row=0, column=1)
# entry2 = tk.Entry(root)
# entry2.grid(row=1, column=1)
# entry3 = tk.Entry(root)
# entry3.grid(row= 2, column=1)
# def addNumbers():
#     sum=int(entry1.get())+int(entry2.get())
#     entry3.insert(0,str(sum))
# button1 = tk.Button(root, text="add", command=addNumbers)
# button1.grid(row=4, column=0)
#
#
# # label1.pack(side=LEFT)
# # entry1.pack(side=RIGHT)
# # label2.pack(side=LEFT)
# # entry2.pack(side=RIGHT)
# # label3.pack(side=LEFT)
# # entry3.pack(side=RIGHT)
#
#
# root.mainloop()

#exercise2
# temperature convertor (Degrees Celsius to Fahrenheit and the other way round)
import tkinter as tk

root = tk.Tk()
root.geometry("500x300")
root.title("TempConvert Web Service Client")
label1 = tk.Label(root, text= "  Temperature Convert Web Service")
label1.grid(row=0, column= 2)
f_label= tk.Label(root, text= "  F:")
f_label.grid(row=1, column=0)
f_entry = tk.Entry(root)
f_entry.grid(row=1,column=1)
c_label= tk.Label(root, text= "C:")
c_label.grid(row=1, column=2)
c_entry = tk.Entry(root)
c_entry.grid(row=1,column=2)

def FtoC():
    pass

root.mainloop()



