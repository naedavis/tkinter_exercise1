# #exercise1
#adding of two numbers displayed in third entry with clear and exit buttons
import tkinter
import tkinter as tk


root= tk.Tk()
root.geometry("500x250")# sets the size of the window everything is being displayed on
label1 = tk.Label(root, text = "Please enter the first number")
label1.grid(row=0, column=0) #using grid to decide where to place a certain label
label2 = tk.Label(root, text = "Please enter second number")
label2.grid(row=1, column=0)
label3 = tk.Label(root, text = "sum of two numbers is:")
label3.grid(row=2, column=0)
def clear(): #defining a function called clear to clear the entries
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
button2 = tk.Button(root, text = "clear", command = clear)
button2.grid(row=4, column=1)
button3 = tk.Button(root, text = "exit", command = exit)
button3.grid(row=4, column= 2)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)
entry3 = tk.Entry(root)
entry3.grid(row= 2, column=1)
def addNumbers():# defining a function so that i can add the two entries and call it when the add button is presssed
    sum=int(entry1.get())+int(entry2.get()) #gets the two values entered in the entry
    entry3.insert(0,str(sum))
button1 = tk.Button(root, text="add", command=addNumbers) #the command option is caling the function previously defined
button1.grid(row=4, column=0)



root.mainloop() # this runs the entire window and everything that been placed on it





