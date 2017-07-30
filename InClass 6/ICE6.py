import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])

np.mean(x)
np.mean(y)

x1=np.mean(x)
y1=np.mean(y)
print (x1)
print (y1)

np.sum((x-x1)*(y-y1))
s1=np.sum((x-x1)*(y-y1))

np.sum((x-y1)*(x-y1))
s2=np.sum((x-y1)*(x-y1))

print(s1)
print(s2)

f = s1/s2
print(f)

b0 = y1-(f*x1)
print(b0)
y2= (b0+f*x)

plt.scatter(x,y)
plt.plot(x, y2)
plt.show()