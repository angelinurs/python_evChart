'''
DataFrame 모든 행을 목표로 해서 
전체적으로 변화를 수행할 때 사용하는 함수가 applymap함수다.
'''
from pandas import Series, DataFrame;
import numpy as np;

df = DataFrame([
    {'x':3.2, 'y':-2.8, 'z':-2.1},
    {'x':-3.9, 'y':3.5, 'z':-3.0},
    {'x':1.6, 'y':-4.6, 'z':3.3},
]);
print(df);
print('----------------------');
print(df.applymap(np.around));




