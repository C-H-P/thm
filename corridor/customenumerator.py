#!/usr/bin/env python3
import requests
import hashlib
success=[]
#replace your ip here
url='http://10.10.118.58/'
#iterate through all numbers from 0 to 50
for i in range(50):
    #create md5 hash of 
    digest=hashlib.md5(str(i).encode()).hexdigest()
    try:
        re=requests.get(url+digest,timeout=5)
    except Exception:
        pass
    #print(re.status_code)
    #print(digest)
    if 200==re.status_code:
        success.append(digest)
print(success)
