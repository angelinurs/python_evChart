import os;

cpath = os.getcwd(); # 현재 소스파일의 위치값
print("현재 위치:", cpath);

sub_list = os.listdir(cpath);

for ff in sub_list:
    print(ff);