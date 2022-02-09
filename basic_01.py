import os



def tuple_01():
    a = 1, 2, 3
    b = 4, 5, 6
    
    c = a + b #basic addition
    q, w, e = a #divides varient a's 
    w, e = e, w #변수값 치환
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
    b.sort(key=len)
    print(b)
    
if __name__ == "__main__":
    print("2022_02_09")
    
    tuple_01()
    list_01()
    list_02()
    