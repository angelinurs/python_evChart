fs = open('fileTest.txt', 'rb'); # 바이너리 형식으로 읽기 모드
content = fs.read();
fs.close();

print(content);
print('-----------------------------------');
print(content.decode('cp949'));# 바이너리 처리된 자원을 원상태로 decode시킨다
