import os



def tuple_01():
    a = 1, 2, 3
    b = 4, 5, 6
    
    c = a + b #basic addition
    q, w, e = a #변수(a)에서의 값 분리
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
    c.append('foo')
    c.pop('foo')
    print(c)
    
if __name__ == "__main__":
    print("2022_02_09")
    
    tuple_01()
    list_01()
    