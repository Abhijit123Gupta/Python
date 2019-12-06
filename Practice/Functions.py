
def hello_func():
	pass			#nothing in function but not blank, no output

print(hello_func)  #returs the address of function in memory
print(hello_func()) #returns the returned value of function (here 'None')

def func():  #function definition
	print("This is a function")

func()     #function call	

def func_ret():
	return 'This is returning'

print(func_ret())  #prints the returned value 
print(len(func_ret())) #length of returned string
print(func_ret().upper()) #modifying returned value

def format_func(greeting, name = 'Abhijit'):  #name is given default value in case no paramter is passed for name , default value is used. If parameter is sent then sent parameter value is used instead of default value
	return '{} {}, Welcome to this function'.format(greeting, name)

print(format_func('Hello','Ayush'))	 #passing parameter 

def student_info(*args, **kwargs):
	print(args)  #positional arguemts   :tuple
	print(kwargs) #keyword arguements   :dictionary
student_info('Maths','Art', name = 'John', age = 22)

#function to check if the year is leap year or not and print number of days in month
months_of_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_name = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

def is_leap(year):
	return (not year % 4 and ((year % 100) or (not year % 400)) )


def day_def(year, month):
	if not 1 <= month <= 12:
		print("Invalid month")
		return
		
	if month == 2 &	 is_leap(year):
		print("The month is:",month_name[month])
		return 29
	
	print("The month is:",month_name[month])
	return months_of_year[month-1]

print(is_leap(2000))
print(day_def(2020, 2))
		




