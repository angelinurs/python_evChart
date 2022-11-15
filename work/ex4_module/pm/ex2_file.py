fs = open('fileTest.txt', 'r');

while True: # 무한 반복
    content = fs.readline(); # 파일로부터 데이터를 한줄만 읽어서 content에 저장
    if content != '':# 만약 읽은 데이터가 공백이 아니면...
        print(content, end='');# 화면에 content값을 출력하고 엔터를 공백으로 대체함
    else: # 읽은 자원이 공백일 때
        break;
fs.close();

print('파일 읽기 끝~!');    




