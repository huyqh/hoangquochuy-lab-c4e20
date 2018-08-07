import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

# 1. prepare data
labels = ["web","androi", "ios", "react native"]
values = [40, 20, 20, 15]
colors = ["green","blue","red","black"]
exploe = [0,0,0,0.2]
# 2.plot
pyplot.pie(values, labels=labels,colors=colors,explode=exploe)
pyplot.axis("equal")
# 3.Show
pyplot.show()