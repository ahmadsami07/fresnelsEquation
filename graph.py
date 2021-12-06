import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


nt=1
ni=1.33

maximumX=math.asin(nt/ni)
maximumXDeg=math.degrees(math.asin(nt/ni))

x_array=[0,maximumX/4,maximumX/3,maximumX/2,maximumX]
#for creating a degrees array:
print("X ARRAY:",x_array)

xf_array=[0,maximumXDeg/4,maximumXDeg/3,maximumXDeg/2,maximumXDeg]
print("XF ARRAY:",xf_array)
q1_array=[]

y1_array=[]
y2_array=[]

#for populating q1 array
for i in range(5):
    if(i==0):
        q1_array.append(0)
        continue
    incident=1.33math.sin(x_array[i])
    thetaT=math.asin(incident)
    thetaT=math.degrees(thetaT)
    # print("PRINT THETA T NUMBER:",i,thetaT)
    q1_array.append(thetaT)


print("Q1 Array is :" ,q1_array)


for i in range(5):
    if(i==0):
            y1_array.append(0.14)
            continue
    rPerpNumerator=(-1)math.sin(math.radians(xf_array[i])-math.radians(q1_array[i]))
    rPerpDenom=math.sin(math.radians(xf_array[i])+math.radians(q1_array[i]))
    rPerp=rPerpNumerator/rPerpDenom
    y1_array.append(rPerp)


print("Y1 Array is ",y1_array)

for i in range(5):
    if(i==0):
            y2_array.append(-0.14)
            continue
    rPerpNumerator=math.tan(math.radians(xf_array[i])-math.radians(q1_array[i]))
    rPerpDenom=math.tan(math.radians(xf_array[i])+math.radians(q1_array[i]))
    rPerp=rPerpNumerator/rPerpDenom
    y2_array.append(rPerp)


print("Y2 Array is ",y2_array)

xf_y1_Spline = make_interp_spline(xf_array, y1_array)
xf_y2_Spline = make_interp_spline(xf_array, y2_array)
xfArrayNp=np.array(xf_array)
X1 = np.linspace(xfArrayNp.min(), xfArrayNp.max(), 100)
Y1 = xf_y1_Spline(X1)
Y2=xf_y2_Spline(X1)

plt.savefig('Question8.pdf')
plt.plot(X1,Y1,'r')
plt.plot(X1,Y2,'g')
plt.xlabel('Incident Angle')
plt.ylabel('Fresnel Amplitude Coefficients')
plt.show()