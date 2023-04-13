from tkinter import*
from tkinter import ttk
root=Tk()
shape=root.geometry("800x800")
text=root.title("Shape Maker")
c=Canvas(root,width=990,height=490,bg="white",highlightbackground="gray")
c.pack()
cc=Label(root,text="Choose Color:")
cc.place(relx=0.6,rely=0.9,anchor=CENTER)
fillcolor=["plum","mediumaquamarine","peachpuff","yellowgreen"]
def circle(event):
    oldx=sxd.get()
    oldy=syd.get()
    newx=exd.get()
    newy=eyd.get()
    if (keypress=='c'):
        draw_circle=canvas.create_oval(oldx,oldy,newx,newy,fill=color)
    draw(keypress,oldx,oldy,newx,newy)
def rect(event):
    oldx=sxd.get()
    oldy=syd.get()
    newx=exd.get()
    newy=eyd.get()
    if (keypress=='r'):
        draw_rect=canvas.create_rectangle(oldx,oldy,newx,newy)
    draw(keypress,oldx,oldy,newx,newy) 
def line(event):
    oldx=sxd.get()
    oldy=syd.get()
    newx=exd.get()
    newy=eyd.get()
    if (keypress=='l'):
        draw_line=canvas.create_line(oldx,oldy,newx,newy)
    draw(keypress,oldx,oldy,newx,newy)
def draw(keypress,oldx,oldy,newx,newy):
    color=cd.get()
    if (keypress=='c'):
        draw_circle=canvas.create_oval(oldx,oldy,newx,newy,width=4,fill=color)
    draw(keypress,oldx,oldy,newx,newy)
    if (keypress=='r'):
        draw_rect=canvas.create_oval(oldx,oldy,newx,newy,width=4,fill=color)
    draw(keypress,oldx,oldy,newx,newy)
    if keypress==('l'):
        draw_line=canvas.create_line(oldx,oldy,newx,newy,width=4,fill=color)
    draw(keypress,oldx,oldy,newx,newy)
cd=ttk.Combobox(root,state="readonly",values=fillcolor,width=10)
cd.place(relx=0.8,rely=0.9,anchor=CENTER)
cv=[10,50,100,200,300,400,500,600,800,900]
sx=Label(root,text="startx:")
sx.place(relx=0.1,rely=0.85,anchor=CENTER)
sxd=ttk.Combobox(root,state="readonly",values=cv,width=10)
sxd.place(relx=0.2,rely=0.85,anchor=CENTER)
sy=Label(root,text="starty:")
sy.place(relx=0.3,rely=0.85,anchor=CENTER)
syd=ttk.Combobox(root,state="readonly",values=cv,width=10)
syd.place(relx=0.4,rely=0.85,anchor=CENTER)
ex=Label(root,text="endx:")
ex.place(relx=0.5,rely=0.85,anchor=CENTER)
exd=ttk.Combobox(root,state="readonly",values=cv,width=10)
exd.place(relx=0.6,rely=0.85,anchor=CENTER)
ey=Label(root,text="endy:")
ey.place(relx=0.7,rely=0.85,anchor=CENTER)
eyd=ttk.Combobox(root,state="readonly",values=cv,width=10)
eyd.place(relx=0.8,rely=0.85,anchor=CENTER)
root.bind("<c>",circle)
root.bind("<r>",rect)
root.bind("<l>",line)
root.mainloop()
