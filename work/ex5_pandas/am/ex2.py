'''
행, 열 삭제하기
   - 보통 삭제할 때는 index번호를 가지고 삭제한다.
'''
from pandas import Series, DataFrame;

emp_list = [
    [1001, '일지매', '2000-02-20'],
    [1002, '이지매', '2000-01-09'],
    [1004, '사지매', '2000-04-23'],
    [1003, '삼지매', '2000-01-07']
];

c_name = ['empno', 'ename', 'hdate'];

df = DataFrame.from_records(emp_list, columns=c_name);
print(df);
print('------ 행들 중 첫번째와 세번째 행을 삭제 ------');
print(df.drop([0,2]));

print('------ 입사일이 2000-04-23인 행을 삭제 ------');
copy_df = df[df.hdate != '2000-04-23'];
print(copy_df);

print('------ 입사일이 2000년 01월인 행을 삭제 ------');
# 우선 DataFrame에서 입사일인 hdate라는 시리즈만 선별한다.
# 우선 DataFrame에서 입사일인 hdate라는 시리즈만 선별한다.
ser = df['hdate'];
# print(ser);
# 입사일들 중 2000-01로 시작하는 정보들 가려낸다.
# ser 은 시리즈이며 문자열이 아니다. 즉, 문자열이 가지는 startswith()를
# 사용해서 가려낼 수 있으니 ser 다시 말해 시리즈를 문자열로 전환한 후
# startswith함수를 사용하면 된다.
#print(ser.str.startswith('2000-01'));
print(df[~ser.str.startswith('2000-01')]);
#print(df[ser.str.startswith('2000-01')]);


print('------ 특정 컬럼(시리즈)을 삭제하는 법 -------------');
ddf = df.drop(columns='empno');
print(ddf);
print('-----------------------------');
print(df.drop('hdate', axis=1)); # axis=1이 컬럼(시리즈)을 의미한다.

# 지금까지의 삭제를 해봤지만 실제 DataFrame에는 직접 적용이 안된다.
# 그래서 바로 적용하면서 실행되는 속성이 필요하다. 그것이
# inplace = True
# 이지만 거의 사용하지 않는다.





