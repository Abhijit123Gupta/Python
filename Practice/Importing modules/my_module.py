print('my_module imported')
print("Welcome to my_module")

test_str = 'my name is abd'

def find_index(courses, member):
	index = 0
	for mem in courses:
		if mem == member:
			return index
		index = index + 1
	return -1		