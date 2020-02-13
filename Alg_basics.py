# Time conversion from 12 hour to 24 hour format
import re
def timeConversion(s):
    x = re.findall(r"[^\W\d_]+|\d+", s)
    dn = x[-1]
    h = x[0]
    m = x[1]
    s = x[2]
    if dn =='AM':
        if h == '12':
            print('00'+':'+m+':'+s)
        else:
            print(h+':'+m+':'+s)
    else:
        if h=='12':
            print('12'+':'+m+':'+s)
        else:
            h = int(h)+12
            h = str(h)
            print(h+':'+m+':'+s)
timeConversion('12:45:54PM')
