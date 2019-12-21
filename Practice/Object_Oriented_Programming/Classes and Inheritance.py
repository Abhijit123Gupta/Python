

class Employee:
	pass

#objects of class Employee
emp_1 = Employee()
emp_2 = Employee()

 #both objects have unique address
print(id(emp_1))
print(id(emp_2))

#first_name, last_name, email and pay are the attributes of the class
emp_1.first_name = 'Abhijit'
emp_1.last_name = 'Gupta'
emp_1.email = 'abhijitkumar1417@gmail.com'
emp_1.pay = 36000

emp_2.first_name = 'Deepak'
emp_2.last_name = 'Gharwal'
emp_2.email = 'gharwaldeefaq@gmail.com'
emp_2.pay = 40000

print(emp_1.email)
print(emp_2.email)

#above way of implementation seems longer and prone to errors


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

emp1 = Employee('Abhijit', 'Gupta', 45000, 'abhijitkumar1417')
emp2 = Employee('Deepak', 'Gharwal', 50000, 'gharwaldeefaq@gmail.com')

print(emp1.pay)
print(emp2.pay)


print(Employee.fullname(emp2)) #another way using Class name itself

print(emp1.fullname()) #() is required since its a method

print(emp1.pay_raise())
print(emp2.pay_raise())
print(emp1.raise_percent) #same as class variable 
print(emp2.raise_percent) #same as class variable 


emp2.raise_percent = 5  #creates an insta
print(emp2.raise_percent)
print(emp2.pay_raise())




		




		