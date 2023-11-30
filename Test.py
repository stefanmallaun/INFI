import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.arange(0,100)

b = np.arange(0,100,2)

c = np.random.normal(0,100,100)

d = np.mean(c)

e = np.median(c)

f = np.std(c)

g = np.quantile(c, 0.025) 

h = np.quantile(c, 0.95)




plt.bar(d, 10)
plt.ylabel("HEy")
plt.xlabel("YO")
#plt.show()

d = [[1, 2], [3, 4]]
s = pd.DataFrame(d, index=['A', 'B'])

print(s)

x = {'Name': ['Herbert', 'Hubert', 'David'], 'Alter' : [12,13,4]}

s = pd.DataFrame(x, columns=['Alter', 'Name'], index= ['ool', 'Uncool', 'Behindert'])

print(s)
