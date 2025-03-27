import numpy as np
import pandas as pd

def func1():
    a = pd.Series([1,3,5,7,9,np.nan])
    print(a)
    dates = pd.date_range('20250327',periods=6)
    print(dates)
    df = pd.DataFrame(np.random.random([4,6]),index=list('ABCD'),columns=dates)
    print(df)
    df2 = pd.DataFrame({
        'A':1,
        'B':pd.Timestamp('20250327'),
        'C':pd.Series(1,index=list(range(4)),dtype='float64'),
        'D':np.array([3]*4,dtype='int64'),
        'E':pd.Categorical(['first','secend','third','fourth']),
        'F':'foo'
    })
    print('---------------------')
    print(df2)
    print(df2.head(2)) # 前两行
    print(df2.tail(2))  # 后两行
    print(df2.columns)
    #如果后续函数要用df，写 return df 。在下个函数中，写 df = func2()调用获取df

def func2():
    df = pd.DataFrame(np.random.random([4, 6]), index=list('ABCD'), columns=pd.date_range('20250327',periods=6))
    print(df)
    print(df.describe().T)
    print(df.sort_index(axis=1,ascending=False))  # 按列，降序
    print(df.sort_values(by='2025-04-01'))

def func3():  # 索引
    df = pd.DataFrame(np.random.random([6, 4]), index = pd.date_range('20250327', periods=6), columns = list('ABCD'))
    print(df)
    print(df['A'],df.A)
    print(df[0:3])
    print(df.head(1))
    print(df.loc['20250331'],df.loc[:,['A','B']])  # 参数索引
    print(df.loc['20250327':'20250330',['B','D']])
    print(df.iloc[0,0])  # 位置索引
    df2 = df.copy()
    df2['E'] = ['one','two','three','four','five','six']
    print(df2)
    print(df2[df2['E'].isin(['two','four'])])  # isin是否包含
    s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20250327',periods=6))
    print(s1)
    df.loc[:, 'D'] = np.array([-1] * 6)
    print(df)

def func4():
    df = pd.DataFrame(np.random.random([6, 4]), index=pd.date_range('20250327', periods=6), columns=list('ABCD'))
    print(df)
    s = pd.Series([1,3,5,np.nan,6,8],index=pd.date_range('20250327',periods=6))
    print(s,s.shift(2))  # 去掉最后两行
    print(df.sub(s,axis='index'))  # df 减 s
    print(df.agg(lambda x: np.mean(x) * 5.6))  # 定义名称为x的函数，按列操作
    print(df.transform(lambda x: x * 0))  # 对每个单元格操作
    print(df.value_counts())

def func5():
    df = pd.DataFrame(np.random.random([10,4]))
    print(df)
    pieces = [df[:3],df[3:7],df[7:]]  # 前三行，三到七行，七到后面的行分成三块
    print(pieces)
    print(pd.concat(pieces))  # 拼起来

def func6():
    left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
    print(left)
    right = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [4, 5]})  # pandas认为这两个foo不是同一个键值，如果一个foo一个bar，结果就只有两行
    print(right)
    # 两张表格合在一起
    print(pd.merge(left,right,on='key'))  # 左边是left，右边是right，以key将二者链接起来

def func7():  # 极其重要 极其重要 极其重要 极其重要 极其重要 极其重要 极其重要 极其重要 极其重要
    df = pd.DataFrame({
        'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
        'B':['one','one','two','three','two','two','one','three'],
        'C':np.random.randn(8),
        'D':np.random.randn(8),
    })
    print(df)
    print('-------------------------------------')
    print(df.groupby('A')[['C','D']].sum())
    #df.stack(),df.unstack() 压缩与解压

def func8():  # 透视表 极其重要 极其重要 极其重要 极其重要 极其重要 极其重要 极其重要 极其重要 极其重要
    df = pd.DataFrame({
        'A': ['one','one','two','three'] * 3,
        'B': ['A','B','C'] * 4,
        'C': ['foo','foo','foo','bar','bar','bar'] * 2,
        'D': np.random.randn(12),
        'E': np.random.randn(12),
    })
    print(df)
    print("----------------------------------")
    # 以D、E的数据为基底，判断AB与C的关系
    print(pd.pivot_table(df,values='D',index=['A','B'],columns=['C']))
    # values聚合列，通常为数据。index行分组，column列分组


if __name__=='__main__':
    func8()