import os
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

def series_01():
    obj = pd.Series([4, 7, -5, -3], index = ['a', 'b', 'c', 'd'])
    print(obj)
    print(obj['a'])
    print(obj[obj > 0])

    sdata = {'Ohio' : 1000, 'SF' : 2000, 'NY' : 3000}
    print(sdata)
    
    #사전형 데이터 Series화 하여 배열하기
    obj2 = pd.Series(sdata)
    print(obj2)
    
    #index에 추가
    states = ['Cali', 'San Diego','Oregon', 'NY']
    obj3 = pd.Series(sdata, index = states)
    print(obj3)

    print(obj2 + obj3)
    
    obj.index = ['d', 'c', 'b', 'a']
    print(obj)

def dataframe_01():
    data = {'a' : [1, 2, 3, 4], 'state' : ['NY', 'SF', 'CA', 'NC'], 'yr' : [2001, 2002, 2003, 2004]}
    frame = pd.DataFrame(data)
    print(frame)
    
    #frame.head -> extracts the first five rows
    frame2 = pd.DataFrame(data, columns = ['yr', 'state', 'a'])
    print(frame2)
    
    #extracting certain column
    a = frame2['state']
    print(a)
    
    #column 추가
    val = pd.Series([-1, 2, -3], index = ['0', '2', '3'])
    frame2['num'] = val
    print(frame2)
    
    #finding row's position and values
    #put '' on strings only (.loc[''])
    frame2row = frame2.loc[0]
    print(frame2row)
    
    #changing certain column's values
    frame2['num'] = 1
    print(frame2)
    
    #adding new column by boolean
    frame2['hello'] = frame2.state == 'NY'
    print(frame2)
    
    #deleting a column
    del frame2['hello']
    print(frame2)
    
    #Transpose
    frame3 = frame2.T
    print(frame3)
    
if __name__ == "__main__":
    series_01()
    dataframe_01()