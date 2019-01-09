#!/anaconda3/bin/python3
#/usr/bin/env python3
# nextbus.py

import sys

if len(sys.argv) != 3:
    # e.g., from video: nextbus.py 22 14787
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'
                           .format(route, stopid))
data = u.read()
print(type(data))
print("data is:", data)

from xml.etree.ElementTree import XML
doc = XML(data)

print("doc is:", doc)

# import pdb; pdb.set_trace()    # Launch debugger

for pt in doc.findall('.//pt'):
    print(pt.text)
'''
Connected to pydev debugger (build 183.4886.43)
<class 'bytes'>
data is: b'<?xml version="1.0" encoding="UTF-8"?>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n<stop>\r\n\r\n\t<id>14787</id> \r\n\t<rtpiFeedName></rtpiFeedName>\r\n\t<nm>Clark &amp; Balmoral</nm>\r\n\t\r\n\r\n\t<sri>\r\n\t\t<rt>22</rt> \r\n\t\t<rtRtpiFeedName></rtRtpiFeedName>\r\n\t\t<rd>22</rd>\t\t\r\n\t\t<d>Southbound</d> \r\n\t\t<dd>Southbound</dd>   \r\n\t\t<dRtpiFeedName></dRtpiFeedName>\r\n\t</sri>\r\n\r\n\t<sbs>\r\n\r\n\r\n\t</sbs>\r\n\t\r\n\r\n\t<cr>22</cr>\r\n\t<crRtpiFeedName></crRtpiFeedName>\r\n\r\n\t<pre>\r\n\r\n\t\t<pt>10 MIN</pt>\r\n\r\n\t\t<fd>Harrison</fd>\r\n\r\n\t\t<v>1914</v>\r\n\t\t<scheduled>false</scheduled>\t\t\r\n\r\n\t\t<rn>22</rn> \r\n\t\t<rd>22</rd> \t\t\r\n\r\n\t\t\r\n\t\t<m>1</m>\t\r\n\t\t<consist></consist>    \r\n\t\t<cars></cars> \r\n\t\t    \t\r\n\t</pre>\r\n\r\n\t<pre>\r\n\r\n\t\t<pt>22 MIN</pt>\r\n\r\n\t\t<fd>Harrison</fd>\r\n\r\n\t\t<v>1848</v>\r\n\t\t<scheduled>false</scheduled>\t\t\r\n\r\n\t\t<rn>22</rn> \r\n\t\t<rd>22</rd> \t\t\r\n\r\n\t\t\r\n\t\t<m>1</m>\t\r\n\t\t<consist></consist>    \r\n\t\t<cars></cars> \r\n\t\t    \t\r\n\t</pre>\r\n\r\n\r\n</stop>\r\n'
doc is: <Element 'stop' at 0x10e648d68>
10 MIN
22 MIN
import sys; print('Python %s on %s' % (sys.version, sys.platform))
'''