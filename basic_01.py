import os
import bisect
#string, tuple = immutable

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
    
def list_01():
    a = ['foo', 'bar']
    b = ['baz']
    c = a + b #basic addition
    c.append('foo') #add 'foo' at the end of the list "c"
    c.pop(1) #pop out the vaule of c[1]
    c.remove('foo') #removes from the first of the list
    
    print(c)
    
def list_02():
    a = [1, 3, 5, 4, 2, 34, 8]
    a.sort() #sorts out by small to big
    
    print(a)
    
    b = ['hello', 'hi', 'bye', 'see you']
    b.sort(key=len) #sorts out by the length of each keys
    
    print(b)
    
def bisect_01():
    a = [1, 2, 3, 4, 0]
    bisect.bisect(a, 0)
    
    print(a)
    
def slicing_01():
    a = [2, 3, 4, 2, 3]
    a[0:2] = [1, 2] #remove & add values in respective indices
    
    b = a[:3] #to the (3-1=2)nd index
    c = a[3:] #from the 3rd index
    d = a[-3:-2]
    e = a[::3] #skips by 3
    f = a[::-2] #skips by 2 from the end
    g = a[::-1] #flipped enumeration
    
    print(a)    
    print(b)
    print(c)
    print(d)
    print(e)  
    print(f)
    print(g)
    
def zip_01():
    a = ['foo', 'bar', 'baz']
    b = ['one', 'two', 'three']
    c = list(zip(a, b))
    
    d = ['false', 'true']
    e = list(zip(c, d)) #zipping zipped-list c and list d
    f = list(zip(a, b, d)) #zipping list a, b, d
    
    print(c)
    print(e)
    print(f)

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
        #use "setdefault" method    
        
    print(by_letter)

def dictionary_03():
    d1 = {}
    d1[tuple([1,2,3,4])] = 2 #list -> tuple :to make list as a key
    print(d1)

def set_01():
    s1 = set([2, 2, 2, 2, 1, 3, 4]) #중복값 제거할때 이용? set (집합)
    print(s1)
    
def set_02():
    s1 = set([1, 2, 3, 4]) #set s1
    s2 = {4, 5, 6, 7} #set s2
    s3 = s1.union(s2) #merging two sets
    
    ''' merging two sets:
    s3 = s1 | s2 '''    
    
    print(s3)

    s4 = s1.intersection(s2)
    print(s4)
    
    ''' intersecting two sets:
    s4 = s1 & s2 '''
 
def list_03():
     str1 = ['a', 'b', 'hi', 'hello']
     a = [x.upper() for x in str1 if len(x) > 2]
     print(a)
     
        
if __name__ == "__main__":
    print("2022_02_09")
    
    tuple_01()
    list_01()
    list_02()
    bisect_01()
    slicing_01()
    zip_01()
    dictionary_01()
    dictionary_02()
    dictionary_03()
    set_01()
    set_02()
    list_03()