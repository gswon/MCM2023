import matplotlib.pyplot as plt
import numpy as np
import re

def get_info(info):
    string=info
    return re.split("\n",string)

BOLTZMANN_CONSTANT=1.380649*(10)**(-23)
m=800
T=270
vertical_shift=15000

report_cases=[]
report_hard_mode=[]

with open("number_of_report_cases.txt",'r') as f_obj:
    text=f_obj.read()
    result=get_info(text)
    report_cases=np.array([int(i) for i in result][::-1])

x=np.arange(202,561,1) # contest number

y_b=10**(-31.6875)*((m/(2*np.pi*BOLTZMANN_CONSTANT*T))**(3/2)) * (4*np.pi*((x-192.5)**2)*np.e**(-(m*(x-192.5)) / (2*k*T))) + vertical_shift
y2=10000000/(x-202)-9500
y3=361908*np.e**(0.015*(228-x))-6000
y_final=list(y_b[0:266-202])+list(y3[266-203:338-202])+list(y2[338-202+1:])

plt.figure()
plt.plot(x,report_cases)
plt.plot(x,y_final)

plt.xlim(202,560)
plt.ylim(0,370000)
plt.show()

with open("reported_cases_approximated.txt",'w') as f_obj:
    content=""
    for i in y_final[::-1]:
        content+=str(i)+'\n'
    f_obj.write(content[:-1])
