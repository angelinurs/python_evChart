'''
현재 폴더안에 test_data.tsv라는 파일을 하나 만들자
그안에 3개의 컬럼으로 값을 넣어두자!
'''
import pandas as pd;

df = pd.read_csv('test_data.tsv', sep='\t');#열을 탭으로 구분했다.
# sep이 생략되었다면 구분자가 기본적으로 콤마(,)로 구분한다. 그리고
# sep대신에 delimiter라고 해도 된다. (sep == separator라는 뜻)
print(df);
print('---------df.head(2)----------------');
# 위에서 2개( top2 )를 결과로 얻기 위해서는  다음과 같이 기술한다.
print(df.head(2));

print('---------df.tail(2)-------------');
# 밑에서 2개
print(df.tail(2));

print('-------------------------');
print(type(df.year)); # 자료형이 뭔지 알고 싶을 때

