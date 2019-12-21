import numpy as np

myArray = np.array([2,4.9,1,0.7,9.0], int)  #int not necessary
print(myArray)        #1D array
print(myArray.dtype)  #if number in array are float it ignores digit after decimal since mentioned type is int

myNewArr = np.array([5, 3.8 ,7 ,1 ,9 ,0])
print(myNewArr)   #since few of the elemts are float hence all are converted into float
print(myNewArr.dtype) #implicit conversion

arr = np.linspace(1,10)
print(arr)
print(len(arr))         #default length of 50, if number of part is not mentioned


arr = np.linspace(1,16, 16)   #(lower,  upper(inclusive), number of parts)
print(arr)

arr = np.arange(1, 15, 2)  #(lower, upper(exclusive), steps)
print(arr)

arr = np.logspace(1, 40, 5) #(lower, upper, 10^1 to 10^40 divided into 5 parts)
print(arr)

arr = np.zeros(10) #arr of size 10 with all zeros
print(arr)

arr = np.ones(5)  #arr of size 10 with all ones
print(arr)

arr = np.ones(5, int) #default is float, we can specifically define data type
print(arr)

my_arr = np.array([3,6,1,8,9])
print(my_arr)
my_arr = my_arr + 5
print(my_arr)

arr_1 = np.array([9,8,7,6,5])
arr_2 = np.array([1,2,3,4,5])
arr_3 = arr_1 + arr_2
print(arr_3)

print(sum(arr_1))
print(np.sin(arr_1))
print(np.sqrt(arr_1))
print(min(arr_1))
print(max(arr_1))
print(np.sort(arr_1))

print(np.concatenate([arr_1, arr_2]))


#COPYING OF ARRAY
arr_1 = np.array([2,3,4,5,6])
arr_2 = arr_1  

print(arr_1)
print(arr_2)
print(id(arr_1))     #both have same address
print(id(arr_2))     #also called Aliasing

arr_1 = np.array([2,3,4,5,6])
arr_2 = arr_1.view()  #creates arr_2 at different loaction from arr_1
print(arr_1)
print(arr_2)
print(id(arr_1))     
print(id(arr_2))     

#SHALLOW COPY
arr_1 = np.array([2,3,4,5,6])
arr_2 = arr_1.view()
arr_1[0] = 10
print(arr_1)
print(arr_2)     #arr_2 also gets modified since its shallow copy
print(id(arr_1))     
print(id(arr_2))     

#DEEP COPY
arr_1 = np.array([2,3,4,5,6])
arr_2 = arr_1.copy()
arr_1[0] = 10
print(arr_1)
print(arr_2)     #arr_2 does not get modified since its deep copy
print(id(arr_1))     
print(id(arr_2))  

print(np.zeros((5,2,3), np.uint8))
		