import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('Book1.csv')

mpl.rcParams['lines.linewidth'] = 2
df.plot()
plt.xlabel('Sample No.')
plt.ylabel('Daily Grain Price ($)')
plt.title('Plot Showing Daily Variance in Grain Price in India')
plt.show()