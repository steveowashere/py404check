#Python 2
#Check if page is 404. 
import urllib.request
import urllib.parse
import time

DownList = open('404List.txt', 'w')
ErrorList = open('ErrorList.txt', 'w')

with open('URLList.txt', 'r', encoding='utf-8') as URLList:
    for item in URLList:
        itemStrip = item.strip('\n,\r')
        ParsedItem = urllib.parse.quote(itemStrip, ':, /,', encoding='utf-8')
        print(time.strftime("[%H:%M:%S]") + ' | Notice: Now checking - ' + itemStrip)
        try:
            a=urllib.request.urlopen(ParsedItem)
            if a.getcode() == 200:
                print(time.strftime("[%H:%M:%S]") + ' | Notice: This page reports okay (200)')
        except urllib.error.URLError as e:
            if e.reason == 'Not Found':
                print(time.strftime("[%H:%M:%S]") + ' | Notice: This page reports not found (404)')
                DownList.write(item)
            elif e.reason != 'Not Found':
                print(time.strftime("[%H:%M:%S]") + ' | Error: ' + e.reason + ' ' + itemStrip)
                ErrorList.write(item)
