import re
import os

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


        
def function_01(x, y, z = 1.5):
    if z > 1:
        print(z * (x + y))
    else:
        print(z / (x + y))

def funct():
    a = []
    for i in range(5):
        a.append(i)      
    print(a)
        
        
#list 정제 (import re)
states = ['AlAbama', 'New Y#ORK!', 'Carolina@@@', 'georgia', 'Gerogia']    
def clean_string(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?@]', '', value)
        value = value.title()
        result.append(value)
    return result
    
#lambda function (복습필요)

#generator
def gen_01(x):
    gen = (x**2 for x in range(10))
    for x in gen:
        print(x, end= " ")
        
        
class Test:
    def __init__(self):
        pass
    
    #returning anyways
    def attempt_float(self, x):
        try:
            return float(x)
        except:
            return x     




if __name__ == "__main__":
    print("2022_02_10")
    test = Test()
    result1 = test.attempt_float(6)
    result2 = test.attempt_float('something')
    
    print(result1)
    print(result2)
    
    
    countlist_01()
    function_01(10, 20, 0.1)
    funct()
    print(clean_string(states))
    gen_01(5)

#아래는 vscode에서의 Numpy 오작동으로 인해 Spyder 에서 작업하였습니다.


import numpy as np

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

def if_else_array():
    #PRINT OUT THE ZIPPED ARRAY
    #IF TRUE = PRINT X, IF FALSE = PRINT Y
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, False, True])
    result = [(x if c else y)
              for x, y, c in zip(xarr, yarr, cond)]
    print(result)
    
#중복된 원소를 배열 내에서 제거하고 남은 원소를 반환하는 법
#테스트 문제 중 하나!
def Test():
    names = np.array(['Bob', 'Joe', 'Bob', 'Will'])
    result = np.unique(names)
    print(result)

def linear_algebra():
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[2, 3], [4, 5], [6, 7]])
    z = x.dot(y) #multiplication of linear algebra btw x and y
    #same as z = np.dot(x, y)
    print(z)
    

if __name__ == "__main__":
    array_test_01()
    if_else_array()
    Test()
    linear_algebra()