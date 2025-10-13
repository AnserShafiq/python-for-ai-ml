student = { 'name': 'Anser',  'age': '25', 'courses': ['Maths', 'Computer', 'Urdu']}
print(student)

print(student['courses'])
print(student['name'])

print(student.get('name'))
print(student.get('phone', 'No phone data'))

student['phone'] = '0321 09023901'
print(student.get('phone', 'No phone data'))

student['name']='musa'
print(student)

student.update({'name': 'Rao','age': '19', 'hobby':['Swimming', 'Football', 'Cricket']})
print(student)

del student['hobby']
print(student)

age = student.pop('age')
print(student)
print(age)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

print(type(student))

for key,val in student.items(): 
      if type(val) == list:
            print(key, end=': ')
            for i in val: 
                  print(i, end= ', ')
            print('')
      else: 
            print(key,':',val)
      
