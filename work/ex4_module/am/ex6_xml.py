'''
xml문서를 메모리상에 생성한 후 실제 문서로 만들어 보자!
<person>
    <name>마루치</name>
    <phone>010-1212-1111</phone>
</person>
'''
import os;
from xml.etree.ElementTree import Element, dump, SubElement, ElementTree;

# 필요한 엘리먼트들 모두 생성
person = Element('person');
name = Element('name');
phone = Element('phone');

# 문자열을 가지는 엘리먼트들에게 문자열 지정
name.text = '마루치';
phone.text = '010-1212-1111';

# 요소(엘리머트)들 배치
person.append(name); # 하위요소 추가
person.append(phone);

# 하위요소 추가하는 다른 방법
SubElement(person, "addr", p_no='08912').text = "서울";

dump(person); #보여주기

# 여기까지는 메모리상에 존재하는 내용이며, 이제 실제로
# 파일로 남겨보자!
cpath = os.getcwd(); # 현재 파일의 위치
fname = "test6.xml"; # 저장할 파일명
ElementTree(person).write(
    cpath+"/"+fname, encoding="UTF-8", xml_declaration=True);