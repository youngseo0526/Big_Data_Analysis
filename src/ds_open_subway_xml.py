#!/usr/bin/env python
# coding: utf-8
import os
import requests
import urllib
import mylib # NO! src.mylib
import lxml
import lxml.etree
from io import StringIO

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    # (1) make params with resource IDs
    KEY=str(key['dataseoul'])
    TYPE='xml'
    #OLD: SERVICE='SearchSTNBySubwayLineService'
    SERVICE='SearchSTNBySubwayLineInfo'
    LINE_NUM=str(2)
    START_INDEX=str(1)
    END_INDEX=str(10)
    startIndex=1
    endIndex=10
    list_total_count=0    # set later
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
        data=requests.get(url).text
        #tree=lxml.etree.parse(StringIO(data.encode('utf-8')))
        tree=lxml.etree.fromstring(data.encode('utf-8'))
        if(startIndex==1):
            for node in tree.xpath('//list_total_count'):
                list_total_count=int(node.text)
                print ("- Total_count=",list_total_count)
        for node in tree.xpath('//STATION_NM'):
            print (node.text, end=", ")
        startIndex+=10
        endIndex+=10
        if(endIndex > list_total_count):
            print("----- Ending endIndex=", endIndex)
            break

if __name__ == "__main__":
    doIt()
