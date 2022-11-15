'''
 데이터 그룹화
'''
from pandas import Series, DataFrame;

emp_dict = [
    {'empno':100, 'name':'마루치', 'job':'IT_PROG'},
    {'empno':120, 'name':'아라치', 'job':'Analysis'},
    {'empno':345, 'name':'을불', 'job':'IT_PROG'},
    {'empno':210, 'name':'창조리', 'job':'Sales'},
    {'empno':197, 'name':'홍길동', 'job':'IT_PROG'},
    {'empno':349, 'name':'마이클', 'job':'Sales'},
    {'empno':445, 'name':'어두일미', 'job':'IT_PROG'},
    {'empno':412, 'name':'오지매', 'job':'Analysis'}
];
df = DataFrame(emp_dict);
print(df);
print('---------------- 그룹화 --------------');
group_job = df.groupby('job');
print(group_job.groups);
print('---------------- 그룹화 출력 --------------');
for name, group in group_job:
    print(name+":"+str(len(group)));
    print(group);
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');

print('---- 간단하게 직종과 인원수만 표현하도록 다시 DataFrame을 만들자 ---');
job_cnt = DataFrame({'count': group_job.size()}).reset_index();
print(job_cnt);



