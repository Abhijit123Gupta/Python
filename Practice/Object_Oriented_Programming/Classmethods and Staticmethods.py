class Employee(object):
	
	#class variables
	raise_percent = 4

	#these are instance variables
	def __init__(self, first_name, last_name, pay, email):
		self.first_name = first_name 
		self.last_name = last_name
		self.pay = pay
		self.email = email

	#method	
	def fullname(self):
		return '{} {}'.format(self.first_name, self.last_name)

	def pay_raise(self):
		return int(self.pay * (1 + self.raise_percent/100)) #self is used when an object/instance has its own (raise_amount) as an instance variable.  
		#return int(self.pay * (1 + Employee.raise_percent/100))	#Employee(class name) is used when an instance wants to access the class variable.

	@classmethod        #class methods operate on class
	def set_raise_percent(cls, amount):
		cls.raise_percent = amount

	@classmethod
	def from_string(cls, emp_string):
		first, last, pay, email = emp_string.split('-')		
		return cls(first, last, pay, email) #creates a new employee object and returns that object

	@staticmethod     #static methods don't operate on instance and class
	def is_workday(day):
		if day.weekday() ==5 or day.weekday() == 6:
			return False
		else:
			return True	

emp1 = Employee('Abhijit', 'Gupta', 45000, 'abhijitkumar1417')
emp2 = Employee('Deepak', 'Gharwal', 50000, 'gharwaldeefaq@gmail.com')

Employee.set_raise_percent(6) #modifying the class variable using the class method, same as Employee.raise_percent = 6 

print(emp1.raise_percent)
print(emp2.raise_percent)

print(emp1.pay_raise())
print(emp2.pay_raise())

emp_str_1 = 'John-Doe-70000-doe.john@gmail.com'
emp_str_2 = 'Steve-Smith-30000-smith.steve@gmail.com'
emp_str_3 = 'Jane-Doe-90000-doe.jane@gmail.com'


first, last, pay, email = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay, email)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2019, 12, 21)
print(my_date)
print(Employee.is_workday(my_date))