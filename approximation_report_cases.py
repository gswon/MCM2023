import matplotlib.pyplot as plt
import numpy as np
import math
import re

def get_info(info):
    string=info
    return re.split("\n",string)

def load_info(info,table):
    for i in range(0,len(info),1):
        table[info[i][0]].append(int(info[i][7]))
    #return table

k=28
#print(math.e, math.gamma(4))

report_cases=[]

with open("number_of_report_cases.txt",'r') as f_obj:
    text=f_obj.read()
    result=get_info(text)
    report_cases=np.array([int(i) for i in result][::-1])


x=np.arange(202,561,1) # contest number
print(report_cases)
y=(6500000)*((x-202)**((k/2)-1)*math.e**(-(x-202)/2)) / (2**(k/2)*math.gamma(k/2))#max 361908
y2=12000000/(x-202)-5000
y3=361908*np.e**(0.015*(228-x))
y4=0.53*y2+0.47*y3
y5=y4+y
#36190800
plt.figure()
plt.plot(x,y)
plt.plot(x,report_cases)
#plt.plot(x,y2)
#plt.plot(x,y3)
plt.plot(x,y4)
#plt.plot(x,y5)
plt.xlim(202,560)
plt.ylim(0,370000)
plt.show()
