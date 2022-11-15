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
print('------ job에서 중복 제거 -----------------');
print(df.job.unique()); # 중복제거하고 하나씩만 출력
print('----------------------------------------');
print(df.job.value_counts());



