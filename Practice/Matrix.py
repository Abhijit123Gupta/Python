import numpy as np 

mul_arr = np.array([
					[1,2,3,9,8,7],
					[4,5,6,7,8,9],
					])
print(mul_arr)
print(mul_arr.dtype)
print(mul_arr.ndim)
print(mul_arr.shape) #(rows,columns)
print(mul_arr.size)  #(rows*columns)

sin_arr = mul_arr.flatten()    #multidimensional to single dimensonal
print(sin_arr)

mul_arr_1 = sin_arr.reshape(4,3) #single dimensional to multidimensional
print(mul_arr_1)

m = np.matrix(mul_arr) #with m, matrix operation can be performed
print(m)

n = np.matrix('1 2 3 ; 4 5 6')
print(n)


p = np.matrix('1 2 3; 4 5 6; 7 8 9')
print(p)
print(np.diagonal(p))
print(p.max())
print(p.sum())

p1 = np.matrix('1 0 0; 0 1 0; 0 0 1')
p_mul = p*p1
print(p_mul)







