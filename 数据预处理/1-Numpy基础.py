import numpy as np

def func1():
    a = np.arange(15).reshape(3,5)  #reshape整形成二维数组
    b = np.arange(15)
    print(b,a,a.ndim,a.shape,a.dtype,a.size,type(a))  #ndim维度
    c = np.array([
        [1,2,3],
        [4,5,6]
    ],dtype='float64')
    print(c)
    d = np.zeros([3,3],dtype='int64')
    print(d)
    e = np.ones([3,3],dtype='int32')
    print(e)

def func2():
    a = np.array([
        [1,2,3],
        [4,5,6]
    ])
    print(a**2,a*2,a < 3,a*a,a.dot(2))

def func3():
    a = np.random.random([2,3])
    print(a,a.sum(axis=1),a.min(),a.max())  # 0列1行
    print(np.exp(1),np.sin(np.pi/2),np.cos(0),np.sqrt(9))

def func4():
    a = np.arange(10)**3
    print(a)
    print(a[2:5])
    a[2:8:2]=66
    print(a[:-2])
    print(a[::-1])

def func5():
    a = np.array([
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ])
    for row in a:
        print(row)
        for col in row:
            print(col)

    for elem in a.flat:
        print(elem)

def func6():
    a = np.floor(10*np.random.random([3,4]))  # 向下取整
    a.resize([2,6])
    print(a)


if __name__ =='__main__':
    func6()