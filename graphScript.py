import matplotlib.pyplot as plt

def createGraphs(figureHeight, figureWidth, hasGridlines, dataSet, xAxisLabel, yAxisLabel, isLog):
    fig, ax = plt.subplots(figsize=(figureHeight, figureWidth)) # Set figure height & width
    # Plot the results of the experiments 
    for column in dataSet:
        # Assumption: the x-axis for each experiment will be called row (could be improved by making this more dynamic)
        if (column != 'r'):
            ax.plot(dataSet['r'], dataSet[column], label=column)
    ax.set_xlabel(xAxisLabel) # Add axis labels
    ax.set_ylabel(yAxisLabel)
    if (isLog):
        ax.set_yscale('log')
    ax.legend() # Add labels for each experiment
    if (hasGridlines): # Does the user want gridlines?
        ax.grid()
    plt.show() 
