import numpy as np
import pandas as pd
from sympy import N


#HDF5 format
#: 메모리에 모두 적재할 수 없는 엄청나게 큰 데이터를 아주 큰 배열에서 필요한 작은 부분들만 효과적으로 읽고 쓸 수 있음.
#: format : 'fixed', 'table' -> 'table' = slower
def hdf5():
    frame = pd.DataFrame({'a' : np.random.randn(100)})
    store = pd.HDFStore('mydata.h5')
    store['obj1'] = frame
    store['obj1_col'] = frame['a']
    print(store)
    print(store['obj1'])
    
    store.put('obj2', frame, format = 'table')
    a = store.select('obj2', where = ['index >= 10 and index <= 15'])
    print(a)
    
if __name__ == "__main__":
    #hdf5()
        
#"Data Cleansing"

    from numpy import nan as NA

#Dropping non-available data (the whole row that includes "NA")
def dropna_01():
    data = pd.Series([1, NA, 3.5, NA, 6])
    data_result = data.dropna()
    print(data_result)
    
    data1 = pd.DataFrame([[1, 2, 3], [1, NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
    cleaned = data1.dropna()
    
    print("\n raw data: \n", data1)
    print("\n cleaned data: \n", cleaned)
    
    #dropping the row that's filled "NA" only
    cleaned2 = data1.dropna(how = 'all') #how = 'all' drops the whole row
    print("\n cleaned data_2: \n", cleaned2)   
    
    #dropping the column that's filled "NA" only
    data1[4] = NA
    print("\n added NA column: \n", data1)
    
    cleaned3 = data1.dropna(axis = 1, how = 'all') #use axis = 1 to remove the column that includes "NA" only
    print("\n cleaned data_3(removed column): \n", cleaned3)

#finding certain row
#.loc -> index with strings as an index
#.iloc -> index with integers as an index
 
def dropna_02():
    df = pd.DataFrame(np.random.randn(7, 3))
    df.iloc[:4, 1] = NA
    df.iloc[:2, 2] = NA
    print("\n original df: \n", df)
    
    df2= df.dropna() #dropping every row that includes "NA"
    print("\n cleaned df by .dropna(): \n", df2)   

    df3 = df.dropna(thresh = 2) #thresh = __ -> finding and removing rows that include certain amount of "NA"s
    print("\n cleaned df (removal of rows that include 2 'NA's: \n", df3)

#filing in the position where we detect "NA"

def fillna_01():
    df = pd.DataFrame(np.random.randn(7, 3))
    df.iloc[:4, 1] = NA
    df.iloc[:2, 2] = NA
    print("\n original df: \n", df)
    
    df2 = df.fillna(1) #filling in "NA" with 1
    print("\n filling in 'NA' with 1: \n", df2)
    
    df3 = df.fillna({1: 0.01, 2: 0.02}) #filling in with libraries (key: column num, value: value)
    print("\n filling in 'NA' with dictionaries: \n", df3)
    
    dff = pd.DataFrame(np.random.randn(7, 3))
    dff.iloc[4:, 1] = NA
    dff.iloc[2:, 2] = NA
    dff1 = dff.fillna(method = "ffill") #ffill method -> column 에서의 마지막 값과 같게 fill
    print("\n filling in 'NA' by ffill: \n", dff1)
    
    dff2 = pd.Series([1, NA, 3.5, NA, 7])
    print ("\n", dff2)
    
    dff3 = dff2.fillna(dff2.mean()) #filling in the means of Series data
    print("\n filling in by means: \n", dff3)
    
#"Eliminating Duplication" of "rows"
def eli_dup_row():
    data = pd.DataFrame({'k1' : ['one', 'two'] * 3 + ['two'], 'k2' : [1, 1, 2, 3, 3, 4, 4]})
    print(data)
    print("\n", data.duplicated()) #boolean of duplicated rows(same rows)
    
    #eliminating duplication of rows
    data_result = data.drop_duplicates()
    print("\n cleaned data with no duplicates: \n", data_result)

    data['v1'] = range(7)
    print("\n 'v1' added new data: \n", data)
    print("\n new data: \n", data)
    
    #eliminating duplication of rows in certain columns
    data2 = data.drop_duplicates(['k1'])
    print("\n cleaned by searching thru k1: \n", data2)
    
    #keep = 'last' -> 마지막으로 발견된 값을 반환
    data3 = data.drop_duplicates(['k1', 'k2'], keep = 'last')
    print("\n cleaned by searching thru k1 and k2: \n", data3)
    
#".map method" -> 사전류(dictionary)의 객체나 어떤 함수를 받을 수 있음. --> 부분집합 치환이라 생각하면 됨.
def map_01():
    data = pd.DataFrame({'food' : ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                                   'corned beef', 'Bacon', 'pastrami','honey ham', 'nova lox'],
                         'ounces' : [4, 3, 12, 6, 7.5, 8, 3, 5, 6]}) #original dataframe
    print("\n original data: \n", data)
    meat_to_animal = {
        'bacon' : 'pig',
        'pulled pork' : 'pig',
        'bacon' : 'pig',
        'pastrami' : 'cow',
        'corned beef' : 'cow',
        'honey ham' : 'pig',
        'nova lox' : 'salmon'     
    } #another dictionary
    
    #adding meat_to_animal dictionary to existing original dataframe "data"
    loweredcase = data['food'].str.lower() #lower-casing each values inside the dataframe
    print("\n lower-casing each values of 'food': \n", loweredcase)
    
    data['animal'] = loweredcase.map(meat_to_animal) #adding meat_to_animal by .map to data with the column named 'animal'
    print("\n new data with 'animal' column: \n", data)
    
    #page 280 lambda 함수로 다시 해보기
    
    


if __name__ == "__main__":
    #hdf5()
    #dropna_01()
    #dropna_02()
    #fillna_01()
    #eli_dup_row()
    map_01()
    