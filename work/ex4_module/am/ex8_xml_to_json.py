'''
pip install xmltodict
'''
import os;
import json;
import xmltodict;
from pkg_resources._vendor.jaraco.text import indent

cpath = os.getcwd();
fname = "test6.xml";

f = open(cpath+"/"+fname, "r", encoding='utf-8');
xmlData = f.read();
f.close();
    
print(xmlData); 

print('JSON으로 변환하기');
jsonData = json.dumps(xmltodict.parse(xmlData), indent=4, ensure_ascii=False);
print(jsonData);   



