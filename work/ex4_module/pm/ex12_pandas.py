'''
한 사람의 정보를 우린 다음과 같이 JSON으로 표현한다.
  {
      'empno':101,
      'name':'마루치',
      'hire_date':'1999-10-01'
  }
'''
import pandas as pd;
from pandas import Series, DataFrame;

emp_list = [
  {'empno':101, 'name':'마루치', 'hire_date':'1999-11-02'},  
  {'empno':102, 'name':'아라치', 'hire_date':'1999-01-12'},  
  {'empno':111, 'name':'을불', 'hire_date':'198-05-25'},  
  {'empno':104, 'name':'창조리', 'hire_date':'1999-10-26'},  
  {'empno':121, 'name':'이도', 'hire_date':'1999-10-30'}    
];

df = DataFrame(emp_list);
print(df);

print('-----------컬럼 순서 변경------------------');
df = df[['name', 'hire_date','empno']];
print(df);

print('-----------리스트로 emp_list 변경------------------');
emp_list = [
    [1001, '일지매', '2000-02-20'],
    [1002, '이지매', '2000-01-09'],
    [1004, '사지매', '2000-04-23'],
    [1003, '삼지매', '2000-11-07']
];

c_name = ['empno', 'ename', 'hdate'];

df = DataFrame.from_records(emp_list, columns=c_name);
print(df);
print('----------- DataFrame에서 행을 선택하는 법 ------------------');
print(df.loc[1]); # 두번 째 행의 정보를 가져온다.
print('----------- DataFrame에서 범위로 행을 선택하는 법 ------------------');
print(df.loc[1:3]); # 두번 째 행부터 네번째 행의 정보를 가져온다.

print('-------- DataFrame의 인덱스로 범위를 지정하여 행을 선택하는 법');
print(df[1:3]);# 인덱스 값으로 행들을 선택할 수 있다. 이때
                # 조심해야하는 것은 3번지가 포함되지 않는다는 것이다.

print('-------- DataFrame의 특정 시리즈에 조건을 지정하여 행을 선택하는 법');
#조건을 부여하여 행들을 선택하는 법
print(df[df.empno > 1003]);
print('-----------------------------------');
print(df.query('empno > 1003'));

print('--- empno가 1002번 이상이고, 입사일이 2000년 3월 이후에 입사한 사원');
print(df[(df.empno >= 1002) & (df.hdate >= '2000-03-01')]);





