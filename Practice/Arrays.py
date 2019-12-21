
#List can contain elements of different data types
my_list = ['abd', 12, 'male', 'NITK', 9148550927]
print(my_list)

#Array contains elements of same data type
import array as arr

#2 parameters (type, array elements)
vals = arr.array('i',[-3,5,-7,1,2])  
print(vals)
print(vals.buffer_info())  #gives address and size of array
print(vals.typecode)  #gives type
vals.reverse()
print("Reversed array: ",vals) 

print(vals[0])
print(vals[-1])

for i in range(len(vals)):
	print(vals[i],end =' ')

print()	

for i in vals:
	print(i,end=':')
print()

char_array = arr.array('u',['a', 'e', 'i', 'o', 'u'])
print(char_array)

new_array = arr.array(vals.typecode, (a**3 for a in vals))
print(new_array)

#taking value from user
my_new_arr = arr.array('i',[]) #empty integer array
n = int(input('Enter the length of array: '))
for i in range(n):
	x = int(input('Enter the value of element: '))
	my_new_arr.append(x)

print('My new array is: ',my_new_arr)

number_to_search = int(input('Enter the element in my_new_arr you want to search for: '))
found = 0
for j in range(n):
	if(number_to_search == my_new_arr[j]):
		print('The number is found at index: ',j)
		found = 1
		break

if not found:  
	print('element not found')

print("Index of the value to search in array: ",my_new_arr.index(number_to_search))




