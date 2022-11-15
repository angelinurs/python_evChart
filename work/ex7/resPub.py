from flask import Flask
from flask_cors import CORS
import requests
import xmltodict
import json

app = Flask( __name__ )
CORS( app )

@app.route( '/' )
def getData():
    zcode = 11
    numOfRows = 20
    serviceKey = 'RqS0Hjv%2B%2F1p4pVpY6HBC%2Fyblgg3WzSz%2B%2Ba2G3m25XrDO3%2Br6ElDZ%2BtkL4GlGf59z3m6%2FYRzGF%2BJBDD0eQvI%2Fgw%3D%3D'
    url = (
        'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo?'
        f'serviceKey={serviceKey}'
        '&pageNo=1'
        f'&numOfRows={numOfRows}'
        f'&zcode={zcode}'
    )

    res = requests.get( url )

    resXml = res.content.decode( encoding='utf-8')
    # print( resXml )

    # to dict
    resJson =  json.dumps(xmltodict.parse(resXml), indent=4, ensure_ascii=False )
    # print( resJson )
    return resJson

if __name__ == '__main__':
    app.run()