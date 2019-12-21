#LISTS

sports = ['cricket', 'football', 'basketball', 'hockey']
print(sports)       #print list
print(len(sports))  #print length of list
print(sports[0])   #access indivisual member
print(sports[-1])  #-ve indexes roll back from last
print(sports[0:2]) #access range of values first index incluse 2nd exlusive
print(sports[2:])  #slicing

sports.append('kabbadi')  #appending , appends at last
print(sports)

sports.insert(1,'throw_ball') #insert, appends at specified position
print(sports)

sports_2 = ['badminton', 'table_tennis']
sports.insert(0, sports_2)
print(sports)  #list within a list
print(sports[0])   # entire sports_2 list is a member of list sports at position 0

courses = ['EMW', 'ENG', 'Maths', 'DECA']
course_2 = ['AIC', 'ESD']
courses.extend(course_2)  #extends, the list and appends at the last
print(courses)   # the new elements added are indivisual members occupying indivisual position unlike insert

courses.remove('AIC')  #removes any member of list
print(courses)
courses.pop()  #by default removes last member
print(courses)
popped_course = courses.pop() #pop also returns popped member
print(popped_course)
print(courses)

courses.reverse()  #reverses the list
print(courses)

courses.sort()  #sorts the list
print(courses)

num_list = [1,4,2,9,3]
num_list.sort()  #sorts in ascending order
print(num_list)  #sorting this way modifies the original list itself

num_list.sort(reverse = True)  #sorts in descending order
print(num_list)

num_list_1 = [7, 4, 2, 9, 4, 6, 9, 1]
num_list_1_sorted = sorted(num_list_1)
print("num_list_1 is: ",num_list_1)   #original list remains the same
print(num_list_1_sorted)  #sorted list

#for number list, finding min max and sum 
print(min(num_list_1))
print(max(num_list_1))
print(sum(num_list_1))

print(num_list_1.index(2))  #returns the index of member
print(10 in num_list_1)  # in check the availbility of the given member in list 
print(7 in num_list_1)

courses_str = ', '.join(courses) # join each member of list 
print(courses_str)
courses_str = ': '.join(courses)
print(courses_str)

original_courses = courses_str.split(': ')  #recover original list from join
print(original_courses)


#TUPLES

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)  #modifiying list_1 modifies list_2 as well
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)
#tuple_1[0] = 'Art' error cant assign
#since TUPLE is immutable we cant do append/insert/extend and anything that tries to change the tuple



#SETS

sets_cources = {'hindi', 'english', 'maths', 'science'}
print(sets_cources)  #the order of print differs on every execution
# repition of a member in set is ignored while printing
print('hindi' in sets_cources) #more efficient that lists and tuples

sets_cources_1 = {'hindi', 'embedded', 'VLSI', 'maths'}
print(sets_cources_1.intersection(sets_cources))
print(sets_cources_1.union(sets_cources))
print(list(sets_cources_1.difference(sets_cources)))



# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()





