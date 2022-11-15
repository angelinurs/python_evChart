'''
DataFrame 합치기
'''
import pandas as pd;
from matplotlib.pyplot import axis

df1 = pd.DataFrame({
   'name':['홍길동', '마루치', '아라치'],
   'Java':[90,80,95],
   'Python':[76,88,90],
   'Flask':[95, 88, 92] 
}); 
print(df1);
print('-------------------------------');

df2 = pd.DataFrame({
   'name':['홍길동', '마루치', '아라치'],
   'Java':[100,90,100],
   'Python':[100,90,100],
   'Flask':[100, 90, 100],
   'Spring':[100,90,100] 
});
res = pd.concat([df1, df2]);
print(res);
print('-------------------------------');
# 인덱스 값을 재정비하자
res = pd.concat([df1, df2], ignore_index=True);
print(res);
print('-------------------------------');
res = df1.append(df2, ignore_index=True);
print(res);
print('-------------------------------');
res = pd.concat([df1, df2], axis=1 , ignore_index=True);
print(res);

