import graphScript as gs
import pandas as pd

df = pd.read_csv('Book2.csv')
# createGraphs(figureHeight, figureWidth, hasGridlines, dataSet, xAxisLabel, yAxisLabel, isLog)
gs.createGraphs(6, 4, True, df, "test x axis", "test y axis", True)
