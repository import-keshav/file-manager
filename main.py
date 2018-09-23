import os
from tkinter import *

HOME_PATH='/home/import_keshav'

def enter_dir(path,root):
		root.destroy()
		root=Tk()
		root.title(path)
		
		current_path=HOME_PATH + '/' + path
		os.chdir(current_path)
		
		files=os.listdir(current_path)
		print(files,end="\n")
		row_num=0
		column_num=1
				
		for i in files:
			if(column_num%5!=0):
				button=Button(root,text=str(i),height=0,width=0,font=("Helvetica",30),bg="powderblue",command=lambda: enter_dir(str(i),root))
				button.grid(row=row_num,column=column_num,sticky=EW,padx=2,pady=1)
				column_num+=1
			else:
				row_num+=1
				column_num=1
	
		root.mainloop()
		
def main():
	os.chdir(HOME_PATH)
	files=os.listdir(HOME_PATH)
	print(files,end="\n")

	root=Tk()
	root.title("Home")
	photo=PhotoImage(file="image.png")
	row_num=0
	column_num=1
	
	for i in files:
		if(column_num%5!=0):
			button=Button(root,text=str(i),height=0,width=0,font=("Helvetica",30),bg="powderblue",command=lambda: enter_dir(str(i),root))
			button.image=photo
			button.grid(row=row_num,column=column_num,sticky=EW,padx=2,pady=1)
			column_num+=1
		else:
			row_num+=1
			column_num=1
			
	root.mainloop()

main()

