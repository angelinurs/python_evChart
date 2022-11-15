
from pandas import Series, DataFrame;

ko = Series([5000, 2100, 3000, 7500] , 
            index=['02-01','02-02','02-03','02-04']);

print(ko);
print('------- 인덱스들만 추출 --------------');
# 인덱스들만 추출하여 출력하자
for idx in ko.index:
    print(idx);


print('------- 값들만 추출 --------------');
for v1 in ko.values:
    print(v1);