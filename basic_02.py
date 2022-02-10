import re
import os



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
