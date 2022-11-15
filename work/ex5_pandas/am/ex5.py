'''
 중복 데이터 삭제
'''
from pandas import Series, DataFrame;

emp_dict = [
    {'empno':100, 'name':'마루치', 'job':'IT_PROG'},
    {'empno':120, 'name':'아라치', 'job':'Analysis'},
    {'empno':345, 'name':'을불', 'job':'IT_PROG'},
    {'empno':210, 'name':'창조리', 'job':'Sales'},
    {'empno':197, 'name':'홍길동', 'job':'IT_PROG'},
    {'empno':200, 'name':'창조리', 'job':'IT_PROG'},
    {'empno':349, 'name':'마이클', 'job':'Sales'},
    {'empno':445, 'name':'어두일미', 'job':'IT_PROG'},
    {'empno':213, 'name':'창조리', 'job':'Analysis'},
    {'empno':412, 'name':'오지매', 'job':'Analysis'}
];
df = DataFrame(emp_dict);
print(df);
print('----- 중복 찾기 ---------------');
print(df.duplicated());

print('----- 중복 제거 ---------------');
copy_df = df.drop_duplicates();
print(copy_df);

print('----- 특정 컬럼의 값이 같을 때 제거 ---------------');

print(df.duplicated(['name']));
print('------------------------------------------');
del_df = df.drop_duplicates(['name'], keep='last');# 마지막 것을 살린다.
print(del_df);






