import graphScripts as gs
import pandas as pd

df = pd.read_csv('shellLogs.csv')
# createGraphs(dataSet, confidenceLevel, figureHeight, figureWidth, hasGridlines, xAxisLabel, yAxisLabel, isLog, displayFormat, fileName (optional))
gs.createGraphs(df, 6, 4, True, "test x axis", "test y axis", True, 'figure', "")
# createBoxPlot(dataSet, figureHeight, figureWidth, title, xAxisLabel, yAxisLabel, hasGrid, displayFormat, fileName (optional))
# gs.createBoxPlot(df, 6, 4, 'Tips', 'day', "total_bill", False, 'figure')