import readlist
import requests
import re
import io
import os
from bs4 import BeautifulSoup

if __name__ == '__main__':
    try:
        filename='modsname.txt'
        if(not os.path.exists(filename)):
            f=open(filename,'w')
            f.close()
        f=open(filename,'r')
        lines=re.split('\n',f.read())
        f.close()
        for line in lines:
            url=readlist.readlist(line)
            if(url!='Raised an exception'):
                response=requests.get(url+'/files')
                content=response.content.decode("utf-8")
                soup=BeautifulSoup(content,'lxml')
                result=soup.find_all('span',class_="button__text")
                list1=[]
                list2=[]
                pattern=re.compile(r'.*Download.*')
                for item in result:
                    if(not(item.text is None)):
                        matcher=re.match(pattern,item.text)
                        if(matcher):
                            url0=re.search(re.compile('(?<=href=").+?(?=")'),str(item.parent)).group()
                            if(line=='CodeChicken Lib 1.8.+'):
                                filename0='CodeChicken Lib 1.8.jar'
                            else:
                                filename0=re.search(re.compile('.+\.jar'),str(item.parent.parent.parent.parent.text)).group()
                            break
                response0=requests.get('https://www.curseforge.com'+url0)
                content0=response0.content.decode("utf-8")
                soup0=BeautifulSoup(content0,'lxml')
                result0=soup0.find_all('a')
                pattern0=re.compile(r'.*here.*')
                for i in result0:
                    if(not(i.text is None)):
                        matcher0=re.match(pattern0,i.text)
                        if(matcher0): 
                            url1='https://www.curseforge.com'+re.search(re.compile('(?<=href=").+?(?=")'),str(i)).group()
                            break
                print(url1)
                print(filename0)
                path='modslinks.txt'
                if(not(os.path.exists(path))):
                    f=open(path,'w')
                    f.close()
                fo=open(path,'a')
                fo.write(filename0+','+url1+'\n')
                fo.close()
    except:
        print('Raised an exception')
    finally:
        input('press any key to exit')