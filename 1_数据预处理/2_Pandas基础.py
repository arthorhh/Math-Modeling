import numpy as np
import pandas as pd

def func1():
    """
    演示 Pandas 基本数据结构：Series 和 DataFrame 的创建与基本操作。
    包括：时间序列索引、混合类型DataFrame构建、数据预览方法。
    """
    a = pd.Series([1,3,5,7,9,np.nan])  # 创建带缺失值的Series
    print(a)
    dates = pd.date_range('20250327',periods=6)  # 生成6个日期的DatetimeIndex
    print(dates)
    df = pd.DataFrame(np.random.random([4,6]),index=list('ABCD'),columns=dates)  # 用随机数创建DataFrame
    print(df)
    df2 = pd.DataFrame({  # 创建包含多种数据类型的DataFrame
        'A':1,  # 标量自动广播
        'B':pd.Timestamp('20250327'),  # 时间戳类型
        'C':pd.Series(1,index=list(range(4)),dtype='float64'),  # 指定类型的Series
        'D':np.array([3]*4,dtype='int64'),  # numpy数组
        'E':pd.Categorical(['first','secend','third','fourth']),  # 分类类型
        'F':'foo'  # 字符串类型
    })
    print('---------------------')
    print(df2)
    print(df2.head(2)) # 显示前两行
    print(df2.tail(2))  # 显示后两行
    print(df2.columns)  # 打印列名
    # 如果后续函数要用df，写 return df 。在下个函数中，写 df = func2()调用获取df

def func2():
    """
    演示 DataFrame 的基本数据分析方法。
    包括：描述性统计、索引排序、值排序。
    """
    df = pd.DataFrame(np.random.random([4, 6]), index=list('ABCD'), columns=pd.date_range('20250327',periods=6))
    print(df)
    print(df.describe().T)  # 转置后的描述性统计
    print(df.sort_index(axis=1,ascending=False))  # 按列名降序排列
    print(df.sort_values(by='2025-04-01'))  # 按指定列的值排序

def func3():
    """
    演示 DataFrame 的多种索引方式。
    包括：列索引、切片索引、标签索引、位置索引、布尔索引。
    """
    df = pd.DataFrame(np.random.random([6, 4]), index = pd.date_range('20250327', periods=6), columns = list('ABCD'))
    print(df)
    print(df['A'],df.A)  # 两种列索引方式
    print(df[0:3])  # 行切片
    print(df.head(1))  # 第一行
    print(df.loc['20250331'],df.loc[:,['A','B']])  # 标签索引
    print(df.loc['20250327':'20250330',['B','D']])  # 标签切片
    print(df.iloc[0,0])  # 位置索引
    df2 = df.copy()
    df2['E'] = ['one','two','three','four','five','six']  # 添加新列
    print(df2)
    print(df2[df2['E'].isin(['two','four'])])  # 布尔索引
    s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20250327',periods=6))
    print(s1)
    df.loc[:, 'D'] = np.array([-1] * 6)  # 整列赋值
    print(df)

def func4():
    """
    演示时间序列操作和DataFrame的数学运算。
    包括：序列位移、对齐运算、聚合/转换操作。
    """
    df = pd.DataFrame(np.random.random([6, 4]), index=pd.date_range('20250327', periods=6), columns=list('ABCD'))
    print(df)
    s = pd.Series([1,3,5,np.nan,6,8],index=pd.date_range('20250327',periods=6))
    print(s,s.shift(2))  # 序列向后位移2位
    print(df.sub(s,axis='index'))  # DataFrame与Series按索引对齐相减
    print(df.agg(lambda x: np.mean(x) * 5.6))  # 每列应用聚合函数
    print(df.transform(lambda x: x * 0))  # 每个元素应用转换函数
    print(df.value_counts())  # 值计数（适用于离散值）

def func5():
    """
    演示DataFrame的分块与合并操作。
    包括：切片分块、concat拼接。
    """
    df = pd.DataFrame(np.random.random([10,4]))
    print(df)
    pieces = [df[:3],df[3:7],df[7:]]  # 将DataFrame分成三块
    print(pieces)
    print(pd.concat(pieces))  # 重新拼接

def func6():
    """
    演示DataFrame的合并操作（merge）。
    重点展示键值重复时的合并行为。
    """
    left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
    print(left)
    right = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [4, 5]})  # 注意重复键值
    print(right)
    print(pd.merge(left,right,on='key'))  # 按key列合并，产生笛卡尔积

def func7():
    """
    演示分组聚合操作（groupby）。
    极其重要的数据分析方法，包括单列和多列分组聚合。
    """
    df = pd.DataFrame({
        'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
        'B':['one','one','two','three','two','two','one','three'],
        'C':np.random.randn(8),
        'D':np.random.randn(8),
    })
    print(df)
    print('-------------------------------------')
    print(df.groupby('A')[['C','D']].sum())  # 按A列分组后对C,D列求和
    # stack/unstack 可用于行列转换（注释掉的备用方法）

def func8():
    """
    演示数据透视表（pivot_table）的创建。
    极其重要的数据透视分析工具，支持多级行列分组。
    """
    df = pd.DataFrame({
        'A': ['one','one','two','three'] * 3,
        'B': ['A','B','C'] * 4,
        'C': ['foo','foo','foo','bar','bar','bar'] * 2,
        'D': np.random.randn(12),
        'E': np.random.randn(12),
    })
    print(df)
    print("----------------------------------")
    # 创建透视表：以D列为值，A,B为行索引，C为列索引
    print(pd.pivot_table(df,values='D',index=['A','B'],columns=['C']))

if __name__=='__main__':
    func8()  # 默认执行透视表示例