import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

directory = 'testy'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and not filename.startswith('.'):
        df = pd.read_csv(f)
        print(filename)
        df.plot()
        plt.show()
