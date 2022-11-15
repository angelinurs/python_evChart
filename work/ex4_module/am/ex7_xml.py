'''
이 전에서 만든 test6.xml문서를 읽어서 파싱해 보자
'''
import os;
import xml.etree.ElementTree as ET;

cpath = os.getcwd();
fname = "test6.xml";

tree = ET.parse(cpath+"/"+fname); # 파싱!!

root = tree.getroot(); # 루트엘리먼트 가져오기
print("루트명:{}:{}".format(root.tag,root));

for sub in root:
    print("\t"+sub.tag+":"+sub.text);
    for att in sub.attrib: # 해당 요소의 속성들
        print("\t\t"+sub.tag+"속성:"+att+"="+sub.get(att))


