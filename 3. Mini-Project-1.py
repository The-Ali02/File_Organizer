from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os       #to create folders and work with directories.
import glob       #to access the name of files
import shutil      #to perform operations on files

def organise_files1():
   path = os.getcwd()
# list with all the filename that is there in the directory
   list_ = os.listdir(path)
# This will go through each and every file
   for file_ in list_:
       name, ext = os.path.splitext(file_)
       # This is going to store the extension type
       ext = ext[1:]

       # This forces the next iteration,if it is the directory
       if ext == '':
           continue

       # This will move the file to the directory where the name 'ext' already exists
       if os.path.exists(path+'/'+ext.upper()):
           shutil.move(path+'/'+file_, path+'/'+ext.upper()+'/'+file_)
    # This will create a new directory,
       # if the directory does not already exist
       else:
           os.makedirs(path+'/'+ext.upper())
           shutil.move(path+'/'+file_, path+'/'+ext.upper()+'/'+file_)
           

#Better sort file names according to alphabetical order maths_u1, maths_u2..., student_attendance, student_cie,
#student_mids.......and so on
#Iterate over sorted list of files and put the file in new directories as required

'''def org1_files():
    list_dir=os.listdir()    #list of all dirs present in cwd
    print("List of ",len(list_dir)," files present in the directory are :\n\n",list_dir)
    c1=c2=0

    #using list slicing to know number of files with provided initial file name

    for i in range(len(list_dir)):
        if list_dir[i][0:12]=='160120737043':
            c1+=1
            
        elif list_dir[i][0:4]=='oopp':
            c2+=1
            
    print("\n\nThere are ",c1," files with initial as '160120737043' in the directory.")
    print("\n\nThere are ",c2," files with initial as 'oopp' in the directory.")

    #now using glob module to access the complete file 
    ##print("\n\nThe file with initials as 160120737043 are: \n\n")
    ##for file_name in glob.glob("160120737043*"):
    ##    
    ##    print(file_name,end=" , ")
    ##    
    print("\n\nThe file with initials as oopp are: \n\n")
    #here * represents extra characters after the specified name of file

    for file_name in glob.glob("oopp*"):
        print(file_name,end=" , ")
    print('\n\n\n')

   #Week-2
    oopp_files=[]
    #os.mkdir("OOPP FOLDER")
##    for file in glob.glob("oopp*"):    #here * represents extra char after the specified name of file
##        oopp_files.append(file)
##        shutil.move(file,"OOPP FOLDER")

    #using user input
        
    init=" "
    while init.upper()!="QUIT":
        init=input("Enter file initial you want to put in a common folder/quit  :  ")
        if init=="quit":
            break
        try:
            os.mkdir(str(init).upper()+" Folder")
            for file in glob.glob("*"+str(init)+"*"):
                shutil.move(file,str(init).upper()+" Folder")
        except:
            for file in glob.glob(str(init)+"*"):
                shutil.move(file,str(init).upper()+" Folder")
                
    # To give input as any random characters of file
    f=" "
    while f.upper()!="QUIT":
        f=input("Enter file's random name you want to put in a common folder/quit  :  ")
        if f=="quit":
            break
        try:
            os.mkdir(str(f).upper()+" Folder")
            for file in glob.glob("*"+str(f)+"*"):
                shutil.move(file,str(f).upper()+" Folder")
        except:
            for file in glob.glob("*"+str(f)+"*"):
                shutil.move(file,str(f).upper()+" Folder") '''

'''Start'''
# Creating the backend functions

def opt_1():
   mb.showinfo(title='File Name', message='Please enter the file name : ')
   Label(root, text = 'File name', font = ('calibre',16,'bold')).place(x=93, y=500)
   #new_name = Entry(root, width=25, font=("Times New Roman", 15))
   #new_name.place(x=215, y=500)
   loop = 0
   def org1_files(user_input):
           list_dir=os.listdir()    #list of all dirs present in cwd
           print("List of ",len(list_dir)," files present in the directory are :\n\n",list_dir)
           
           #init=input("Enter file initial you want to put in a common folder/quit  :  ")
           if user_input=="quit":
               return
           try:
               os.mkdir(str(user_input).upper()+" Folder")
               for file in glob.glob("*"+str(user_input)+"*"):
                   shutil.move(file,str(user_input).upper()+" Folder")
           except:
               for file in glob.glob("*"+str(user_input)+"*"):
                   shutil.move(file,str(user_input).upper()+" Folder")

   while loop < 2:

       print ('loop')

       def user_data():
           user_input = data.get()
           org1_files(user_input)
       lb=Label(root, text = 'File name', font = ('calibre',16,'bold')).place(x=93, y=500)
       data = Entry(root, width=25, font=("Times New Roman", 15))
       data.place(x=215, y=500)
         
       #lb=ttk.Label(roott, text="Enter data")
       #data=ttk.Entry(roott)
       Button(root, text='Ok', command=user_data).place(x=500, y=500)
       if data.get()=='quit':
           break

       loop += 1

   #roott.mainloop()

def opt_2():
    mb.showinfo(title='File Type', message=' Processing')
    organise_files1()
    

# Defining the variables
title = 'File Organizer'
background='Yellow'

button_font = ("Pristina", 30)
button_background = 'White'

# Initializing the window
root = Tk()
root.title(title)
root.geometry('700x650')
root.config(bg=background)

# Creating and placing the components in the window
Label(root, text=title, font=("Algerian", 40), bg=background).place(x=200, y=100)

Button(root, text='File name', width=20, font=button_font, bg=button_background, command=opt_1).place(x=150, y=250)

Button(root, text='File Extension', width=20, font=button_font, bg=button_background, command=opt_2).place(x=150, y=350)

#Finalizing the windowroot.update()
root.mainloop()

'''user=input("Do you want to sort files based on names ? ")
if user=='y':
        org1_files()
user=input("Do you want to sort files based on extension ? ")
if user=='y':
        organise_files1()'''
