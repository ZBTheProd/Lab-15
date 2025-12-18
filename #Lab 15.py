#Lab 15
#Plot a math formula using matplotlib
#Zavier Butler
#12/7/25
import matplotlib.pyplot as plt
import numpy as np


#draw a circle
theta = np.linspace(0, 2 * np.pi, 300)
radius = 2 *(1 - np.cos(theta))

x = radius * np.cos(theta)
y = radius * np.sin(theta)

fig, ax = plt.subplots(figsize=(10,10))

ax.plot(x,y, color='red')
ax.set_aspect(1)
ax.tick_params(labelsize=10)
ax.set_title("Cardioid equation", fontsize= 12)
ax.set_xlabel("Shape X axis", fontsize=12)
ax.set_ylabel("Shape Y axis", fontsize=12)

#plt information
plt.show()
