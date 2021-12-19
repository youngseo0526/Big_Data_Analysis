# coding: utf-8
import os
import mylib # NOTE: do not use 'from src import mylib'
import requests
import re

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    _key=str(key['dataseoul'])

    busstopurl='http://openAPI.seoul.go.kr:8088/'+_key+'/xml/CardBusTimeNew/1/5/202107/7016'
    data=requests.get(busstopurl).text
    p=re.compile('<BUS_STA_NM>(.+?)</BUS_STA_NM>')
    res=p.findall(data)
    for item in res:
        print (item)

    p=re.compile('<.*_NUM>(\d+)</.*_NUM>')
    res=p.findall(data)
    print(" ".join(res))
if __name__ == "__main__":
    doIt()
