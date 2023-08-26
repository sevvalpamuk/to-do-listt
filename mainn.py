import tkinter
from tkinter import *
from PIL.ImageTk import PhotoImage

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")

task_list=[]
def addtask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("c:\\Users\\seval\\Desktop\\TODOLIST\\projects\\tasklist.txt","a") as taskfile:

            taskfile.write(f"\n{task}")

        task_list.append(task)
        listbox.insert(END,task)

def deletetask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
         
        with open("c:\\Users\\seval\\Desktop\\TODOLIST\\projects\\tasklist.txt","w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n") #taski altsatıra geçmeye taşı
        
        listbox.delete(ANCHOR)

def opentaskfile():

    try:
        
        with open("c:\\Users\\seval\\Desktop\\TODOLIST\\projects\\tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()


        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file=open("c:\\Users\\seval\\Desktop\\TODOLIST\\projects\\tasklist.txt","w")
        file.close()

    



#icon
image= PhotoImage(file = "c:\\Users\\seval\\Desktop\\TODOLIST\\projects\\task.png")
root.iconphoto(False, image)

#topbar
TopImage=PhotoImage(file="C:\\Users\\seval\\Desktop\\TODOLIST\\projects\\topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="C:\\Users\\seval\\Desktop\\TODOLIST\\projects\\dock.png")
Label(root,image=dockImage,bg='#32405b').place(x=30,y=25) 

noteImage=PhotoImage(file = "C:\\Users\\seval\\Desktop\\TODOLIST\\projects\\task.png")
Label(root,image=noteImage).place(x=340,y=20)

heading=Label(root,text="BÜTÜN NOTLAR",font="Verdana 14",fg="white",bg="#32405b")
heading.place(x=130,y=20)


frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="Verdana 14",bd=0)
task_entry.place(x=10,y=7)

button=Button(frame,text="ADD",font="Verdana 14", width=6,bg='blue',bd=0,fg="#fff",command=addtask)
button.place(x=300,y=0)

def onclick(event):
    addtask()


#listbox
frame1=Frame(root,width=700,height=280,bg="#32405b",bd=3)
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg='#32405b',relief='sunken',cursor='hand2',selectbackground='#5a95ff')

listbox.pack(side=LEFT ,  fill=BOTH , padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side="right",fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentaskfile()


#delete
deleteimage=PhotoImage(file="C:\\Users\\seval\\Desktop\\TODOLIST\\projects\\delete.png")
Button(root,image=deleteimage,bd=0,command=deletetask).pack(side=BOTTOM,pady=13)
 


root.mainloop()