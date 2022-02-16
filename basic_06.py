'''written in Jupyter Notebook'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

#################################################################################################################################
'''
data = np.arange(10)
print(plt.plot(data)
'''
#################################################################################################################################
'''
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
'''
#################################################################################################################################
'''
plt.plot(np.random.randn(60).cumsum(), 'k--')
'''
#################################################################################################################################
'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
'''
#################################################################################################################################
'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
tick = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation = 30, fontsize = 'small')
'''
#################################################################################################################################
'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
tick = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation = 30, fontsize = 'small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
'''
#################################################################################################################################
'''
from numpy.random import randn

fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)

ax.plot(randn(1000).cumsum(), 'k', label = 'one')
ax.plot(randn(1000).cumsum(), 'k--', label = 'two')
ax.plot(randn(1000).cumsum(), 'k.', label = 'three')
ax.legend(loc ='best')
'''
#################################################################################################################################
'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color = 'k', alpha = 0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color = 'b', alpha = 0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color = 'g', alpha = 0.5)

ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
'''
#################################################################################################################################
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure()

s = pd.Series(np.random.randn(10).cumsum(), index = np.arange(0, 100, 10))

s.plot()
'''
#################################################################################################################################
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns = ['A', 'B', 'C', 'D'], index = np.arange(0, 100, 10))

df.plot()
'''
#################################################################################################################################
#.plot.bar() -> 수직막대그래프, .plot.barh() -> 수평막대그래프
#color = 'k' -> black ink, alpha = 0.7 -> transparency
'''
df = pd.DataFrame(np.random.rand(6, 4), index = ['one', 'two', 'three', 'four', 'five', 'six'], 
columns = pd.Index(['A', 'B', 'C', 'D'], name = 'Genus'))

print(df)

df.plot.bar()
'''
#################################################################################################################################
#staced = True -> 누적막대그래프
'''
df = pd.DataFrame(np.random.rand(6, 4), index = ['one', 'two', 'three', 'four', 'five', 'six'], 
columns = pd.Index(['A', 'B', 'C', 'D'], name = 'Genus'))

df.plot.barh(stacked = True, alpha = 0.5)
'''
#################################################################################################################################


