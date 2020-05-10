# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

import urllib.request

# file url

f="https://raw.githubusercontent.com/anbaee/python-class/master/exercises/12_5e3da4a9846c323216262ca8.txt"

#read file

def read(f):
    
    fl = urllib.request.urlopen(f).read().decode('utf-8')
 
    return fl

#convert to dec
    
def converToDic(fl):
    
    dictoinary={}
    key=sub("r",'=',fl).split('=')
    key= list(map( lambda a:a.strip('\t') , map( lambda a:a.strip('\n') , map( lambda a:a.strip(' ') , key))))
    
    values=findall("r",fl)
            
    for vec,item in enumerate(values,start=0):
        dictoinary[key[vec]]=re.findall(r"([]",item)
        dictoinary[key[vec]]=[float(i)for i in dictoinary[key[vec]]]
                
    return dictoinary

# output
            
print(read(f))
            
        