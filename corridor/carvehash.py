#!/usr/bin/python3
import re
f=open('curl-res','r').read()
hashes=set(re.findall(r'[a-z0-9]{16,32}',f))
f=open('carves-res.txt','w')
for i in hashes:
    f.write(i+'\n')
f.close()

