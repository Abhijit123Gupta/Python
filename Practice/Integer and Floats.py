num_int = 5
num_float = 4.78
strn_word = "hello"

print(type(num_int))    # type defines data type 
print(type(num_float))
print(type(strn_word))  

print(4-1)
print(3/2) 
print(3//2)    # // used for floor 
print(3**2)    # 3^2 exponent
print(3%2)     # mod operator

num = 1
num += 10
print(num)
#print(num++)  invalid syntax
print(abs(-(num+1)))     # abs for absolute value
print(round(3.46))	# round off 
print(round(3.51))	# no parameter rounds off to nearest decimal
print(round(4.567, 1))  #round off to 1 decimal point

#comparison operators :returns true or false
print(2>1)
print(2==1)
print(2==2)
num_1 = 4
num_2 = 7
print(num_1 < num_2)

num_1 = '100.4'
num_2 = '200'
print(float(num_1) + int(num_2))  #type casting

str_1 = 100.6
str_2 = 200
print(str(str_1) + ' ' + str(str_2))  #type casting