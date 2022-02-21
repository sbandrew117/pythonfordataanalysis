import numpy as np; import pandas as pd
from sympy import ordered


def practice():
    values = pd.Series(['apple', 'orange', 'apple', 'apple'] *2)
    
    print("\noriginal series:\n", values)
    print("\nunique values: \n", pd.unique(values))
    print("\ncounting each unique values:\n", pd.value_counts(values))
    
    a = pd.Series([0, 1, 0, 0] * 2)
    b = pd.Series(['apple', 'orange'])
    
    print(b.take(a))
    
def practice_02():
    fruits = ['apple', 'orange', 'apple', 'apple'] * 2
    n = len(fruits) #Out[]: 8
    df = pd.DataFrame({'fruit' : fruits,
                       'basket_id' : np.arange(n),
                       'count' : np.random.randint(3, 15, size = n),
                       'weight' : np.random.uniform(0, 4, size = n)},
                      columns = ['basket_id', 'fruit', 'count', 'weight'])
    print("\noriginal dataframe:\n", df)
    
    fruit_cat = df['fruit'].astype('category')
    print("\nfruit category:\n", fruit_cat)
    
    c = fruit_cat.values
    print("\ntype:\n", type(c))
    
    print(c.codes)
    
    df['fruit'] = df['fruit'].astype('category')
    print("\n", df.fruit)
    
    #직접 생성
    my_categories = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])
    print("\nby pd.categorical: \n", my_categories)
    
    #from_codes 함수 이용
    categories = ['foo', 'bar', 'baz']
    codes = [0, 1, 2, 0, 0, 1]
    my_cats_2 = pd.Categorical.from_codes(codes, categories)
    print("\nby from_codes:\n", my_cats_2)
    
    #ordered = True 사용하여 순서 나타내주기
    ordered_cat = pd.Categorical.from_codes(codes, categories, ordered = True)
    print("\nordered = True, ordered cat: \n", ordered_cat)
    
    #as_ordered() 사용하여 순서 나타내주기
    print("\nas_ordered:\n", my_cats_2.as_ordered())
    
    
def calculation():
    np.random.seed(12345)
    draws = np.random.randn(1000)
    print("\ndraws:\n", draws[:5])
    
    # .qcut -> 범주형 데이터 나누기
    bins = pd.qcut(draws, 4) #4 sections 으로 나누기
    print("\nbins:\n", bins)
    
    bins = pd.qcut(draws, 4, labels = ['Q1', 'Q2', 'Q3', 'Q4'])
    print("\nbins with labels:\n", bins)
    
    print("\nbins.codes:\n", bins.codes[:10])

    bins = pd.Series(bins, name = 'quartile')
    results = (pd.Series(draws).groupby(bins).agg(['count', 'min', 'max']).reset_index())
    
    print("\nresults:\n", results)

def practice_03():
    n = 10000000
    draws = pd.Series(np.random.randn(n))
    labels = pd.Series(['foo', 'bar', 'baz', 'qux'] * (n // 4))
    categories = labels.astype('category') #lables를 categorical 하게 바꿔 적은 메모리 사용

def categorical():
    s = pd.Series(['a', 'b', 'c', 'd'] * 2)
    cat_s = s.astype('category')
    print("\ncat_s as categorical:\n", cat_s)
    
    print("\ncodes:\n", cat_s.cat.codes)
    
    print("\ncategories:\n", cat_s.cat.categories)
    
    actual_categories = ['a', 'b', 'c', 'd', 'e']
    cat_s2 = cat_s.cat.set_categories(actual_categories)
    print("\ncat_s2:\n", cat_s2)
    
    print(cat_s.value_counts())
    
    cat_s3 = cat_s[cat_s.isin(['a', 'b'])]
    
    print("\ncat_s3:\n", cat_s3)
    
    print("\nremoved unused categories:\n", cat_s3.cat.remove_unused_categories())
    
def dummy():
    cat_s = pd.Series(['a', 'b', 'c', 'd'] * 2, dtype = 'category')
    print("\ndummies:\n", pd.get_dummies(cat_s)) #pd.get_dummies -> changes 1D categorical data to DataFrame
    
def groupby():
    df = pd.DataFrame({'key' : ['a', 'b', 'c'] * 4,
                       'value' : np.arange(12.)})
    print("\n original dataframe:\n", df)
    
    g = df.groupby('key').value
    print("\n mean of each keys:\n", g.mean())
    
    print("\ntransform: \n", g.transform(lambda x: x.mean()))
    
    print("\n'mean' agg:\n", g.transform('mean'))

    print("\n x = x * 2:\n", g.transform(lambda x: x* 2))
    
    print("\nrank of g:\n", g.transform(lambda x: x.rank(ascending = False)))
    
    def normalize(x):
        return (x - x.mean()) / x.std()

    print("\nnormalized:\n", g.transform(normalize))
    
    print("\n.apply:\n", g.apply(normalize))
    
    #page 497 복습
    
def time():
    n = 15
    times = pd.date_range('2017-05-20 00:00', freq = '1min', periods = n)
    df = pd.DataFrame({'time' : times, 'values' : np.arange(n)})
    
    print("\ntime series data frame:\n", df)
    
    df.set_index('time').resample('5min').count() #'time' 으로 색인한 후 리샘플
    df2 = pd.DataFrame({'time' : times.repeat(3),
                        'key' : np.tile(['a', 'b', 'c'], n),
                        'value' : np.arange(n *3)})
    print("\ndf2:\n", df2[:7])
    
    '''
    time_key = pd.TimeGrouper('5min') #pands.TimeGrouper -> 'key' 의 각 값에 대해 같은 리샘플을 수행
    
    resampled = (df2.set_index('time').groupby(['key', time_key]).sum())
    print("\nresampled:\n", resampled)
    
    '''
    #page 500 다시
    
#method 연결 기법: DataFrame.assign method
'''
#실용적이지 않은 방법
df2 = df.copy()
df2['k'] =v

#실용적인 방법
df2 = df.assign(k = v)
'''
#값을 직접 대입하는 것이 assign 보단 빠름
#하지만 assign 이용시 method 를 연결해서 사용 가능

#page 502 - 504 복습

#pipe method
  
    
    
    
    
    
if __name__ == "__main__":
    #practice()
    #practice_02()
    #calculation()
    #practice_03()
    #categorical()
    #dummy()
    #groupby()
    time()
    