import re
import os
import sys
import time

for i in range(10):
    content = os.popen("adb shell dumpsys meminfo net.peakgames.toonblast").read()    
    print content
    string = str(content)
    print string
    f2 = open("memt.txt", 'r+')
    f2.seek(0, os.SEEK_END)    

    result = re.findall(".*TOTAL:(.*)TOTAL.*", string)

    for x in result:
        print x
    
    b = re.compile(r' ')
    b.sub('', result)
    for y in result:
        s = str(y)
        f2.write(s)
    f2.write('\n')
    f2.close()
    time.sleep(1)   

print "ok"    



