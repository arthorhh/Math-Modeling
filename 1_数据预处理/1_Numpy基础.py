import numpy as np

def func1():
    """
    演示 NumPy 数组的基本创建和属性。
    包括：数组整形、类型指定、全零/全一数组生成。
    """
    a = np.arange(15).reshape(3, 5)  # 将0-14的序列整形为3行5列的二维数组
    b = np.arange(15)  # 创建0-14的一维数组
    print(b, a, a.ndim, a.shape, a.dtype, a.size, type(a))  # 打印数组及其维度、形状、数据类型、元素数量、类型
    c = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ], dtype='float64')  # 显式指定数据类型为float64
    print(c)
    d = np.zeros([3, 3], dtype='int64')  # 创建3x3的全零数组，类型为int64
    print(d)
    e = np.ones([3, 3], dtype='int32')  # 创建3x3的全一数组，类型为int32
    print(e)

def func2():
    """
    演示 NumPy 数组的通用函数操作。
    包括：逐元素运算、布尔运算、矩阵乘法。
    """
    a = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print(a**2)    # 逐元素平方
    print(a*2)     # 逐元素乘以2
    print(a < 3)   # 逐元素比较是否小于3（布尔数组）
    print(a*a)     # 逐元素乘法（等价于a**2）
    print(a.dot(2))  # 矩阵乘法（标量乘法，等价于a*2）

def func3():
    """
    演示 NumPy 的数学函数和聚合操作。
    包括：随机数组生成、求和/最小/最大值、指数/三角函数。
    """
    a = np.random.random([2, 3])  # 生成2行3列的随机数组（0-1之间）
    print(a)
    print(a.sum(axis=1))  # 沿行方向求和（axis=1）
    print(a.min())        # 数组最小值
    print(a.max())        # 数组最大值
    print(np.exp(1))      # e^1
    print(np.sin(np.pi/2))  # sin(π/2)
    print(np.cos(0))       # cos(0)
    print(np.sqrt(9))      # 平方根

def func4():
    """
    演示 NumPy 数组的索引和切片操作。
    包括：步长切片、赋值、逆序。
    """
    a = np.arange(10)**3  # 创建0-9的立方数组
    print(a)
    print(a[2:5])         # 切片索引（位置2到4）
    a[2:8:2] = 66         # 从位置2到7，步长为2，赋值为66
    print(a[:-2])         # 切片到倒数第2个元素
    print(a[::-1])        # 逆序数组

def func5():
    """
    演示 NumPy 数组的迭代操作。
    包括：按行迭代、按元素迭代。
    """
    a = np.array([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])
    for row in a:         # 按行迭代
        print(row)
        for col in row:   # 按行内元素迭代
            print(col)

    for elem in a.flat:   # 按扁平化后的元素迭代
        print(elem)

def func6():
    """
    演示数组的重塑和向下取整操作。
    包括：随机数组生成、向下取整、resize调整形状。
    """
    a = np.floor(10 * np.random.random([3, 4]))  # 生成3x4随机数组并向下取整
    a.resize([2, 6])  # 调整形状为2行6列（注意：resize会直接修改原数组）
    print(a)

if __name__ == '__main__':
    func6()  # 默认运行 func6