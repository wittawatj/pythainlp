# -*- coding: utf-8 -*-
'''
ขอขอบคุณ คุณ Korakot Chaovavanich‎ สำหรับโค้ด word_frequency จาก https://www.facebook.com/photo.php?fbid=363640477387469&set=gm.434330506948445&type=3&permPage=1
'''
from __future__ import absolute_import,division,unicode_literals,print_function
import re,requests
def word_frequency(word):
    url = "http://www.arts.chula.ac.th/~ling/TNCII/corp.php"
    data = {'genre[]':'','domain[]':'','sortby':'perc','p':word}
    r = requests.post(url,data=data)
    pat = re.compile('TOTAL</font>(?s).*?#ffffff">(.*?)</font>')
    n = pat.search(r.text).group(1)
    return int('0'+n.strip())