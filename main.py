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
		btn=[]

		row_num=0
		column_num=1
		for i in range(0,len(files)):
			if(column_num%5>0 and column_num%5<=4):
				btn.append(Button(root,text=str(files[i]),height=0,width=0,font=("Helvetica",10),bg="powderblue",command=lambda c=i: enter_dir(btn[c].cget('text'),root)))
				btn[i].pack()
				column_num+=1
			else:
				btn.append(Button(root,text=str(files[i]),height=0,width=0,font=("Helvetica",10),bg="powderblue",command=lambda c=i: enter_dir(btn[c].cget('text'),root)))
				btn[i].pack()
				row_num+=1
				column_num=1

		root.mainloop()

def main():
	os.chdir(HOME_PATH)
	files=os.listdir(HOME_PATH)
	print(files,end="\n")

	root=Tk()
	root.title("Home")
	#photo=PhotoImage(file='image.png')

	row_num=0
	column_num=1
	btn=[]

	print(len(files))
	for i in range(0,len(files)):
		if(column_num%5>0 and column_num%5<=4):
			btn.append(Button(root,text=str(files[i]),height=0,width=0,font=("Helvetica",10),bg="powderblue",command=lambda c=i: enter_dir(btn[c].cget('text'),root)))
			#button.image=photo
			btn[i].grid(row=row_num,column=column_num,sticky=EW,padx=2,pady=1)
			column_num+=1
		else:
			btn.append(Button(root,text=str(files[i]),height=0,width=0,font=("Helvetica",10),bg="powderblue",command=lambda c=i: enter_dir(btn[c].cget('text'),root)))
			#button.image=photo
			btn[i].grid(row=row_num,column=column_num,sticky=EW,padx=2,pady=1)
			row_num+=1
			column_num=1
	root.mainloop()

main()
