language = 'python x 2'

if language == 'python': 
      print('Language is python')
elif language == 'python x 2':
      print('Language is python x 2')
else: 
      print('No match')


user = 'Rao'
logged_in = False

if user == 'Rao' and logged_in: 
      print('Rao is logged in')
elif user == 'Rao' and not logged_in:
      print('Rao is not logged in')
else: 
      print('Invalid user') 

user = 'Anser'
if user == 'Anser' or user == 'Rao': 
      print ('Welcome %s' % user)
else: 
      print('Invalid user')