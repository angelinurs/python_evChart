fs = open('fileTest.txt', 'w');

fs.write("안녕하세요? increpas입니다."); # 추가 아니고, 기존 데이터들이
        # 삭제되고 지금 쓰기하는 내용으로 대체된다.
fs.close();
