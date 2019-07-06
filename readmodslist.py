import readlist
import io
import re
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url=readlist.readlist(input('modname:'))+'/relations/dependencies?filter-related-dependencies=3'
    print(url)
    list1=readlist.listmods(url)
    print(list1)
    input()