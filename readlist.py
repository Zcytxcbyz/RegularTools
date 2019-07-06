import json
import io
import os
import re
import requests
from bs4 import BeautifulSoup

list1=[]
def readlist(modname):
    try:
        if(modname=='CodeChicken Lib 1.8.+'):
            modname='CodeChicken Lib 1.8'
        fo=open('modslist.json','r')
        jsonData=fo.read()
        pattern='(?<="'+modname+'":").+?(?=")'
        text=re.search(re.compile(pattern),jsonData)
        fo.close()
        return text.group()
    except:
        return 'Raised an exception'

def listscrawler(url):
    try:
        response=requests.get(url)
        content=response.content.decode("utf-8")
        soup=BeautifulSoup(content,"lxml")
        result=soup.find_all('h3',class_="text-primary-500 font-bold text-lg hover:no-underline")
        return result
    except:
        return 'Raised an exception'

def listmods(url):
    try:
        result=listscrawler(url)
        if(len(result)!=0):
            pattern=re.compile(r'(?<=href=").*(?=")')
            for item in result:
                matcher=re.search(pattern,str(item.parent))
                #print(item.text)
                #print(matcher.group())
                list1.insert(len(list1), str(item.text))
                listmods('https://www.curseforge.com'+matcher.group()+'/relations/dependencies?filter-related-dependencies=3')
            return list1
    except:
        return 'Raised an exception'

if __name__ == '__main__':
    filename='modsname.txt'
    if(not os.path.exists(filename)):
        f=open(filename,'w')
        f.close()
    f=open(filename,'r')
    lines=re.split('\n',f.read())
    f.close()
    for line in lines:
        modname=re.sub('\n','',line)
        print(modname)
        url=readlist(modname)+'/relations/dependencies?filter-related-dependencies=3'
        print(url)
        list1=listmods(url)
        if(not(list1 is None or list1=='Raised an exception')):
            print(list1)
            for item in list1:
                f=open(filename,'a')
                f.write('\n'+str(item))
                f.close()
        list1=[]
    f=open(filename,'r')
    lines0=re.split('\n',f.read())
    lines0=list(set(lines0))
    f=open(filename,'w')
    isfrist=True
    for i in lines0:
        if(isfrist):
            f.write(str(i))
            isfrist=False
        else:
            f.write('\n'+str(i))
    f.close()
    input('press any key to exit')