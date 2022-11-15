from pandas import Series, DataFrame;

ar_dict = [
    {'b_day':'1983-10-09'},
    {'b_day':'1970-04-22'},
    {'b_day':'2000-12-19'},
    {'b_day':'1999-03-21'},
    {'b_day':'2001-09-09'}
];
df = DataFrame(ar_dict);
print(df);
print('------------------------------');

def clip_year(col):
    return col.split('-')[0];

df['year'] = df['b_day'].apply(clip_year); 
print(df);
print('------------------------------');

def set_age(year, c_year):
    return c_year - int(year);

df['age'] = df['year'].apply(set_age, c_year=2022);
print(df);
print('------------------------------');

def get_age(row):
    return str(row.year)+"년 생은 "+ str(row.age)+"세";

df['etc'] = df.apply(get_age, axis=1);
print(df);

