from tkinter import  *;

def clear_all():
    c_int.config(state='normal') 
    prn.delete(0,"end")
    rt.delete(0, "end")
    tm.delete(0, "end")
    c_int.delete(0, "end")

def compute_interest():
    p=float(prn.get())
    r=float(rt.get())
    t=float(tm.get())
    x=p*(1+r/100)**t
    ci = x - p
    c_int.insert(0, str(ci))
    c_int.config(state='readonly')

root=Tk()
root.geometry("300x200")
root.title("Compound Interest")
lbl_1=Label(root, text="Principal Amount : ")
lbl_2=Label(root, text="Rate Of Interest : ")
lbl_3=Label(root, text="Time (in years)  : ")
lbl_4=Label(root, text="Compound Interest : ")
lbl_1.grid(row=1, column=0, padx=5, pady=5)
lbl_2.grid(row=2, column=0, padx=5, pady=5)
lbl_3.grid(row=3, column=0, padx=5, pady=5)
lbl_4.grid(row=4, column=0, padx=5, pady=5)

prn=Entry(root)
rt=Entry(root)
tm=Entry(root)
c_int=Entry(root)

prn.grid(row=1, column=1, padx=5, pady=5)
rt.grid(row=2, column=1, padx=5, pady=5)
tm.grid(row=3, column=1, padx=5, pady=5)
c_int.grid(row=4, column=1, padx=5, pady=5)

btn1=Button(root, text="Submit", command=compute_interest)
btn2=Button(root,text="Clear", command=clear_all)

btn1.grid(row=7,column=0, padx=5, pady=5)
btn2.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()
 