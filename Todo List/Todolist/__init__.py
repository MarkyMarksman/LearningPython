#imports
import sys
import Tkinter
import tkMessageBox
from Tkinter import *

#GUI variable
goey = Tkinter.Tk()
#kleine GUI aanpassingen
goey.geometry('450x450')
goey.title("To-do list")

#======================================================================================= 
#Alle Commands

    #Maakt een alert message
def welcomeBack():
    tkMessageBox.showinfo( "Zyno", "Zyno, Je bent een homo")

def donothing():
    print "hallo"


    

#=======================================================================================    
#MENU
menubar = Menu(goey)
filemenu = Menu(menubar, tearoff=0)
#MENUBAR


filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=goey.quit)
#MENUBAR1
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
#MENUBAR2
menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
#MENUBAR3
menubar.add_cascade(label="Help", menu=helpmenu)

goey.config(menu=menubar)





#=======================================================================================


#Welcome label
welcomeLabel = Label(text= "Welcome", fg= 'red')
welcomeLabel.pack()
newText = Text(goey, height=2).pack()

#=======================================================================================
    #LABELFRAME
labelframe = LabelFrame(goey, text="Information")
labelframe.pack(fill="both", expand="yes")
welcomeLabel = Label(labelframe, 
             text="Welcome",
              
             height=1, 
             width=10)
welcomeLabel.pack()





#=======================================================================================








#=======================================================================================
#maakt knoppen



blackbutton = Button(goey, 
                     text="Button", 
                     fg="black",
                      
                     command = welcomeBack
                     ).place(x=0,y=400)


blackbutton = Button(goey, 
                     text="Close", 
                     fg="black",
                      
                     command = goey.quit
                     ).place(x=400,y=400)











#=======================================================================================
#################################TEST


NotesLabel = Label(text= "Notes", fg= 'red')
NotesLabel.pack()
NotesText = Text(goey, height=5).pack()


######################TEST

#=======================================================================================






#Opent de GUI
goey.mainloop()











