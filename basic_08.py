from datetime import datetime
from datetime import timedelta
from re import L
from dateutil.parser import parse
import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
from pandas.tseries.offsets import Day, MonthEnd
import pytz


def date():
    longer_ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods = 1000))
    print("\nrandom 1000 dates from 1/1/2000:\n", longer_ts)
    
    print("\nJune of 2001:\n", longer_ts['2001-06'])
    
    
def date_02():
    dates= pd.date_range('1/1/2000', periods = 100, freq = 'W-WED') #every Wednesday
    long_df = pd.DataFrame(np.random.randn(100, 4), 
                           index = dates, columns = ['Colorado', 'Texas', 'New York', 'Ohio'])
    
    print("\nprinting out wednesdays of May 2001:\n", long_df.loc['5-2001'])
    
#중복된 색인을 갖는 시계열 찾기
def duplicates():
    dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000',])
    dup_ts = pd.Series(np.arange(5), index = dates)
    
    print("\ndate:\n", dup_ts)                              
    
    print("\nunique?:\n", dup_ts.index.is_unique) # .is_unique -> returns boolean whether it's true or false
    
def resample():
    dates = [datetime(2011,1, 2), datetime(2011, 1, 5), datetime(2011, 1, 17)
             , datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
    ts = pd.Series(np.random.randn(6), index = dates)
    print(ts)
    
    # .resample -> 시계열을 고정된 일 빈도로 변환할때 이용
    resampler = ts.resample('D')
    
def date_03():
    #날짜 범위 생성하기
    index = pd.date_range('2012-04-1', '2012-06-01')
    print("\nranged index:\n", index)
    
    print("\n20 days from 2012-04-01:\n", pd.date_range(start = '2012-04-01', periods = 20))

    #freq = 'BM' -> 각월 영업 마감일 빈도값으로 전달
    print("\nonly the end dates of each month:\n", pd.date_range('2000-01-01', '2000-12-01', freq = 'BM'))
    
def freq():
    print("finding frequency by 4 hours:\n", pd.date_range('2000-01-01', '2000-01-03 23:59', freq = '4h'))
    
    print("\nfinding 10-period frequency by an hour and half:\n", pd.date_range('2000-01-01', periods = 10, freq = '1h30min'))
    
    #'M' : MonthEnd, 'BM' : BusinessMonthEnd
    #월별 주차(WOM)
    rng = pd.date_range('2012-01-01', '2012-09-01', freq = 'WOM-3FRI')
    print("\nlist of third fridays of each month:\n", list(rng))
    
def shift():
    ts = pd.Series(np.random.randn(4), index = pd.date_range('1/1/2000', periods = 4, freq = 'M'))
    print("\noriginal timestamp: \n", ts)
    print("\nshifted ts:\n", ts.shift(2))
    print("\nshifted backwards ts:\n", ts.shift(-2))
    
def shift_02():
    now = datetime(2022, 2, 18)
    print("\nthree days from 2022-02-18:\n", now + 3 * Day())          
    print("\nthe end of the month of 2022-02-18:\n", now + MonthEnd())
    
def groupby():
    offset = MonthEnd()
    ts = pd.Series(np.random.randn(20), 
                   index = pd.date_range('1/15/2000', periods = 20, freq ='4d'))
    print("\n20-period by 4 days from 1/15/2000:\n", ts)
    
    print(ts.groupby(offset.rollforward).mean())    
    '''
    ts.groupby(offset.rollforawrd).mean()
    # same as
    ts.resmaple('M').mean()
    '''

def period():
    p = pd.Period(2007, freq = 'A-DEC')
    print(p)
    
    print(p+2)
    
    print((pd.Period('2014', freq = 'A-DEC') - p))

    rng = pd.period_range('2000-01-01', '2000-06-30', freq = 'M')
    print(rng)
    
    print(pd.Series(np.random.randn(6), index = rng))
    
def period_02():
    p = pd.Period('Aug-2007', 'M')
    
    print(p.asfreq('A-JUN'))
    
'''
#resample : 빈도 변환과 관련된 모든 작업에서 유용.
resample 호출하여 데이터를 그룹 짓고 요약함수를 적용하는 식.
'''

def resample_02():
    rng = pd.date_range('2000-01-01', periods = 100, freq = 'D')
    ts = pd.Series(np.random.randn(len(rng)), index= rng)
    
    print("\noriginal date: \n", ts)

    print("\n", ts.resample('M').mean())
          
    print("\n", ts.resample('M', kind = 'period').mean())

#down-sampling
def down():
    rng = pd.date_range('2000-01-01', periods = 12, freq = 'T')
    ts = pd.Series(np.arange(12), index = rng)
    
    print(ts)
    



if __name__ == "__main__":
    print("2022_02_18")
    
    #date()
    #date_02()
    #duplicates()
    #resample()
    #date_03()
    #freq()
    #shift()
    #shift_02()
    #groupby()
    #period()
    #period_02()
    #resample_02()
    down()
    