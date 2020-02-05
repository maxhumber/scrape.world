import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)

seconds_in_day = 24*60*60

import datetime

x = datetime.datetime.now()

x.second

dir(pd.Timestamp('now'))

n = 1000
x = np.random.randint(0, 24*60*60, n)
y = 10 * np.sin(2*np.pi * x / seconds_in_day)
y += 10


plt.scatter(x, y)




#
