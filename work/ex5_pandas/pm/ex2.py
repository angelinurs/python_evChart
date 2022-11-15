'''
map함수와 applymap함수

   머신러닝을 하다보면 특정 컬럼의 문자열 값을 숫자로 변경해야 
   하는 경우가 생긴다.
'''
from pandas import Series, DataFrame;

df = DataFrame([
    {'name':'홍길동', 'dept':'개발1'},
    {'name':'일지매', 'dept':'개발3'},
    {'name':'마루치', 'dept':'개발1'},
    {'name':'오지매', 'dept':'개발2'},
    {'name':'김통깨', 'dept':'개발3'},
    {'name':'이도', 'dept':'개발1'}
]);
print(df);
print('---------------------------');
df.dept = df.dept.map({'개발1':1, '개발2':2, '개발3':3 });
print(df);









