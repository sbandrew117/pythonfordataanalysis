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
def broadcast():
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    #reshape()
    #array()
    #array_02()
    #array_03()
    #take()
    broadcast()