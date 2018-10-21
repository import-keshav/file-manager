import os
HOME_PATH= os.getcwd()

class Root():
	
	def __init__(self):
		self.name=HOME_PATH
		os.chdir(self.name)
		self.folders=os.listdir()
		self.folders.sort()
		
	def change_head(self,name):
		previous_name=self.name
		self.name=name
		
		try:
			os.chdir(self.name)
			self.folders=os.listdir()
			self.folders.sort()
			return 1
			
		except NotADirectoryError:
			print("not a directory")
			self.name=previous_name
			return 0
					
class Root2():
	
		def __init__(self,name):
			self.name=name
			self.folders=os.listdir(name)

Head=Root()

def new_file_fun():

	print("enter your file name")
	print("")
	y=str(input())
	os.mknod(y)
	Head.folders.append(y)
	print("your file has succesfully added")
	return

def delete_file_fun():

	print("Enter full name of the file or folder")
	print("")
	x=str(input())
	os.remove(x)
	Head.folders.remove(x)
	print("file removed")
	print("")
	return

def back_fun(current_path):

	current_path_list = current_path.split("/")
	len_current_path_list = len(current_path_list)
	current_path_list=current_path_list[:len_current_path_list-1]
	current_path="/".join(current_path_list)
	Head.change_head(current_path)
	show_dir(current_path)
	return
	
def show_dir(current_path):

	current_path_list = current_path.split("/")
	len_current_path_list = len(current_path_list)
	print("You are in  " + str(current_path_list[len_current_path_list-1]) + "  directory")		
	print("")
	k=1
	for i in Head.folders:
		print(k,"=",i)
		k+=1
	print("Enter your number for going to your destination directory")
	print("")
	print("Enter B for going back")
	print("")
	print("Enter N for adding new file")
	print("")
	print("Enter D for deleting new file")
	print("")
	print("Enter S for searching file")
	print("")
	print("Enter X for exit the file manager")
	print("")
	x=input()
	if(x.isdigit()):
		enter_dir(int(x),current_path,Head.folders)
	elif(x=='B'):
		back_fun(current_path)
	elif(x=='N'):
		new_file_fun()
		show_dir(current_path)
	elif(x=='D'):
		delete_file_fun()
		show_dir(current_path)
	elif(x=='S'):
		x=str(input())
		print("Your file path is : " + os.path.realpath(x))
		show_dir(current_path)
	elif(x=='X'):
		exit(0)
		
def enter_dir(dir_num,current_path,lists):

	current_path = current_path + "/" + str(lists[dir_num-1])
	error_value = Head.change_head(current_path)
	if(error_value==0):
		print("enter directory number")
		y=int(input())
		enter_dir(y,os.getcwd(),Head.folders)
	else:
		show_dir(Head.name)	


def main():

	print("You are in HOME directory")
	print("")
	k=1
	for i in Head.folders:
		print(k,"=",i)
		k+=1	
	print("Enter your number for going to your destination directory")
	print("")
	dir_num=int(input())
	enter_dir(dir_num,os.getcwd(),Head.folders)

main()
