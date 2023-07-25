import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)  # Sample data.

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x axis')  # Add an x-label to the axes.
ax.set_ylabel('y axis')  # Add a y-label to the axes.
ax.set_title("My Second Graph")  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.show()