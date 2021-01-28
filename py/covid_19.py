import pandas as pd
import numpy as np

import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs

from dateutil import parser
import matplotlib.pyplot as plt

def tsplot(y, lags=None, figsize=(10, 8), style='bmh'):
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    with plt.style.context(style):
        fig = plt.figure(figsize=figsize)
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))
        y.plot(ax=ts_ax)
        ts_ax.set_title('Time Series Analysis Plots')
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax, alpha=0.5)
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.5)
        sm.qqplot(y, line='s', ax=qq_ax)
        qq_ax.set_title('QQ Plot')
        y.hist(bins = 20, ax = pp_ax)
        # scs.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)

        plt.tight_layout()
    return
# we will transform the first row of our data_set to columns
def transform_columns(path,columns,column):
    data = pd.read_csv(path)
    keys=data[column].fillna("").apply(lambda x: "_".join(x).replace(" ","_").rstrip("_"),axis=1)
    dates=[i for i in data.columns if i not in columns] 
    n=len(keys)
    all_series=[]
    for i in range(n):
        series=pd.DataFrame(data[dates].iloc[i].T)
        series.rename(columns = {i: keys.iloc[i]}, inplace = True)   
        all_series.append(series)
    series=pd.concat(all_series,axis=1).rename_axis('dates').reset_index()
    series['dates']=series['dates'].apply(lambda x: parser.parse(x))
    return series
# we will conserve the rows and add rows for index transform the first row of our data_set to columns
def transform_rows(path,output,columns):
    data = pd.read_csv(path)
    keys=data[columns]
    dates=[i for i in data.columns if i not in columns] 
    n=len(keys)
    all_series=[]
    for i in range(n):
        l=pd.DataFrame(data[dates].iloc[i].T)
        l.rename(columns = {i: "series"}, inplace = True)
        l[columns]=l.apply(lambda x: keys.iloc[i], axis = 1)
        l.rename_axis('dates').reset_index( inplace=True)
        l['dates']=l['dates'].apply(lambda x: parser.parse(x))
        all_series.append(l)
    return pd.concat(all_series,axis=0

