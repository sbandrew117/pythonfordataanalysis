import re
import numpy as np
import random


'''
배열을 생성하는 방법 array 함수
e.g. list 변환하기
data1 = [1, 2, 3, 4.5]
arr1 = np.array(data1)
print(arr1)
Out[]: array([1, 2, 3, 4.5])

*Numpy 배열 = 행렬화 -> 행렬 모양 체크 : arr1.shape
'''


def countlist_01():
    data = [['john', 'emily', 'mary', 'steven', 'juan'], ['maria', 'javier', 'natalia']]
    names_of_interest = []
    for names in data:
        a = [name for name in names if name.count('e') >= 2]
        names_of_interest.extend(a)
    print(names_of_interest)
    
    #중첩된 리스트 표기법
    #example 1    
    b = [name for names in data for name in names
        if name.count('e') >= 2]
    print(b)
    #example 2
    some_tup = (1, 2, 3), (4, 5, 6), (7, 8, 9)
    to_list = [x for tup in some_tup for x in tup]
    print(to_list)
    #list inside a list example 1
    print([[x for x in tup] for tup in some_tup])

'''
['steven']
['steven']
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
        
def function_01(x, y, z = 1.5):
    if z > 1:
        print(z * (x + y))
    else:
        print(z / (x + y))

'''
In[]: function_01(10, 20, 0.1)
Out[]: 0.0033333333333333335
'''

def funct():
    a = []
    for i in range(5):
        a.append(i)      
    print(a)
        
'''
[0, 1, 2, 3, 4]
'''
        
#list 정제 (import re)
states = ['AlAbama', 'New Y#ORK!', 'Carolina@@@', 'georgia', 'Gerogia    ', " "]    
def clean_string(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?@]', '', value)
        value = value.title()
        result.append(value)
    return result

'''
In[]: print(clean_string(states))
Out[]: ['Alabama', 'New York', 'Carolina', 'Georgia', 'Gerogia', '']
'''    

'''
제너레이터 표현식: 리스트 표현식에서 대괄호를 사용하듯이 괄호를 사용하여 생성.
e.g.
In[]: gen = (x ** 2 for x in ragne(100))
In[]: gen
Out[]: <generator object <genexpr> at 0x7fbbd5ab29e8>
'''

#generator
def gen_01(x):
    gen = (x**2 for x in range(10))
    for x in gen:
        print(x, end= " ")
        
'''
0 1 4 9 16 25 36 49 64 81
'''        

class Test:
    def __init__(self):
        pass
    
    #returning anyways
    def attempt_float(self, x):
        try:
            return float(x)
        except:
            return x     

'''
6.0
something
'''


if __name__ == "__main__":
    print("2022_02_10")
    test = Test()
    result1 = test.attempt_float(6)
    result2 = test.attempt_float('something')
    
    #print(result1)
    #print(result2)
    
    
    #countlist_01()
    #function_01(10, 20, 0.1)
    #funct()
    #print(clean_string(states))
    #gen_01(5)
    

def array_test_01():
    arr = np.arange(20).reshape((4,5))
    arr1 = np.arange(10)
    
    print(arr)
    print(arr1)
    #print(arr[[1, 2][2,3]]) #list indices must be int or slices, not tuple
    x = np.random.randn(8)
    y = np.random.randn(8)
    print(x, y)

    result1 = np.where(arr > 0, 1, -1)
    print(result1)

'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
[0 1 2 3 4 5 6 7 8 9]
[-0.22000406  0.2878691  -0.89907886  2.21600569  0.15967513 -1.66795243
 -0.12422886 -0.02088689] [-1.72379741 -1.07826782  0.06820012 -0.3709512   0.98470964 -0.23824979
  0.30787551 -1.71429559]
[[-1  1  1  1  1]
 [ 1  1  1  1  1]
 [ 1  1  1  1  1]
 [ 1  1  1  1  1]]
'''

def if_else_array():
    #PRINT OUT THE ZIPPED ARRAY
    #IF TRUE = PRINT X, IF FALSE = PRINT Y
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, False, True])
    result = [(x if c else y)
              for x, y, c in zip(xarr, yarr, cond)]
    print(result)

'''
[1.1, 2.2, 1.3, 2.4, 1.5]
'''    

def test_01():
    names = np.array(['Bob', 'Joe', 'Bob', 'Will'])
    result = np.unique(names)
    print(result)

'''
['Bob' 'Joe' 'Will']
'''

def linear_algebra():
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[2, 3], [4, 5], [6, 7]])
    z = x.dot(y) #multiplication of linear algebra btw x and y
    #same as z = np.dot(x, y)
    print(z)

'''
[[28 34]
 [64 79]]
'''    

def random_sample():
    samples = np.random.normal(size=(4, 4))
    print(samples)

'''
[[-0.44813752  1.0182798  -0.77053734 -0.79826741]
 [ 1.43837967  0.65429618  0.99926153  1.86635079]
 [ 0.04928745  0.04533399  0.64782321  0.83900133]
 [ 0.14798192  0.3452549  -1.65998592 -1.01799639]]
'''

def stairs():
    position = 0
    walk = [position]
    steps =1000
    for i in range(steps):
        step = 1 if random.randint(0, 1) else -1
        position += step
        walk.append(position)
    #print(plt.plot(walk[:100]))
    
    
if __name__ == "__main__":
    #array_test_01()
    #if_else_array()
    #test_01()
    #linear_algebra()
    #random_sample()
    

#numpy.random은 큰 표본을 생성할 때 내장 모듈보다 수십 배 이상 빠름.
