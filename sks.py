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
            first_num_pos = next(re.finditer('\d+', l[2], )).regs[0][0]
            print ("    {:<38} {:<10}{:>5}".format(l[2][:first_num_pos], l[2][first_num_pos:], l[3]))
else:
    print ("Stołówka jest zamknięta :(")

print () # add some padding
