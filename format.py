import re
import io

if __name__ == '__main__':
    try:
        fop=open("modslist.json","r")
        sr=fop.read()
        fop.close()
        fope=open("modslist.json","w")
        wr=re.sub('",,"','","',sr)
        fope.write(wr)
        fope.close()
        fo=open("modslist.json","r")
        read=fo.read()
        result=re.sub('",','",\n  ',read)
        pattern1=r"(?<!.){"
        pattern2=r"}(?!.)"
        result=re.sub(pattern1,'{\n  ',result)
        result=re.sub(pattern2,'\n}  ',result)
        fo.close()
        f=open("modslist_format.json","w")
        f.write(result)
        f.close()
    except:
        print('Raised an exception')