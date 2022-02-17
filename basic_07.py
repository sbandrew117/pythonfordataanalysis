import numpy as np
import pandas as pd

def groupby():
    df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'], 'key2' : ['one', 'two', 'one', 'two', 'one'], 
                        'data1' : np.random.randn(5), 'data2' : np.random.randn(5)})
    print("\noriginal frame: \n", df)
    
    grouped = df['data1'].groupby(df['key1'])
    
    print("\n", grouped.mean)
    
    means = df['data1'].groupby([df['key1'], df['key2']]).mean()
    
    print("\nmeans: \n", means)
    
    states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
    years = np.array([2005, 2005, 2006, 2005, 2006])
    
    #print(states)
    #print(years)
    
    print(df['data1'].groupby([states, years]).mean())
    
    print(df.groupby(['key1', 'key2']).mean())  
    
    for name, group in df.groupby('key1'):
        print("\n", name)
        print("\n", group)
    
    for (k1, k2), group in df.groupby(['key1', 'key2']):
        print("\n", (k1, k2))
        print("\n", group)
        
    grouped_01 = df.groupby(df.dtypes, axis = 1) #grouping by dtype
    for dtype, group in grouped_01:
        print("\ndtype:\n", dtype)
        print("\ngrouped by dtype:\n", group)

def groupby_02():
    people = pd.DataFrame(np.random.randn(5, 5),
                          columns = ['a', 'b', 'c', 'd', 'e'],
                          index = ['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
    people.iloc[2:4, [1, 2]] = np.nan #[2:4 -> row, [1, 2] -> column]
    print("\noriginal data:\n", people)
    
    mapping = {'a' : 'red', 'b' : 'red', 'c' : 'blue',
               'd' : 'blue', 'e' : 'red', 'f' : 'orange'}
    by_column = people.groupby(mapping, axis = 1)
    
    print("\nprinting out the sum of same group of color:\n", by_column.sum())
    
    map_series = pd.Series(mapping)
    
    print("\nseries version of dic map:\n", map_series)
    
    print("\ncounting by people:\n", people.groupby(map_series, axis = 1).count())
     
    print("\ngrouping by length of people's name:\n", people.groupby(len).sum())
    
def groupby_03():
    col = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'], [1, 3, 5, 1, 3]], names = ['cty', 'tenor'])
    hier_df = pd.DataFrame(np.random.randn(4, 5), columns = col)
    print(hier_df)
    
    print("\nprinting out by cty:\n", hier_df.groupby(level = 'cty', axis = 1).count())
    
#pg.396 - pg.408 복습 필요

def fillna_01():
    s = pd.Series(np.random.randn(6))
    s[::2] = np.nan
    print(s)
    print("\nfilling in NaN with mean value:\n", s.fillna(s.mean()))
    
def fillna_02():
    states =  ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
    group_key = ['East'] * 4 + ['West'] * 4
    
    data = pd.Series(np.random.randn(8), index = states)
    
    print(data)
    
    data[['Vermont', 'Nevada', 'Idaho']] = np.nan
    
    print("\nNaN added:\n", data)
    
    fill_mean = lambda g: g.fillna(g.mean())
    
    print("\nfilled with mean:\n", data.groupby(group_key).apply(fill_mean))

def random():
    suits = ['H', 'S', 'C', 'D']
    card_val = (list(range(1,11)) + [10] * 3) * 4
    #print(card_val)   
    base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
    #print(base_names)
    
    cards = []
    for suit in ['H', 'S', 'C', 'D']:
        cards.extend(str(num) + suit for num in base_names)
    
    print("\ncards:\n", cards)   
    deck = pd.Series(card_val, index = cards)
    print("\ndeck: \n", deck[:13])
    
    def draw(deck, n= 5):
        return deck.sample(n)
    
    print("\ndraw: \n", draw(deck))
    
    get_suit = lambda card: card[-1] #last letter as a set
    print("\nlast letter as a set:\n", deck.groupby(get_suit).apply(draw, n = 2))
    
    print("\nrandom two drawn from last letter as a set:\n", deck.groupby(get_suit, group_keys = False).apply(draw, n = 2))
    
def wavg():
    df = pd.DataFrame({'category' : ['a', 'a', 'a', 'a',
                                     'b', 'b', 'b', 'b'],
                       'data' : np.random.randn(8),
                       'weights' : np.random.rand(8)})
    print(df)

    grouped = df.groupby('category')
    get_wavg = lambda g: np.average(g['data'], weights = g['weights'])
    
    print("\ngrouped avg by 'category':\n", grouped.apply(get_wavg))
        
        
if __name__ == "__main__":
    print("2022_02_17")
    
    #groupby()
    #groupby_02()
    #groupby_03()
    #fillna_01()
    #fillna_02()
    #random()
    wavg()
