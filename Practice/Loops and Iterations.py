
#FOR LOOPS

num_list = [1,2,3,5,0]
index = 0
for list_mem in num_list:
	print(index,':',list_mem)
	index = index + 1

# Search program
index = 0
found = False
value_to_search = 7
for list_mem in num_list:
	if list_mem == value_to_search:
		print("Search Successful")
		print("Number found at index: ",index)
		found = True
		break              # use of break 
	index = index + 1

if found == False:
	print("Search Unsuccessful")

#for ignoring a certain iteration depending upon  a condition  
# 'continue' statement can be used		

for list_mem in num_list:
	for characters in 'abhijit':
		print(list_mem,':',characters)

for i in range(10):  #gives a range of value 
	print(i)	#range 0 to 9

for j in range(1, 11): #1 inclusive 11 exclsive
	print(j)	#range 1 to 10


#WHILE LOOPS

x = 0

while x<5:
	print(x)
	x += 1    #shorthand

# 'break' and 'continue' can be used similarily