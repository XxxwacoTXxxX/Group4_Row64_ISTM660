# -*- coding: utf-8 -*-
"""Eksteen_Group_4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SRxKA1deyyl8_pw5bgrdsWTqDt7C1ksQ
"""

import matplotlib.colors as cl
import matplotlib.pyplot as plt
import pandas as pd
import row64
import seaborn as sns

def ScatterPlotBasic(inDf, inCol1, inCol2):
    col1 = inDf.columns[inCol1]
    col2 = inDf.columns[inCol2]
    sns.scatterplot(color="#1F77B4",data=inDf,x=col1,y=col2,s=25)

#IMPORT("C:\Users\14352\Desktop\Loan D.csv")
dfIn=row64.get_dataframe("Dataframe4")
df=dfIn.copy(deep=True)
ScatterPlotBasic(df,1,26)

import matplotlib.colors as cl
import matplotlib.pyplot as plt
import pandas as pd
import row64
import seaborn as sns

def ScatterPlotBasic(inDf, inCol1, inCol2):
    col1 = inDf.columns[inCol1]
    col2 = inDf.columns[inCol2]
    sns.scatterplot(color="#1F77B4",data=inDf,x=col1,y=col2,s=25)

import matplotlib.colors as cl
import matplotlib.pyplot as plt
import pandas as pd
import row64
import seaborn as sns

def ScatterPlotBasic(inDf, inCol1, inCol2):
    col1 = inDf.columns[inCol1]
    col2 = inDf.columns[inCol2]
    sns.scatterplot(color="#1F77B4",data=inDf,x=col1,y=col2,s=25)

#IMPORT("C:\Users\14352\Desktop\Loan D.csv")
dfIn=row64.get_dataframe("Dataframe4")
df=dfIn.copy(deep=True)
ScatterPlotBasic(df,65,66)