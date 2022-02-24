import numpy as np; import pandas as pd

def reshape():
    arr = np.arange(8)
    print("\nlist of tuple arr:\n", arr)
    arr2 = arr.reshape((4, -1)) # -1 assumes the right value
    print("\nmatrix arr 4 by 2:\n", arr2)
    arr3 = arr.reshape((4, 2)).reshape((2, -1))
    print("\nmatrix arr 2 by 4:\n", arr3)
    
    #ravel method와 flatten method 는 다차원 배열을 낮은 차원으로 변환
    # .ravel() -> 필요하지 않다면 원본 데이터의 복사본을 생성 x 
    # .flatten() -> 항상 데이터의 복사본을 반환
    
    print("\nraveling:\n", arr.ravel())
    #same as
    print("\nflattening:\n", arr.flatten())
    
    #C and F
    print("\nrow first\n", arr2.ravel('C')) #matrix 의 row 먼저 정렬
    print("\ncolumn first\n", arr2.ravel('F')) #matrix 의 column 먼저 정렬
    
def array():
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    print("\narr1:\n", arr1)
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
    print("\narr2:\n", arr2)
    
    print("\nconcatenate by row:\n", np.concatenate([arr1, arr2], axis = 0))
    print("\nconcatenate by column:\n", np.concatenate([arr1, arr2], axis = 1))
    
    #vstack and hstack
    print("\nvstack:\n", np.vstack((arr1, arr2))) #vstack = concatenate axis = 0
    print("\nhstack:\n", np.hstack((arr1, arr2))) #hstack = concatenate axis = 1
          
    #.split -> [__, __] __: split 하는 위치들
    arr3 = np.random.randn(5, 2)
    print("\n5 by 2 matrix:\n", arr3)
    
    first, second, third = np.split(arr3, [1, 3])
    print("\nfirst:\n", first, "\nsecond:\n", second, "\nthird:\n", third)
    
def array_02():
    arr = np.arange(6)
    arr1 = arr.reshape((3, 2))
    arr2 = np.random.randn(3,2)
    
    print("\nr_:\n", np.r_[arr1, arr2]) #stacks by row
    print("\nc_:\n", np.c_[np.r_[arr1, arr2], arr]) #stacks by column
    
def array_03():
    arr = np.arange(3)
    print("\narr:\n", arr)
    
    print("\nrepeat arr 3 times:\n", arr.repeat(3))
    
    print("\nrepeat respectively:\n", arr.repeat([0, 3, 4]))
    
    arr2 = np.random.randn(2, 2)
    print("\narr2:\n", arr2)
    
    print("\nrepeat arr2 by row:\n", arr2.repeat(2, axis = 0))
    
    print("\nrepeat arr2 respectively by row:\n", arr2.repeat([2, 3], axis = 0))
    
    #tile
    print("\ntile arr2 twice:\n", np.tile(arr2, 2))
    
    print("\ntile by 3 by 2:\n", np.tile(arr2, (3, 2)))
    
    
    #take and put -> take: 단일 축에 대한 값을 선택할 때만 이용 (axis = 1)
    #                put: 평탕화된 배열에 대한 색인을 받음 
def take():
    arr = np.arange(10) * 100
    print("\narr\n", arr)
    
    inds = [7, 1, 2, 6]
    print("\n7th, 1st, 2nd, 6th index in arr:\n", arr[inds])
    
    print("\ntake:\n", arr.take(inds))
    
    arr.put(inds, 42)
    
    print("\nput 42 in inds:\n", arr)
    
    
    #브로드캐스팅은 다른 모양의 배열 간의 산술 연산 수행.
    #page 602 - page 607 복습


def ufunc():
    arr = np.arange(10)
    print(np.add.reduce(arr)) #np.add.reduce() -> 배열의 모든 원소 더하는 방법
    
    print(arr.sum()) #.sum() -> 배열의 모든 원소 더하는 방법
    
def dtype():
    dtype = [('x', np.float64), ('y', np.int32)]
    sarr = np.array([(1.5, 6), (np.pi, -2)], dtype = dtype)
    print("\nsarr:\n", sarr)    
        
    print("\nsarr[0]:\n", sarr[0])
    
    print("\nsarr[0]['y']:\n", sarr[0]['y'])
    
def sort():
    #argsort and lexsort
    values = np.array([5, 0, 1, 3, 2])
    indexer = values.argsort()
    
    print("\nby index:\n", indexer) #argsort() -> sorts by index
    
    print("\nsorted values of index:\n", values[indexer]) #sorts by values of index
    
    #two dimensional example
    arr = np.random.randn(3, 5)
    arr[0] = values
    
    print("\nrandom 3 by 5\n", arr) #0th index is "values"
    
    first_name = np.array(['Bob', 'Jane', 'Steve', 'Bill', 'Barbara'])
    last_name = np.array(['Jones', 'Arnold', 'Arnold', 'Jones', 'Walters'])
    sorter = np.lexsort((first_name, last_name))
    print(sorter)
    
def stable():
    values = np.array(['2 : first', '2 : second', '1 : first',
                       '1 : second', '1 : third'])    
    key = np.array([2, 2, 1, 1, 1])
    
    indexer = key.argsort(kind = 'mergesort')
    
    print(indexer)
    
    print(values.take(indexer))
    
def partial():
    np.random.seed(12345)
    arr = np.random.randn(20)
    print("\nprint the smallest three in the front:\n",
          np.partition(arr, 3)) #첫 세 원소는 해당 배열에서 가장 작은 값
    indices = np.argpartition(arr, 3) #해당 원소의 위치를 반환
    print(indices)
    print(arr.take(indices))
    
def search():
    arr = np.array([0, 1, 7, 12, 15])
    print(arr.searchsorted(9)) #새로운 값을 삽입할 때 정렬된 상태를
    #계속 유지하기 위한 위치를 반환
    
    print(arr.searchsorted([0, 8, 11, 16]))

    arr1 = np.array([0, 0, 0, 1, 1, 1, 1])
    print(arr1.searchsorted([0, 1]))
    print(arr1.searchsorted([0, 1], side = 'right'))
    
    

    
if __name__ == "__main__":
    #reshape()
    #array()
    #array_02()
    #array_03()
    #take()
    #ufunc()
    #dtype()
    #sort()
    #stable()
    #partial()
    search()
    