import os
import re

try:
    fileslist=os.listdir('Temp')
    filename='modslist.json'
    l=len(fileslist)
    a=1
    fo=open(filename,"w")
    fo.write('{')
    fo.close()
    while a<=l:
        for i in fileslist:
            num=re.search(re.compile(r'\d+(?=_)'),i).group(0)
            if(num==str(a)):
                print('Temp\\'+i+'->'+filename)
                f=open('Temp\\'+i,"r")
                text=f.read()
                if(a==l):
                    text=text[1:len(text)-1]
                else:
                    text=text[1:len(text)-1]+','
                f.close()
                fo=open(filename,"a")
                fo.write(text)
                fo.close()
        a+=1
    fo=open(filename,"a")
    fo.write('}')
    fo.close()
    for item in fileslist:
        os.remove('Temp\\'+item)
    os.rmdir('Temp')
except:
    print('Raised an exception')
finally:
    os.system('python format.py')