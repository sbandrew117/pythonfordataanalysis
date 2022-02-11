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

def series_02():
    obj = pd.Series([1.2, 2.3, 3.4, 4.5], index = ['d', 'b', 'c', 'a'])
    print(obj)
    
    #reindexing -> changing the sequence of the rows
    obj2 = obj.reindex(['a', 'b', 'c', 'd']) #sustaining the values of each rows
    print(obj2)
    
    #ffill -> 누락된 값을 직전의 값으로 채워 넣기
    obj3 = pd.Series(['red', 'blue', 'yellow'], index = [0, 2, 4])
    print(obj3)
    #applying 'ffill' method
    print(obj3.reindex(range(7), method = 'ffill'))

def dataframe_02():
    frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index = ['a', 'c', 'd'], columns = ['ohio', 'texas', 'cali'])
    print(frame)
    #Deleting a certain row
    frame2 = frame.drop(['a'])
    print(frame2)
    #Deleting a certain column (.drop([__] , axis = 'columns'))
    frame3 = frame.drop(['ohio'], axis = 'columns')
    print(frame3)
    #라벨 이름으로 슬라이싱하면 시작점과 끝점을 포함
    frame4 = frame3['a' : 'c']
    print(frame4)
    
def dataframe_series():
    arr = np.arange(12.).reshape(3, 4)
    print (arr)
    print(arr - arr[0]) #broadcasting
    
    frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns = list('bde'),
                         index= ['Utah', 'Ohio', 'Texas', 'Oregon'])
    series = frame.iloc[0]
    print(frame)
    print(series)
    print(frame - series)
    
def series_sort():
    obj = pd.Series(range(3), index = ['e', 'c', 'a'])
    print(obj)
    obj2 = obj.sort_index() #sorting indices of a series
    print(obj2)
    
def frame_sort():
    frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index = ['three', 'one'], columns = ['d', 'a', 'b', 'c'])
    print(frame)
    frame1 = frame.sort_index() #sorting out the index side(row)
    print(frame1)
    frame2 = frame.sort_index(axis = 1)
    print(frame2)
    
def series_sort2():
    obj = pd.Series([4, 7, -3, 2])
    print(obj)
    obj1 = obj.sort_values() #sorting by values bottom to top
    print(obj1)

def frame_sort2():
    frame = pd.DataFrame({'b' : [4, 7, -3, 2], 'a' : [0, 1, 0, 1]})
    print(frame)
    #when more than one column
    frame2 = frame.sort_values(by = 'b')
    print(frame2)
    frame3 = frame.sort_values(by = ['a', 'b'])
    print(frame3)
    
def series_rank():
    obj = pd.Series([7, 1, 2, 3, -4])
    print(obj.rank())
    
#중복되는 색인값 찾기
def duplicated_index():
    obj = pd.Series(range(4), index = ['a', 'a', 'b', 'b'])
    print(obj.index.is_unique) #.is_unique로 중복된 값 있는지 확인 가능


    
if __name__ == "__main__":
    #series_01()
    #dataframe_01()
    #series_02()
    #dataframe_02()
    #dataframe_series()
    #series_sort()
    #frame_sort()
    #series_sort2()
    #frame_sort2()
    #series_rank()
    duplicated_index()
    

