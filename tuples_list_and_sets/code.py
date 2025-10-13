# List
cars = ["honda", "corolla", "suzuki", "bmw"]
print("Original list:", cars)

print("cars[1]:", cars[1])

print("Looping through list:")
for car in cars:
    print(car, " -", end=' ')

print(len(cars))

print(cars[2:]) 


cars.append('mercedes')
print(cars)

cars.insert(0,'ford')
print(cars)


cars_2=['fiat','peugot']
cars.extend(cars_2)
print(cars)


cars.remove(cars_2[0])
print(cars)


popped = cars.pop() # Will remove the last value of the list
print(popped)
print(cars)

cars.reverse()
print(cars)

cars.sort()
print(cars)

numbers = [5,2,1,4,3]
numbers.sort()
print(numbers)

numbers.sort(reverse=True) # In ascending order
cars.sort(reverse=True) # In ascending order

print(numbers)
print(cars)


sorted_numbers = sorted(numbers)
sorted_numbers_reverse = sorted(numbers, reverse=True)

print(sorted_numbers) 
print(sorted_numbers_reverse)

print('Minimum from list:', min(numbers))
print('Maximum from list:', max(numbers))
print('Sum of list valus:', sum(numbers))
print('Index of number 5: ', numbers.index(5))
print('Index of number 2: ', numbers.index(2))
print('Check is 6 in our list: ', 6 in numbers)
print('Check is 1 in our list: ', 1 in numbers)

for i in numbers: 
    print(numbers)

for index,car in enumerate(cars):
    print(index, car)
for index,car in enumerate(cars, start=1): # assigning starting index
    print(index, car)


cars_str = (', ').join(cars) # converting list into string
print(cars_str)


list1 = ['a','v', 'b'] 
list2 = list1 # Using list and assigining its values to any other variable is a mutable thing
print(list1, list2)
list1.append('c')
print(list1, list2)


# Tuples - immutable things

tuple1 = ('a','b','d')
tuple2 = tuple1
print(tuple1, tuple2)
# tuple1.append('c') || tuple1[0] = 'c' - can't update or add values in tuples


# Sets 
new_set = {1,2,3,4,5}
print(new_set)