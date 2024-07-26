from tkinter import *
root = Tk()

#Create Entry Box:
res = StringVar()
box = Entry(root, width=50, textvariable=res)
box.grid(row=4,column=0, columnspan=4)

class customised_buttons:
    def __init__(self,n,fun):
        self.n = n
        self.fun = fun
        self.btn_var = Button(root, text=str(self.n), width=10, command=self.action)

    def display(self,r, c):
        self.btn_var.grid(row=r, column=c)

    def action(self):
        if self.fun=="Clear":
            box.delete(0,END)
            pass
        elif self.fun=="Equals":
            exp = str(box.get())
            result = eval(exp)
            res.set(result)
        else:
            exp = res.get()
            exp+=str(self.n)
            res.set(exp)

#Create buttons 0-0
buttons = []
for i in range(0,10):
    buttons.append(customised_buttons(i,"add_"+str(i)))

#Create Buttons to perform addition/ Subtraction/etc
add_button = customised_buttons('+',"addition")
subtract_button = customised_buttons('-',"subtraction")
multiply_button = customised_buttons('*',"multiplication")
divide_button = customised_buttons('/',"division")
clear_button = customised_buttons('C',"Clear")
evaluate_button = customised_buttons('=',"Equals")

#Display the buttons 1-9
i,j=0,0
for button in buttons: 
    button.display(j,i)
    print(j,i)
    if i==2:
        i=-1
        j+=1
    i+=1

#Grid the buttons
add_button.display(0,3)
subtract_button.display(1,3)
multiply_button.display(2,3)
divide_button.display(3,1)
clear_button.display(3,2)
evaluate_button.display(3,3)

root.mainloop()
