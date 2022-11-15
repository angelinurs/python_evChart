
from pandas import Series, DataFrame;

s1 = Series([20,30,60], index=['olleh', 'kt', 'sk']);
s2 = Series([10,40,50], index=['kt', 'sk', 'olleh']);

hap = s1 + s2;

print(hap);