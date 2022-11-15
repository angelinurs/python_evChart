'''
행과 열을 추가하기
'''
from pandas import Series, DataFrame;

student_dict = [
    {'id':1010, 'name':'마루치', 'Java':89, 'Python':82, 'Flask': 92},
    {'id':1216, 'name':'아라치', 'Java':90, 'Python':88, 'Flask': 95},
    {'id':1023, 'name':'을불', 'Java':79, 'Python':85, 'Flask': 91},
    {'id':1233, 'name':'창조리', 'Java':93, 'Python':89, 'Flask': 92},
    {'id':1708, 'name':'이도', 'Java':95, 'Python':92, 'Flask': 99}
];
df = DataFrame(student_dict);
print(df);
print('--- 각 행의 총점을 구하자 ------');
df['total'] = df['Python'] + df['Java'] + df['Flask'];
print(df);

print('--- 각 행의 평균을 구하자 ------');
df['average'] = df['total']/3;
print(df);

print('--- 각 행의 평균을 가지고 등급을 구하자(평균이 96이상이면 A+ ... ------');
grades = [];
for var in df['average']:
    if var >= 95:
        grades.append('A+');
    elif var >= 90:
        grades.append('A-');
    elif var >= 85:
        grades.append('B+');
    elif var >= 80:
        grades.append('B-');
    elif var >= 75:
        grades.append('C+');
    elif var >= 70:
        grades.append('C');
    elif var >= 60:
        grades.append('D');
    else:
        grades.append('F');

df['grade'] = grades;
print(df);


