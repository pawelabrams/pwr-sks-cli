#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import re
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

data = []
r = urlopen('http://aken.pwr.edu.pl/sks/menu_dnia/index.php?prefix=tv')
for line in r:
    line = line.decode('utf-8')
    if line.find('div class="global') > -1:
        data = re.findall(r'<div[^>]*>(.+)</div>', line)
        data = re.findall(r'(<div class="(?:pozycje|global)">)?<div class="([^>]*?)">(.+?)(?:<div class="cena">(.+?)</div>)?</div>', data[0])

if data:
    for l in data:
        if (l[1] == 'groupname'): # nice headers
            print ("\n    "+l[2]+"\n    ---")
        else:
            danie = l[2].split(' ')
            print ("    {:<36} {:<5}{:>5}".format(u' '.join(danie[:-1]), danie[-1], l[3]))
else:
    print ("Stołówka jest zamknięta :(")

print () # add some padding
