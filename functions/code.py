def hello_func(): 
      pass

hello_func()

print(hello_func)


def hello_func_2():
      print('Hello function !!')
hello_func_2()


def hello_func_3():
      return 'Hello function !!!'

print(hello_func_3())


def hello_func_4(greeting):
      return '{} function !!!'.format(greeting)

print(hello_func_4('Yo'))

def hello_func_5(greeting, name='You'):
      return '{} {} !!!'.format(greeting, name)

print(hello_func_5('Yo', name='Rao'))


def sending_tuple_and_dict(*tuple, **full_dict):
      print(tuple)
      print(full_dict)

sending_tuple_and_dict('Name','Rao', name='Johnny Bravo', age='28')   # First two should be a part of tuple and second two both with sub-name should be added in the dictionary

subjects = ['Maths', 'English']
info = {
      'name': 'Rao',
      'age': '26',
      'city': 'Lahore',
}

sending_tuple_and_dict(subjects, info)   # Now both subjects and info will get out as a tuple and dictionary will come empty


sending_tuple_and_dict(*subjects, **info) # init highlighted the types so should be assigned to the variable depending upon type
