#15-1:Cubes
#Zavier Butler
#12/7/25
# A program to plot cubic numbers up to 5000^3
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
x = range(1,5001)
y= [x**3 for x in x]

#Color map for cubes plot
ax.scatter(x,y, c=y, cmap=plt.cm.Greens, s=100)

# Set chart title and label axes.
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)
ax.axis([0,5100,0,130_000_000])

plt.show()