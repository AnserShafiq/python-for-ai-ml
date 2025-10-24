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
      print(reading_only_single_line,end='')
      
      reading_only_single_line = a.readline()
      print(reading_only_single_line, end='')



with open('test.txt', 'r') as b: 
      read_from_file= b.read()
      print(read_from_file, end='')


with open('test.txt', 'r') as b: 
      read_from_file= b.read(10)
      print(read_from_file)

      read_from_file= b.read(10)
      print(read_from_file)


with open('test.txt', 'r') as b: 
      read_length_limit=20

      read_from_file = b.read(read_length_limit)
      
      while len(read_from_file) > 0: 
            print(read_from_file, end=', ')
            read_from_file = b.read(read_length_limit)
      print()
      print('Used tell command:',b.tell())

with open('test.txt', 'r') as b: 
      read_length_limit=15

      read_from_file = b.read(read_length_limit)
      
      print(read_from_file)
      print('Used tell command:',b.tell())

with open('test.txt', 'r') as b: 
      read_length_limit=10

      read_from_file = b.read(read_length_limit)
      print(read_from_file, end='')
      b.seek(0)
      read_from_file = b.read(read_length_limit)
      print(read_from_file, end=',')
      print()



# Writing
with open('test2.txt', 'w') as f:
      f.write('Test write')

with open('test2.txt', 'w') as f:
      f.write('Test write')
      f.seek(0)
      f.write('check write')