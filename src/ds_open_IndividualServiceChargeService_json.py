#!/usr/bin/env python
#coding: utf-8
import sys
import os
import requests
import urllib
import mylib # NO! src.mylib
    
def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    # (1) make params with resource IDs
    KEY=str(key['dataseoul'])
    # api
    TYPE='json'
    SERVICE='IndividualServiceChargeService'
    START_INDEX=str(1)
    END_INDEX=str(10)
    startIndex=1
    endIndex=10
    list_total_count=0
    
    while True:
        #sys.stdout = open('src/ds_open_IndividualServiceChargeService_xml.txt', 'w')
        START_INDEX=str(startIndex)
        END_INDEX=str(endIndex)
        params="/".join([KEY,TYPE,SERVICE,START_INDEX,END_INDEX])
        _url='http://openAPI.seoul.go.kr:8088' 
        url="/".join([_url,params])
        r=requests.get(url)
        charge=r.json()
        if(startIndex==1):
            list_total_count=charge['IndividualServiceChargeService']['list_total_count']
            print("---- 가져온 데이터 건 수:", list_total_count)
        startIndex+=10
        endIndex+=10
        if(endIndex > list_total_count):
            for e in charge['IndividualServiceChargeService']['row']:
                print (charge['IndividualServiceChargeService']['row'])
            print("----- Ending endIndex=",endIndex)
            #sys.stdout.close()
            break

if __name__ == "__main__":
    doIt()
