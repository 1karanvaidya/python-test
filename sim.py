import os,sys,getpass,shutil,commands


path = os.getcwd()
fileLists = os.listdir(path)


def extract_(s):
	s = s.split()
	files = []
	args = []
	cmd = s[0]
	directory = []
	if cmd=="cp" or cmd=="mkdir":
		for i in range(1,len(s)):	
			try:		
				if s[i][0]=='-':
					args.append(s[i])
				elif os.path.isfile(s[i]):
					files.append(s[i])
				elif os.path.exists(os.getcwd()+"/"+s[i]): 
					directory.append(os.getcwd()+"/"+s[i])
				elif os.path.exists(os.path.split(s[i])[1]):
					directory.append(os.getcwd()+"/"+os.path.split(s[i])[1])
				elif os.path.exists(s[i]): 
					directory.append(s[i])
				else:
					directory.append(s[i])
			
			except (OSError,IOError):
				print "cannot access "+s[i]+": No such file or directory"
				return -1
		return (cmd,args,directory,files)

			
	for i in range(1,len(s)):	
		try:		
			if s[i][0]=='-':
				args.append(s[i])
			elif os.path.isfile(s[i]):
				files.append(s[i])
			elif os.path.exists(os.getcwd()+"/"+s[i]): 
				directory.append(os.getcwd()+"/"+s[i])
			elif os.path.exists(os.path.split(s[i])[1]):
				directory.append(os.getcwd()+"/"+os.path.split(s[i])[1])
			elif os.path.exists(s[i]): 
				directory.append(s[i])			
			else:
				print "cannot access \'"+s[i]+"\': No such file or directory"
				return -1
			
		except (IOError,OSError):
			print "cannot access "+s[i]+": No such file or directory"
			return -1
	return (cmd,args,directory,files)

def cd(directory):
	try:	
		if len(directory) == 0:
			return -1	
		else:
			os.chdir(directory[0])
	except (OSError,IOError):
		print "cannot access \'"+s[i]+"\': No such file or directory"

def ls(): 
    for file in fileLists:
    	print(file)

def remove(args,directory,files):
	try:
		count_arguments = len(args)
		count_files = len(files)
		if count_arguments==0:
			if count_files==0 and len(directory) == 0:
				print "rm: missing operand"
			elif count_files!=0 and len(directory) == 0:
				for i in files:
					os.remove(i)
			elif count_files==0 and len(directory) != 0:
				for i in range(0,len(directory)):
					print "rm: cannot remove \'"+directory[i]+"\': Is a directory"
			elif count_files!=0 and len(directory) != 0:
				for i in files:
					os.remove(i)
				for i in range(0,len(directory)):
					print "rm: cannot remove \'"+directory[i]+"\': Is a directory"
	
		elif count_arguments==1:
			if args[0]=="-r":
				if count_files==0 and len(directory) == 0:
					print "rm: missing operand"
				elif count_files!=0 and len(directory) == 0:
					for i in files:
						os.remove(i)
				elif count_files==0 and len(directory) != 0:
					for i in directory:
						for root, dirs, files in os.walk(i, topdown=False):
	    						for name in files:
								os.remove(os.path.join(root, name))
	    						for name in dirs:
								os.rmdir(os.path.join(root, name))
						os.removedirs(i)
				elif count_files!=0 and len(directory) != 0:
					for i in files:
						os.remove(i)
					for i in directory:
						for root, dirs, files in os.walk(i, topdown=False):
	    						for name in files:
								os.remove(os.path.join(root, name))
	    						for name in dirs:
								os.rmdir(os.path.join(root, name))
						os.removedirs(i)					

			elif ("-i" in args):
				print "Do you really want to delete:(Y/N)",
				r = raw_input()
				r = r.lower()
				if r=="y":
					args=[]
					remove(args,directory,files)
				else:
					return

			elif ("-ri" in args or "-ir" in args):
				print "Do you really want to delete:(Y/N)",
				r = raw_input()
				r = r.lower()
				if r=="y":
					args=["-r"]
					remove(args,directory,files)
				else:
					return
		
			else:
				print "rm: invalid option --\'"+args[0]+"\'"
			
		elif count_arguments==2:
			if (args[0]=="-i" and args[1]=="-r") or (args[0]=="-r" or args[1]=="-i"):
				print "Do you really want to delete:(Y/N)",
				r = raw_input()
				r = r.lower()
				if r=="y":
					args=["-r"]
					remove(args,directory,files)
				else:
					return
			else:
				print "Arguments other than -i and -r are not avaialble."
			
		else:
			print "Multi argument option not available."
	except(OSError,IOError):
		print "Remove Error."


def copy(files,directory):
	try:
		'''with open(files) as f:
									with open(directory, "w") as f1:
										for line in f:
											f1.write(line)'''
		if len(files)==1 and len(directory)==1:
			shutil.copyfile(files[0],directory[0])
		else:
			print "Invalid option"			
	except(OSError,IOError):
		print "Overwrite not allowed."

def readFile(files):
	try:
		if len(files)==1:
			if os.path.isfile(files[0]):
				fd = os.open(files[0],os.O_RDWR)
				ret = os.read(fd,100)
				print ret
				# Close opened file
				os.close(fd)
	except (IOError,OSError):
		print "cat Error"

def makeDir(directory):
	try:
		if len(directory)==1:
			if not os.path.isfile(directory[0]):
				os.mkdir(directory[0],0755)
				print "directory created"

			
		else:
			print "Not valid."
			return

	except (IOError,OSError):
		print "make directory Error"

def pathFile():
    print(os.getcwd() + "\n")




def main():
	
	pwd = os.getcwd()
	while(True):	
		os.chdir(pwd)
		print("Enter the command :")
		s = raw_input()

		if s.isspace() or s=="":
			continue		
		args = []
		files = []
		directory = []
		if(extract_(s)!=-1):
			cmd, args, directory, files = extract_(s)
		else:
			continue

		if cmd=="":
			continue
		elif s=='exit' or s=='quit':
			return	
		elif cmd=="ls":
			ls()
		elif cmd=="cd":
			cd(directory)
			pwd = os.getcwd()
		elif cmd=="rm":
			remove(args,directory,files)
		elif cmd=="cp":
			copy(files,directory)
		elif cmd=="cat":
			readFile(files)
		elif cmd=="mkdir":
			makeDir(directory)
		elif cmd=="pwd":
			pathFile()
		else:
			print "No command \'"+cmd+"\' found"	

if __name__ == "__main__":
	main() 
