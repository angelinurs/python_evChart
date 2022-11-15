'''
mode
  - 'w' : 쓰기
  - 'r' : 읽기
  - 'a' : 추가
  - 'rb': 바이너리로 읽기
'''
fs = open('fileTest.txt'); # 파일과 연결된 스트림
content = fs.read();
fs.close();

print(content);
