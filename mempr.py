#cd /Users/panluobu/Documents/Mem
#python memp.py
import re
import os
import sys
import time
import matplotlib.pyplot as plt

def get(msg):
    PN = input(msg)
    if PN=='':
        PN =  'com.panda.unity.blastsaga'
    return PN

PackName = get("please input Packname:")
squares = []
squares1 = []

mins = 0
sec = 10

for i in range(60*mins + sec):
#    print("adb shell dumpsys meminfo " + PackName)
    content = os.popen("adb shell dumpsys meminfo " + PackName).read()    
    string = str(content)
    f2 = open("memp.txt", 'r+')
    f2.seek(0, os.SEEK_END)    

    result0 = re.findall(".*TOTAL:(.*)TOTAL.*", string)
    result1 = ''.join(result0)

    result2 = re.compile(r' ')
    result3 = result2.sub('', str(result1))
    result = ''.join(result3)

    squares.append(result)

    for y in result:
        s = str(y)
        f2.write(s)
    f2.write('\n')
    f2.close()
    print (str(i) + '. ' +result)
    time.sleep(1)   

for s in squares:
    s1 = int(int(s)/1024)
    print(s1)
    squares1.append(s1)

plt.title(PackName)
plt.xlabel("Time")
plt.ylabel("Men")
#plt.xlim(0, 60*mins+sec-1)
plt.ylim(0, 500)
plt.plot(squares1)
plt.show()

print ("ok")