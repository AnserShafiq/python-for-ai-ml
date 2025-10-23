import os
print(dir(os)) # will print the list of all the attributes and methods


print(os.getcwd()) # Will give current working directory
 
os.chdir('/Users/786/Desktop/Projects') # Will set given path as current working directory
print(os.getcwd())

print(os.listdir()) # Will give the list of all the folders and files present in the general directory or current added directory

os.mkdir('dir_name') # Will create new directory/folder in the current directory
print(os.listdir())

os.makedirs('dir_name_2/sub_dir_1') # By using it can create sub directory in the directories. For example it will create a sub directory named as sub_dir_1 in the directory dir_name. 
# And if the parent directory is also not available first it will create parent then sub child.


os.rmdir('dir_name') # Will delete a directory if not sub directory init
print(os.listdir())
os.removedirs('dir_name/sub_dir_1') # Will delete the sub directory of the highlighted given directory and if the sub dir is last so will also delete the parent
print(os.listdir())

os.makedirs('dir_name_2/sub_dir_2')
os.makedirs('dir_name_2/sub_dir_3')

os.removedirs('dir_name_2/sub_dir_2') 
print(os.listdir())


os.chdir('/Users/786/Desktop/Projects/dir_name_2')
print(os.listdir())

os.rename('sub_dir_3','sub_dir_2') # To rename a folder/file, first target folder/file name second new name for the target folder/file
print(os.listdir())


os.rename('test.txt','demo.txt')
print(os.listdir())

print(os.stat('demo.txt')) # Will give the stats about the file
print(os.stat('demo.txt').st_size) # Will give the file size
print(os.stat('demo.txt').st_mtime) # Will give last update time in seconds

# For getting in general timestamp version import datetime from datetime library
from datetime import datetime
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


for dirpath, dirnames, filenames in os.walk('/Users/786/Desktop/Projects/dir_name_2'): # Will give all the directories and sub directories and the files present in the given path and childs in it.
      print('Current path: ', dirpath)
      print('Directories: ', dirnames)
      print('Files: ', filenames)
      print()


print(os.environ) # To get all the envoirnment names list 

for i in os.environ:
      print(i)

print(os.environ.get('USERPROFILE')) # To get the user's profile envoirnment. For example right now getting the envoirnment of the variable HOMEPATH


# Going to create a new profile in USERPROFILE envoirnment.
filepath = os.path.join(os.environ.get('USERPROFILE'),'test.txt')
print(filepath)
with open(filepath, 'w') as f: 
      f.write('Hello from VS Code.')
os.chdir(os.environ.get('USERPROFILE'))
os.listdir()


os.path.basename(filepath) # In my path the basename would be test.txt
os.path.split(filepath) # It will divide the given path into environment and the basename of the file 
os.path.split('/tmp/dir_1/files/file')

os.path.exists('/tmp/dir_1/files/file') # To check availability of the file by using it's path.
os.path.exists(filepath)

os.path.isdir(filepath) # To check is the given path pointing to directory
os.path.isdir(os.environ.get('USERPROFILE')) 


os.path.isfile(filepath) # To check the given path is pointing to a file.

os.path.splitext(filepath) # Will give the path of the file from the given path and the type of the file.
