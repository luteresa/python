import os
import time

#1. The files and directories to be backed up are
#specified in a list

source =['/home/yyb/work/git/python']


#2.the backup must be stored in a main backup directory
target_dir =  '/home/yyb/work/git/bk_python'

#create tart directory if it is not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#3. the files are backed up into a zip file
#4. the name of the zip archive is the current date and time
#in the main directory
#the  curretn day is the name of the subdirectory
today = target_dir + os.sep + time.strftime('%Y%m%d')
#The current time is the name of zip archive
now=time.strftime('%H%M%S')
comment=input('Enter a comment -->')
#check if a comment was entered
if len(comment) == 0:
	target=today + os.sep + now + '.bz2'
else:
	target = today + os.sep + now + '_'+ \
	comment.replace(' ','_')+ '.bz2'

print(target)

#Create the subdircoty if it isn't already there
if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created dirctory',today)


#5.we use the zip command to put the files in a zip archive
tar_command = 'tar jcvf {0} {1}'.format(target,' '.join(source))

#run the backup
print('tar command is:')
print(tar_command)
print('Running:')
if os.system(tar_command) == 0:
	print('Successful backup to',target)
else:
	print('Backup failed')
