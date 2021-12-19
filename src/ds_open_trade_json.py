#!/usr/bin/env python
# coding: utf-8
import os
import requests
import urllib
import mylib

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    # (1) make params with resource IDs
    KEY=key['dataseoul']
    TYPE='json'
    SERVICE='VwsmTrdarFlpopQq'
    START_INDEX=str(1)
    END_INDEX=str(10)
    STDR_YM_CD=str(2017)
    params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,STDR_YM_CD)
    # (2) make a full url
    _url='http://openAPI.seoul.go.kr:8088'
    #url=urllib.parse.urljoin(_url,params)
    url="/".join([_url,params])
    # (3) get data
    r=requests.get(url)
    trade=r.json()
    for e in trade['VwsmTrdarFlpopQq']['row']:
        #print(e['TRDAR_CD_NM'])
        print (e['TRDAR_CD'], e['TRDAR_CD_NM'], e['TOT_FLPOP_CO'], e['ML_FLPOP_CO'], e['FML_FLPOP_CO'])
    #for e in stations['SearchSTNBySubwayLineService']['row']:
        #print e['STATION_CD'], e['STATION_NM'], e['FR_CODE'], e['LINE_NUM']

if __name__ == "__main__":
    doIt()
