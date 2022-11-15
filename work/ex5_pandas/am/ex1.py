'''
열 선택!
'''
from pandas import Series, DataFrame;

emp_list = [
    [1001, '일지매', '2000-02-20'],
    [1002, '이지매', '2000-01-09'],
    [1004, '사지매', '2000-04-23'],
    [1003, '삼지매', '2000-11-07']
];

c_name = ['empno', 'ename', 'hdate'];

df = DataFrame.from_records(emp_list, columns=c_name);
print(df);

print('--- df에서 ename만 출력 -----------------------');
print(df['ename']); # print(df.ename);이것 보다는 df['ename']형식이 좋은 것 같다.

print('--- df에서 ename시리즈와 hdate시리즈를 같이 출력 -----------------');
print(df[['ename','hdate']]);

print('--- df에서 모든 행들을 포함하고, 첫번째 열과 두번째 열만 선택 -----');
#  iloc(행범위, 열범위)
print(df.iloc[: , 0:2]);

print('--- 두번째 행과 세번째 행의 정보에서 첫번째 열과 두번째 열만 선택 -----');
print(df.iloc[1:3 , 0:2]);

