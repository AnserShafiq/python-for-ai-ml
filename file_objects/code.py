import os
f = open('test.txt', 'r')
print(f.mode)
f.close()

os.getcwd()

os.chdir('/Users/786/Desktop/Projects/python-for-ai-ml/file_objects') # Updated the current directory for reading the test.txt present in current folder.

with open('test.txt', 'r') as f:
      f_content = f.read()
      print(f_content) 

with open('test.txt', 'r') as a:
      f_content_as_lines_list = a.readlines()
      print(f_content_as_lines_list)

with open('test.txt', 'r') as a:
      reading_only_single_line = a.readline()
      print(reading_only_single_line)