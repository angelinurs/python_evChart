'''
특정 컬럼(시리즈)에 None값을 찾아서 다른 값으로
변경해보자!
'''
from pandas import Series, DataFrame;


emp_dict = [
    {'empno':100, 'name':'마루치', 'job':'IT_PROG', 'age':30},
    {'empno':120, 'name':'아라치', 'job':'Analysis', 'age':25},
    {'empno':345, 'name':'을불', 'job':'IT_PROG', 'age':None},
    {'empno':210, 'name':'창조리', 'job':'Sales', 'age':23},
    {'empno':197, 'name':'홍길동', 'job':'IT_PROG', 'age':38},
    {'empno':200, 'name':'창조리', 'job':'IT_PROG', 'age':None},
    {'empno':349, 'name':'마이클', 'job':'Sales', 'age':None},
    {'empno':445, 'name':'어두일미', 'job':'IT_PROG', 'age':29},
    {'empno':213, 'name':'창조리', 'job':'Analysis', 'age':31},
    {'empno':412, 'name':'오지매', 'job':'Analysis', 'age':None}
];
df = DataFrame(emp_dict);
print(df);
print('------------------------------');
print(df.isna()); # 각 셀당 None이 있는 자리만 True로 표현!
print('------------------------------');
print(df.isnull());
print('------ null값을 찾아서 0으로 변환 -------------');
#df.age = df.age.fillna(0);
print(df.age.fillna(0));

print('------ null값을 찾아서 직종의 가운데 나이로 변환 -------------');
df['age'].fillna(df.groupby('job')['age'].transform('median'), inplace=True);
print(df);






