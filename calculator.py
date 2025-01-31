import tkinter as tk

calculation=""   #initializing the variable
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
 
def evaluate_calc():
    global calculation
    try:
        result=str(eval(calculation))
        calculation=result
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
    
def clear_field():
        global calculation
        calculation=''
        text_result.delete(1.0,'end')

root=tk.Tk()
root.geometry("300x400")
root.title('Calculator')
text_result=tk.Text(root,height=2,width=16, font=('Arial',24))
text_result.grid(columnspan=5)

#button 0-9
btn_1=tk.Button(root,text='1',command=lambda: add_to_calculation(1), width=5, font=("Arial",15))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root, text="2", command=lambda: add_to_calculation(2),width=5,font=("Arial",15))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root, text="3", command=lambda: add_to_calculation(3),width=5,font=("Arial",15))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root, text="4", command=lambda: add_to_calculation(4),width=5,font=("Arial",15))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root, text="5", command=lambda: add_to_calculation(5),width=5,font=("Arial",15))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(root, text="6", command=lambda: add_to_calculation(6),width=5,font=("Arial",15))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(root, text="7", command=lambda: add_to_calculation(7),width=5,font=("Arial",15))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(root, text="8", command=lambda: add_to_calculation(8),width=5,font=("Arial",15))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root, text="9", command=lambda: add_to_calculation(9),width=5,font=("Arial",15))
btn_9.grid(row=4,column=3)

btn_0=tk.Button(root, text="0", command=lambda: add_to_calculation(0),width=5,font=("Arial",15))
btn_0.grid(row=5,column=2)

#button for +,-,*,/
btn_add=tk.Button(root, text="+", command=lambda: add_to_calculation("+"),width=5,font=("Arial",15))
btn_add.grid(row=2,column=4)

btn_sub=tk.Button(root, text="-", command=lambda: add_to_calculation("-"),width=5,font=("Arial",15))
btn_sub.grid(row=3,column=4)

btn_multiply=tk.Button(root, text="*", command=lambda: add_to_calculation("*"),width=5,font=("Arial",15))
btn_multiply.grid(row=4,column=4)

btn_div=tk.Button(root, text="/", command=lambda: add_to_calculation("/"),width=5,font=("Arial",15))
btn_div.grid(row=5,column=4)

#button for (,)
btn_openbrac=tk.Button(root, text="(", command=lambda: add_to_calculation("("),width=5,font=("Arial",15))
btn_openbrac.grid(row=5,column=1)

btn_closebrac=tk.Button(root, text=")", command=lambda: add_to_calculation(")"),width=5,font=("Arial",15))
btn_closebrac.grid(row=5,column=3)

#buttton for =
btn_equal=tk.Button(root, text="=", command=evaluate_calc,width=24,font=("Arial",15))
btn_equal.grid(row=6,column=1,columnspan=4)

#clear button
btn_clr=tk.Button(root, text="C", command=lambda: clear_field(),width=5,font=("Arial",15))
btn_clr.grid(row=6,column=4)

root.mainloop()
