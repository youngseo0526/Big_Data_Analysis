#!/usr/bin/env python
# coding: utf-8
import os
import requests
import urllib
import mylib # NO! src.mylib

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    # (1) make params with resource IDs
    KEY=str(key['dataseoul'])
    TYPE='json'
    #OLD: SERVICE='SearchSTNBySubwayLineService'
    SERVICE='InfoTrdarAptQq'
    LINE_NUM=str(2)
    START_INDEX=str(1)
    END_INDEX=str(10)
    startIndex=1
    endIndex=10
    list_total_count=0    # set later
    a = 1
    while True:
        START_INDEX=str(startIndex)
        END_INDEX=str(endIndex)
        #params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
        params="/".join([KEY,TYPE,SERVICE,START_INDEX,END_INDEX,'','',LINE_NUM])
        # (2) make a full url
        _url='http://openAPI.seoul.go.kr:8088' #NOTE slash: do not use 'http://openAPI.seoul.go.kr:8088/'
        #url=urllib.parse.urljoin(_url,params)
        url="/".join([_url,params])
        #print(url)
        # (3) get data
        r=requests.get(url)
        #print(r)
        data=r.json()
        #print(stations)
        if(startIndex==1):
            list_total_count=data['InfoTrdarAptQq']['list_total_count']
            print("- Total Count: ", list_total_count)
        for e in data['InfoTrdarAptQq']['row']:
            print (a,"{0:4}\t{1:4}\t{2:4}\t{3:3}\t{4:5}".format(e['TRDAR_SE_CD_NM'], e['APT_HSMP_CO'], e['PC_6_HDMIL_ABOVE_HSHLD_CO'], e['AVRG_MKTC'], e['TRDAR_CD_NM']))
            a+=1
        startIndex+=10
        endIndex+=10
        if(endIndex > 100):
            print("----- Ending endIndex=",endIndex)
            break  # exit from the while loop

if __name__ == "__main__":
    doIt()
