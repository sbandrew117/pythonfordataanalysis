import re
import numpy as np
import pandas as pd

def labeling():
    group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
    ages = [20, 21, 22, 23, 25, 26, 27, 28, 29, 33, 34, 41, 42] 
    bins = [18, 25, 35, 60, 100] #creating categories' range
    
    print("\n", pd.cut(ages, bins, labels = group_names))
    
def example():
    data = np.random.rand(20)
    print(pd.cut(data, 4, precision = 2)) #categories: 4, precision = 2 -> 소수점 아래 2자리
    
#qcut -> 같은 크기의 그룹으로 나눌 때 편이
    data1 = np.random.randn(1000) #정규분포
    cats = pd.qcut(data1, 4) #4 categories
    print("\n", cats)    
    print("\ncounting values:\n", pd.value_counts(cats))

#outlier(특잇값)
def outlier_01():
    data = pd.DataFrame(np.random.randn(1000, 4))
    
    col = data[2] #thrid column = col
    print("\nselect the value that's np.abs(col) > 3:\n", col[np.abs(col) > 3]) # .abs -> 절댓값
    # .any(): to select the whole row that includes .abs(col) > ___
    print("\nselect the rows that include .abs(col) > 3:\n", data[(np.abs(data) > 3).any(1)])
    
    data[np.abs(data) > 3] = np.sign(data) * 3 #assigning those over or under 3 and -3 to 3 and -3
                                               #np.sign(data) -> +/- = assign +1 or -1
    print("\ndescribing data:\n", data.describe())

#permutation -> relocating the "rows"    
def permutation():
    df = pd.DataFrame(np.arange(5*4).reshape((5, 4)))
    sampler = np.random.permutation(5)
    #print(sampler)
    print("\noriginal frame:\m", df)
    print("\ndisplaying row permutation by .take:\n", df.take(sampler)) #.take function
    
    #not permutating but picking out random n rows in a frame
    print("\ndisplaying three random rows:\n", df.sample(n=3)) #picking out 3 random rows
    
    choices = pd.Series([5, 7, -1, 6, 4])
    print("\noriginal series:\n", choices)
    draws = choices.sample(n=10, replace=True) #replace=True -> approves reselection of num                   
    print("\npermutation with reselection:\n", draws)
    
def dummy():
    df = pd.DataFrame({'key' : ['b', 'b', 'a', 'c', 'a', 'b'], 'data1' : range(6)})
    print("\noriginal frame:\n", df)
    print("\ndummy:\n", pd.get_dummies(df['key'])) # .get_dummies -> make the columns a DataFrame or matrix and fill in with 1s and 0s
    
    #pg 294 실습해보기

def string_01():
    val = 'a, b, guido'
    pieces = [x.strip() for x in val.split(',')]
    print("\nstripped and split:\n", pieces)
    
    first, second, third = pieces
    print("\n", first + second + "***and***" + third, "\n")
    print("\nusing .join:\n", '::'.join(pieces)) # .join method -> 일괄적 적용 (strings 사이)    
    
    #.find and .index in strings
    #print(val.index(':')) .index returns error when nothing's found
    print("\n.find found nothing:\n", val.find(':')) #while .find returns -1 when nothing's found
    
    #.count -> 특정 부분문자열이 몇건 발견되었는지 반환
    print("\ncounting ',' in val: \n", val.count(','))
    
    #.replace
    print("\nreplacing ',' with ':' in val: \n", val.replace(',', ' :'))
    
def re_01():
    text = "foo bar\t baz \tqux"
    print("\noriginal text: \n", text)   
    print("\nsplit and spaced with \s+: \n", re.split('\s+', text))
    
#.findall, .search, .match, .sub
def re_02():
    text = """Dave dave@google.com
    Steve steve@gmail.com
    Rob rob@gmail.com
    Ryan ryan@yahoo.com
    """
    pattern = r'[A-Z0-9._%+-] + @[A-Z0-9._%+-] + \.[A-Z]{2, 4}'
    regex = re.compile(pattern, flags = re.IGNORECASE) #re.IGNORECASE -> 정규 표현식이 대소문자를 가리지 않도록 한다.
    
    print(regex.findall(text))
    
    #page 300 참조
    #.findall -> makes a list of all that match
    #.search -> finds the first that match
    #.match -> if the first doesn;t match -> return None
    #.sub ->permutation e.g. print(regex.sub('REDACTED', text))
    #if there's a pattern in a group -> .findall returns a tuple
    
#.contain -> Series 의 str 속성 이용 -> NaN(np.nan) 누락된 값 찾기

#계층적 색인(hierarchical index)
def index_01():
    data = pd.Series(np.random.randn(9), index = [['a','a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 3]])
    print("\nhierarchical index data:\n", data)
    print("\npartial index 'b' from data:\n", data['b'])
    print("\npartial indexing:\n", data['b' : 'c'])
    print("\n", data.loc[['b', 'd']]) # string -> .loc, integer -> .iloc
    
    print("\n", data.unstack()) # .unstack() method -> rearranging the data
    print("\n", data.unstack().stack()) # .stack() method ->re-rearranging the data
    
def index_02():
    frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2, ]], 
                         columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
    print("\noriginal fram:\n", frame)
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    print("\nnew frame:\n", frame)
    
    print(frame.swaplevel('key1', 'key2')) #swapping between 'key1' and 'key2'
    
    #(level = ) option -> useful when you want to get merged(btw same value) column
    print("\n'key2' merged: \n", frame.sum(level = 'key2')) 
    print(frame.sum(level = 'color', axis = 1)) #axis = 'column' or axis = 1 returns added values of same column
    

def merge_01():
    df1 = pd.DataFrame({'key' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1' : range(7)})
    df2 = pd.DataFrame({'key' : ['a', 'b', 'd'], 'data2' : range(3)})
    print("\ndf1: \n", df1)
    print("\ndf2: \n", df2)
    #same column exists ('key')
    print("\nmerged: \n", pd.merge(df1, df2, on = 'key')) #merging two dataframes on = 'key'
    #different column exists
    df3 = pd.DataFrame({'lkey' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1' : range(7)})
    df4 = pd.DataFrame({'rkey' : ['a', 'b', 'd'], 'data2' : range(3)})
    print("\n", pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey')) #left_on, right_on when different names of columns exist
    
    # merging & printing out everything
    print("\nmerge everything:\n", pd.merge(df1, df2, how = 'outer'))
    
   
    
    
if __name__ == "__main__":
    print("2022_02_15")
    
    #labeling()
    #example()
    #outlier_01()
    #permutation()
    #dummy()
    #string_01()
    #re_01()
    #re_02()
    #index_01()
    #index_02()
    merge_01()