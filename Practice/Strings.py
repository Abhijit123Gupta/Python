print ("hello world loll")                                     #normal print
my_first_string = 'This is my first program' 					
my_second_string = "This is my second program"
my_combined_string = my_first_string + my_second_string        #string concatenation
my_combined_string_1 = my_first_string +'. ' + my_second_string 
print(my_combined_string)
print(my_combined_string_1)
my_multiline_string  = """This is a multiline string           
and it is written in python"""									#multiline string 
print(my_multiline_string)
print(len(my_first_string)) 		#length of the string
print(my_first_string[23])			#extracting the character at different position
print(my_second_string[0:])			#string slicing 
print(my_second_string[0:6])
print(my_second_string[5:7])
print(my_second_string[:])
print(my_combined_string.lower())   #upper case  
print(my_combined_string.upper())	#lower case
my_first_string_uppercase = my_first_string.upper()
print(my_first_string_uppercase)  
print(my_first_string.count('my'))   #counts the occurence of the given parameter
print(my_first_string.count('world')) 
print(my_first_string.find('my'))    #finds the occurence of the given parameter ,return -1 if not found, else returns the position of occurence if found
print(my_first_string.find('z'))
print(my_first_string.replace('program','code'))   #replaces the first parameter with the second int the given string
second_string_mod = my_second_string.replace('program','code')  
print(second_string_mod)
print(my_first_string) 
name = 'abhijit'
greeting = 'Hello'

message = '{}! {}, How are you?'.format(greeting, name)   #string formatting
print(message)

message = f'{greeting}! {name.upper()}, How are you?'    #other way using fstring
print(message)

print(name.islower())