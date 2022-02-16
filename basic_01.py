import numpy as np
import pandas as pd
import bisect

'''
튜플은 1차원의 고정된 크기를 가진 변경 불가능한 순차 자료형.

In[]: tup = 4, 5, 6
In[]: tup
Out[]: (4, 5, 6)

In[]: nested_tup = (4, 5, 6), (7, 8)
In[]: nested_tup
Out[]: ((4, 5, 6), (7, 8))

In[]: tup = tuple([1, [1, 2], 3])
In[]: tup[1].append(3)
In[]: tup
Out[]: (1, [1, 2, 3], 3)

In[]: a= (1, 2, 2, 2, 3, 4, 2)
In[]: a.count() # .count() -> 주어진 값과 같은 값이 몇 개 있는지 반환. 
Outp[]: 4
'''

def tuple_01():
    a = 1, 2, 3
    b = 4, 5, 6
    
    c = a + b #basic addition
    q, w, e = a #divides varient a's 
    w, e = e, w #swap values of the keys
    z = c.count(8) #count
    
    print(c)
    print(q)
    print(w)
    print(z)  

'''
(1, 2, 3, 4, 5, 6)
1
3
0
'''
   
'''
리스트는 크기나 내용의 변경이 가능.
In[]: alist = [1, 2, 3]
In[]: alist.append('dwarf')
In[]: alist
Out[]: [1, 2, 3, 'dwarf']

In[]: alist.insert(2, 'red') # .insert -> 특정 위치에 값을 추가.
In[]: alist
Out[]: [1, 2, 'red', 3, 'dwarf']


***CAUTION***
.insert 는 .append 에 비해 연산비용이 많이 듦.
따라서 양방향 큐인 collections.deque 사용 권장.
'''

def list_01():
    a = ['foo', 'bar']
    b = ['baz']
    c = a + b #basic addition
    c.append('foo') #add 'foo' at the end of the list "c"
    c.pop(1) #pop out the vaule of c[1]
    c.remove('foo') # .remove -> removes from the first of the list (when there's duplication)
    
    print(c)

'''
['baz', 'foo']
'''

def list_02():
    a = [1, 3, 5, 4, 2, 34, 8]
    a.sort() #sorts out by small to big
    
    print(a)
    
    b = ['hello', 'hi', 'bye', 'see you']
    b.sort(key=len) #sorts out by the length of each keys
    
    print(b)

'''
[1, 2, 3, 4, 5, 8, 34]
['hi', 'bye', 'hello', 'see you']
'''

'''
bisect.bisect(list_name, int) 는 integer 이 추가될 때 리스트가 정렬된 상태를 유지할 수 있는 위치를 반환하며,
bisect.insort(list_name, int) 는 실제로 정렬된 상태를 유지한 채 값을 추가한다.
'''    

def bisect_01():
    a = [1, 2, 3, 4, 0]
    print(bisect.bisect(a, 0))
    bisect.insort(a, 0)
    print(a)

'''
0
[0, 1, 2, 3, 4, 0]
'''    

def slicing_01():
    a = [2, 3, 4, 2, 3]
    a[0:2] = [1, 2] #remove & add values in respective indices
    
    b = a[:3] #to the (3-1=2)nd index
    c = a[3:] #from the 3rd index
    d = a[-3:-2]
    e = a[::3] #skips by 3
    f = a[::-2] #skips by 2 from the end
    g = a[::-1] #flipped enumeration
    e = a[-6:-2]
    
    print(a)    
    print(b)
    print(c)
    print(d)
    print(e)  
    print(f)
    print(g)
    print(e)

'''
[1, 2, 4, 2, 3]
[1, 2, 4]
[2, 3]
[4]
[1, 2, 4]
[3, 4, 1]
[3, 2, 4, 2, 1]
[1, 2, 4]
'''

def enumerate_01():
    some_list = ['foo', 'bar', 'baz']
    mapping = {}
    for i, v in enumerate(some_list):
        mapping[v] = i
    print(mapping)
    
'''
{'foo': 0, 'bar': 1, 'baz': 2}
'''

'''
# .zip -> 여러 개의 리스트나 튜플 또는 다른 순차 자료형을 서로 짝지어서 튜플의 리스트를 생성.
리스트의  크기는 넘겨받은 순차 자료형 중 가장 짧은 크기 순.
'''

