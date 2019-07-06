# -*- coding: utf-8 -*-
import os
import re
import requests
import lxml
import time
import random
from bs4 import BeautifulSoup

if __name__ == '__main__':
    a=1
    while a<=1:
        try:
            response=requests.get(str('https://www.curseforge.com/minecraft/mc-mods?page='+str(a)))
            content=response.content.decode("utf-8")
            soup=BeautifulSoup(content,"lxml")
            #result=soup.find_all('a')
            result=soup.find_all('h3',class_="text-primary-500 font-bold text-lg hover:no-underline")
            pattern1 = re.compile(r'(?<=href=").*(?=")')
            #pattern2 = re.compile(r'(?<=<h3 class="text-primary-500 font-bold text-lg hover:no-underline">).*(?=</h3>)')
            jsoncode='{'
            for i in result:
                if(re.search('h3',str(i))):
                    matcher1=re.search(pattern1,str(i.parent))
                    #if(matcher1 and matcher2):
                    if(matcher1):
                        print(i.text+" "+matcher1.group())
                        jsoncode+='"'+i.text+'":"https://www.curseforge.com'+matcher1.group()+'",'
            jsoncode=jsoncode[:len(jsoncode)-1]+'}'
            filename=os.getcwd()+'\\Temp\\'+str(a)+'_'+str(int(time.time()))+str(random.randint(0,9))+str(random.randint(0,9))+".json"
            if(not os.path.exists(os.getcwd()+'\\Temp\\')):
                os.makedirs(os.getcwd()+'\\Temp\\')
            fo = open(filename, "w")
            fo.write(jsoncode)
            fo.close()
            print('Write to file "'+filename+'"')
        except:
            print('Raised an exception')
        finally:
            a+=1
    os.system('python mergefiles.py')
