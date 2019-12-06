#DICTIONARIES (KEY : VALUE)
my_bio = {'NAME':'Abhijit', 'AGE':19, 'COLLEGE':'NITK', 'CGPA':8.78, 'COURSES':['embedded','VLSI','AIC']}  #VALUE can be anything: strings/integer/lists etc
print(my_bio)
print(my_bio['NAME'])
print(my_bio['COURSES'])

my_bio_new = {1:'Abhijit', 2:19, 3:'NITK', 4:8.78, 5:['embedded','VLSI','AIC']}  #KEY can be integer /strings etc
print(my_bio_new)
print(my_bio_new[1])

#print(my_bio['address'])  gives key error
print(my_bio.get('COLLEGE'))   #get used for same purpose, ie: to get the value corresponding to a key
print(my_bio.get('ADDRESS'))   #additionaly, get indicates if the key is valid or not (returns 'None' if key not present in dictionary)
print(my_bio.get('BLOOD_grp','NOT FOUND'))  #we can set a default value for the keys not present in dictionary

my_bio['PHONE'] = 9148550927  #adding new entry to dictionary
print(my_bio)                 #appends at last

my_bio['AGE'] = 20	#updating the dictionary
print(my_bio)

my_bio.update({'BLOOD_grp':'B+', 'AGE':19, 'CGPA':8.70})  #updates multiple things altogether
print(my_bio)

del my_bio['COURSES']		#deleting a key:value pair
print(my_bio)

my_age = my_bio.pop('AGE')  #also returns the deleted 'value'
print(my_bio) 
print(my_age)

print(len(my_bio))   # number of key value pairs
print(my_bio.keys())	#accesing all keys only
print(my_bio.values())	#accessing all values only
print(my_bio.items())	#accesing all key value pairs

for key, values in my_bio.items():
	print(key,':',values)
