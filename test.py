import numpy as np
import matplotlib.pyplot as plt

# create data
x = np.linspace(0,3)
y = x**2
z = x**3

# strong line on top 
plt.fill_between(x,z,color="yellow")
plt.fill_between( x, y, color="lightblue")

plt.xlim(0,)
plt.ylim(0,)
#plt.savefig("areaplot.png",bbox_inches = 'tight', pad_inches = 0)
plt.show()