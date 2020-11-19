import tkinter as tk
import os
from tkinter import filedialog, Text

root=tk.Tk()
apps=[]
if os.path.isfile("save.txt"):
    with open('save.txt','r') as f:
        tempApps=f.read()
        tempApps=tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]
        
def addapp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename=filedialog.askopenfilename(initialdir="/",title="Select File",filetype=(("executables","*.exe"),("allfiles","*.*")))
    apps.append(filename)
    for app in apps:
        label=tk.Label(frame,text=app,bg="grey")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas=tk.Canvas(root,height=500,width=700,bg="#263042")
canvas.pack()

frame=tk.Frame(root,bg="White")
frame.place(relheight=0.6,relwidth=0.6,relx=0.2,rely=0.1)

openfile=tk.Button(root,text="Open File",padx=10,pady=5,fg="white",bg="#263042",command=addapp)
openfile.pack()
runapps=tk.Button(root,text="RunApps",padx=10,pady=5,fg="white",bg="#263042",command=runApps)
runapps.pack()

for app in apps:
    label=tk.Label(frame,text=app)
    label.pack()

root.mainloop()
