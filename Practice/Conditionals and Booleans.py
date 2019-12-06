if True:     #normal syntax
	print("Ïts a true statement")

language = 'C'

if language == 'Python':        #demonstration of if, elif and else
	print("Language is Python")
elif language == 'Java':
	print("Language is Java")
else: 
	print("Language is neither Python nor Java") 

#switch cases are not present in Python
 
name = 'Abhijit'    # '=' for assignment , '==' for equality
pass_check = False
if name == 'Abhijit' and pass_check:   #logical operators (and, or, not)
	print("Access approved")
else :
	print("Access denied")

if not pass_check:
	print("Enter the right pass_key") 	

a = [1,2,3]
b = [1,2,3]
print(a==b)    #returns 'True'
print(a is b)  #returns 'False' since a and b are two different things in memory 
print(id(a))
print(id(b))   #both ids are different

a = b #now they are same object in memory
print(a==b)  	#True
print(a is b)	#True  id(a) = id(b)

#things that evaluate to false
# 1. False
# 2. None
# 3. 0 of any numeric type
# 4. Any empty sequence . '', (), [].
# 5. Any empty mapping {}

if None :    
	print("Evaluate to true")
else:
	print("Evaluate to false")	
 