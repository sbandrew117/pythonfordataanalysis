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
    
    print(df['data1'].groupby([states, years]).mean())
    
    print(df.groupby(['key1', 'key2']).mean())  
        
    
    
    
if __name__ == "__main__":
    print("2022_02_17")
    groupby()