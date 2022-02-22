import numpy as np; import pandas as pd
import patsy
import statsmodels.api as sm
import statsmodels.formula.api as smf


def model_01():
    data = pd.DataFrame({
        'x0' : [1, 2, 3, 4, 5],
        'x1' : [0.01, -0.01, 0.25, -4.1, 0.],
        'y' : [-1.5, 0., 3.6, 1.3, -2]})
    
    print("\n data:\n", data)
    
    print("\nnumpy array form:\n", data.values) # .values -> DataFrame 을 Nympy 배열로 변환
    
    df2 = pd.DataFrame(data.values, columns = ['one', 'two', 'three']) #2차원 ndarray 만들기
    print("\nnumpy ndarray data:\n", df2)
    
    df3 = data.copy()
    
    df3['strings'] = ['a', 'b', 'c', 'd', 'e']
    
    print("\nadding column strings(changing to ndarray):\n", df3)
    
    model_col = ['x0', 'x1']
    # .loc -> 전체 컬럼 중 일부만 사용하고 싶을 때 이용
    print("\n'x0', 'x1': \n", data.loc[:, model_col].values)
    
#Data set에 숫자가 아닌 컬럼이 있다고 가정 후 더미값으로 치환
#더미값으로 치환하고 싶다면 더미값을 생성하고 컬럼을 삭제한 다음 결과와 합쳐야 함
    #example
    data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'],
                                      categories = ['a', 'b'])
    print("\nnew data:\n", data)
    
    dummies = pd.get_dummies(data.category, prefix = 'category')
    data_with_dummies = data.drop('category', axis = 1).join(dummies)
    print("\ndata with dummies:\n", data_with_dummies)
    
def patsy_01():
    data = pd.DataFrame({
        'x0' : [1, 2, 3, 4, 5],
        'x1' : [0.01, -0.01, 0.25, -4.1, 0.],
        'y' : [-1.5, 0., 3.6, 1.3, -2]})
    print("\noriginal data:\n", data)
    
    y, X = patsy.dmatrices('y ~ x0 + x1', data)
    print("\ny:\n", y)
    print("\nX:\n", X)
    
    print("\nwithout intercept:\n", patsy.dmatrices('y ~ x0 + x1 + 0', data)[1]) #0을 더하여 intercept 제거
    coef, resid, _, _ = np.linalg.lstsq(X,y) #np.linalg.lastsq -> 최소자승회귀분석
    

    y, X = patsy.dmatrices('y ~ x0 + np.log(np.abs(x1) + 1)', data)
    #표준화(평균 0, 분산 1)와 센터링(평균값을 뺌)
    #example
    y, X = patsy.dmatrices('y ~ standardize(x0) + center(x1)', data)
    print("\nstandardized and centered:\n", X)
    

    new_data = pd.DataFrame({
        'x0' : [6, 7, 8, 9],
        'x1' : [3.1, -0.5, 0, 2.3],
        'y' : [1, 2, 3, 4]})
    
    new_X = patsy.build_design_matrices([X.design_info], new_data)
    print("\nnew_x:\n", new_X)    
    
def patsy_02():
    data = pd.DataFrame({
        'key1' : ['a', 'a', 'b', 'b', 'a', 'b', 'a', 'b'],
        'key2' : [0, 1, 0, 1, 0, 1, 0, 0],
        'v1' : [1, 2, 3, 4, 5, 6, 7, 8],
        'v2' : [-1, 0, 2.5, -0.5, 4.0, -1.2, 0.2, -1.7]
    })
    
    y, X = patsy.dmatrices('v2 ~ key1', data)
    print("\noriginal v2 ~ key1:\n", X)
    
    #intercept 제거
    y, X = patsy.dmatrices('v2 ~ key1 + 0', data)
    print("\nwithout intercept\n", X)
    
    #산술 컬럼은 C 함수를 이용하여 범주형으로 해석 가능
    y, X = patsy.dmatrices('v2 ~ C(key2)', data)
    print("\ncategorical:\n", X)
    
    # page 516 - 517 복습
'''    
def linear(mean, variance, size = 1):
    if isinstance(size, int):
        size = size
    return mean + np.sqrt(variance) * np.random.randn(*size)
    #동일한 난수 발생을 위해 시드값 직접 지정
    
    '''

    
    
    
    
    
    
    



if __name__ == "__main__":
    #model_01()
    #patsy_01()
    patsy_02()