'''
매번 파일을 닫기 하는 것이 번거롭다면
다음의 with문을 사용하자!
'''
with open('fileTest.txt', 'r') as fs: #fs = open('fileTest.txt', 'r');와 같다
    content = fs.read();
    
# 자동적으로 닫기가 이루어 지므로 닫기는 생략해도 된다.
print(content);    