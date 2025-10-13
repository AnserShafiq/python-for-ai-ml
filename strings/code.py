print('Hello message.')

message = 'Hello message x2'
print(message)

message = 'Hello message x3'
print(message[0:4]) # Setting range of charcters from 0 to index 4

message = 'Hello message x4'
print(message[:-2]) # Setting range of charcters before second last


message = """Hello Mr Mark,
How are you?
Would you like to learn pyhton ?
"""
print(message) # Message in the form of paragraphs

print('Length of last message string: ', len(message)) # Getting number of characters in string


print(message.lower()) # Coverting whole string into lowercase
print(message.upper()) # Coverting whole string into uppercase

print(message.count('you')) #Counting the number of presence of assigned element in the string

print(message.find('Mr')) # Will return the index no of the first letter of value assigned
print(message.find('Universe')) # Will return -1 if value not in the string

message = 'Hello  World'
replacedMessage=message.replace('World', 'Pakistan') # Will replace the word World with word Pakistan, but will not change the value of variable so we need to store it into new one.
print(message)
print(replacedMessage)


combinedMessage = message + ', ' + replacedMessage  # Combining the both variable's values. Using ' ' to keep a space element otherwise there wouldn't be any space
print(combinedMessage)
combinedMessage = '{}, {}'.format(message, replacedMessage)  # One more way of combining
print(combinedMessage)
combinedMessage = f'{message}, {replacedMessage}'  # One more way of combining
print(combinedMessage)