def zip_01():
    a = ['foo', 'bar', 'baz']
    b = ['one', 'two', 'three']
    c = list(zip(a, b)) # .zip -> 같은 인덱스끼리 짝지어서 튜플의 리스트를 생성.
    
    d = ['false', 'true']
    e = list(zip(c, d)) #zipping zipped-list c and list d
    f = list(zip(a, b, d)) #zipping list a, b, d
    
    print(c)
    print(e)
    print(f)

'''
[('foo', 'one'), ('bar', 'two'), ('baz', 'three')] #튜플의 리스트
[(('foo', 'one'), 'false'), (('bar', 'two'), 'true')]
[('foo', 'one', 'false'), ('bar', 'two', 'true')]
'''

'''
# reversed
In[]: list(reversed(range(10)))
Out[]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
'''

'''
# Dictionary
본질적으로 사전은 2개짜리 튜플로 구성. dict 함수가 2개짜리 튜플의 리스트를 인자로 받아서 사전을 생성.
'''

def dictionary_01():
    d1 = {'a' : 'some value', 'b' : 'hello'}
    print(d1)
    d1['c'] = 'an alphabet' #adding string value via ''
    print(d1)
    d1[3] = 'an integer' #adding integer value
    print(d1)
    print(d1['b']) #print value of key 'b'
    del d1[3] #deleting dic with key 3
    print(d1)
    
    a = list(d1.keys())
    b = list(d1.values())
    print(a)
    print(b)

'''
{'a': 'some value', 'b': 'hello'}
{'a': 'some value', 'b': 'hello', 'c': 'an alphabet'}
{'a': 'some value', 'b': 'hello', 'c': 'an alphabet', 3: 'an integer'}
hello
{'a': 'some value', 'b': 'hello', 'c': 'an alphabet'}
['a', 'b', 'c']
['some value', 'hello', 'an alphabet']
'''

#sorted, reversed method

def dictionary_02():
    words = ['apple', 'banana', 'pineapple', 'watermelon']
    by_letter = {}
    for word in words:
        letter = word[0] #word's first index as letter
        if letter not in by_letter: #if letter is not in the dictionary
            by_letter[letter] = [word] #dictionary by_letter has a key of letter and a word of value
        else:
            by_letter[letter].append(word)
        #if - else -> by_letter.setdefault(letter, []).append(word)
        #use ".setdefault" method    
        
    print(by_letter)

'''
{'a': ['apple'], 'b': ['banana'], 'p': ['pineapple'], 'w': ['watermelon']}
'''

'''
사전의 값으로는 해시 가능해야 함. 즉, 튜플이나 스칼라형(정수, 실수, 문자열)처럼 바뀌지 않는 객체만 가능.
리스트를 키로 이용하기 위한 한가지 방법: 튜플로 변경.
'''

def dictionary_03():
    d1 = {}
    d1[tuple([1,2,3,4])] = 2 #list -> tuple :to make list as a key
    print(d1)

'''
{(1, 2, 3, 4): 2}
'''

def set_01():
    s1 = set([2, 2, 2, 2, 1, 3, 4]) #중복값 제거할때 이용? set (집합)
    print(s1)
    
'''
{1, 2, 3, 4}
'''

def set_02():
    s1 = set([1, 2, 3, 4]) #set s1
    s2 = {4, 5, 6, 7} #set s2
    s3 = s1.union(s2) # .union -> merging two sets
    
    ''' merging two sets:
    s3 = s1 | s2 '''    

    print(s3)

    s4 = s1.intersection(s2) #교집합
    print(s4)
    
    ''' intersecting two sets:
    s4 = s1 & s2 '''

'''
{1, 2, 3, 4, 5, 6, 7}
{4}
'''
 
def list_practice_01():
     str1 = ['a', 'b', 'hi', 'hello']
     a = [x.upper() for x in str1 if len(x) > 2]
     print(a)
     
'''
['HELLO']
'''      
  
if __name__ == "__main__":
    print("2022_02_09")
    
    #tuple_01()
    #list_01()
    #list_02()
    #bisect_01()
    #slicing_01()
    #enumerate_01()
    #zip_01()
    #dictionary_01()
    #dictionary_02()
    #dictionary_03()
    #set_01()
    #set_02()
    list_practice_01()
    