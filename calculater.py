from tkinter import *
import tkinter.messagebox


# ==================setting===================
root = Tk()
root.geometry('400x200')
root.title('Calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# ===================Variables===================
n1 = StringVar()
n2 = StringVar()
rv = StringVar()


# ===================frames===================
t1 = Frame(root, width=400, height=50, bg=color)
t1.pack(side=TOP)

t2 = Frame(root, width=400, height=50, bg=color)
t2.pack(side=TOP)

t3 = Frame(root, width=400, height=50, bg=color)
t3.pack(side=TOP)

t4 = Frame(root, width=400, height=50, bg=color)
t4.pack(side=TOP)

# ===================Functions===================


def errormsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')


def plus():
    try:
        v = float(n1.get()) + float(n2.get())
        rv.set(v)
    except:
        errormsg('error')


def minus():
    try:
        v = float(n1.get()) - float(n2.get())
        rv.set(v)
    except:
        errormsg('error')


def mul():
    try:
        v = float(n1.get()) * float(n2.get())
        rv.set(v)
    except:
        errormsg('error')


def div():
    if n2.get() == '0':
        errormsg('division zero error')
    elif n2.get() != '0':
        try:
            v = float(n1.get()) / float(n2.get())
            rv.set(v)
        except:
            errormsg('error')


# ===================Buttons===================
bp = Button(t3, text="+", width=10,
            highlightbackground=color, command=lambda: plus())
bp.pack(side=LEFT, padx=10, pady=10)

bm = Button(t3, text="-", width=10,
            highlightbackground=color, command=lambda: minus())
bm.pack(side=LEFT, padx=10, pady=10)

bml = Button(t3, text="*", width=10,
             highlightbackground=color, command=lambda: mul())
bml.pack(side=LEFT, padx=10, pady=10)

bd = Button(t3, text="/", width=10,
            highlightbackground=color, command=lambda: div())
bd.pack(side=LEFT, padx=10, pady=10)

# ===================Entries and Labels===================
lfn = Label(t1, text='Input Number 1: ', bg=color)
lfn.pack(side=LEFT, pady=10)

fn = Entry(t1, highlightbackground=color, textvariable=n1)
fn.pack(side=LEFT, pady=10, padx=10)

lsn = Label(t2, text='Input Number 2: ', bg=color)
lsn.pack(side=LEFT, pady=10)

sn = Entry(t2, highlightbackground=color, textvariable=n2)
sn.pack(side=LEFT, pady=10, padx=10)

res = Label(t4, text='Result : ', bg=color)
res.pack(side=LEFT, pady=10)

rn = Entry(t4, highlightbackground=color, textvariable=rv)
rn.pack(side=LEFT, pady=10, padx=10)


root.mainloop()
