import requests
import re
import os
import io

def download(url,path):
    r=requests.get(url)
    with open(path,"wb") as f:
        f.write(r.content)
        f.close()

if __name__ == '__main__':
        try:
                if(not(os.path.exists('download'))):
                        os.makedirs('download')
                filename='modslinks.txt'
                if(not os.path.exists(filename)):
                        f=open(filename,'w')
                        f.close()
                f=open(filename,'r')
                lines=re.split('\n',f.read())
                f.close()
                for line in lines:
                        list1=re.split(',',str(line))
                        download(list1[1],'download\\'+list1[0])
        except:
                print('Raised an exception')
        finally:
                input('press any key to exit')