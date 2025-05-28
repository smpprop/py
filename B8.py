from tkinter import*
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
def add():
    bats=baf.get()
    scores=[f2017.get(),f2018.get(),f2019.get(),f2020.get()]
    print(bats)
    print(scores)
    with open("batsman.csv","a") as f:
        f.write(f"{bats},{''.join(scores)}\n")
    messagebox.showinfo("batsman","details saved")
    baf.delete(0, END)
    f2017.delete(0, END)
    f2018.delete(0, END)
    f2019.delete(0, END)
    f2020.delete(0, END)

def showplot():
    data=pd.read_csv("batsman.csv")
    data.plot(x='batsman',kind='bar',title='scorecard',xlabel='batsman',ylabel='runs')
    plt.show()

with open("batsman.csv","w") as f:
    f.write("batsman 2017,2018,2019,2020\n")

root=Tk()
root.title("scores")
root.geometry("210x250")
lb_bat=Label(root,text='batsman')
lb_score=Label(root,text="scores")
lb_2017=Label(root,text="2017")
lb_2018=Label(root,text="2018")
lb_2019=Label(root,text="2019")
lb_2020=Label(root,text="2020")
lb_bat.grid(row=1,column=0,padx=5,pody=5)
lb_score.grid(row=2,column=0,padx=5,pady=5)
lb_2017.grid(row=3,column=0,padx=5,pady=5)
lb_2018.grid(row=4,column=0,padx=5,pady=5)
lb_2019.grid(row=5,column=0,padx=5,pady=5)
lb_2020.grid(row=6,column=0,padx=5,pady=5)

baf=Entry(root)
f2017=Entry(root)
f2018=Entry(root)
f2019=Entry(root)
f2020=Entry(root)

baf.grid(row=1,column=1)
f2017.grid(row=3,column=1)
f2018.grid(row=4,column=1)
f2019.grid(row=5,column=1)
f2020.grid(row=6,column=1)

addbtn=Button(root,text="add",command=add)
pltbtn=Button(root,text="plot",command=showplot)

addbtn.grid(row=7,column=0,padx=5,pady=5)
pltbtn.grid(row=7,column=1,padx=5,pady=5)

root.mainloop()

