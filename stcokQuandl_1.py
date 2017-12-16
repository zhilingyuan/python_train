import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression


quandl.ApiConfig.api_key = 'HLyJztY8bNuKQ5LL-2f2'
data=quandl.get_table('WIKI/PRICES')
print(data.head())
data=data[['adj_open','adj_high','adj_low','adj_close','adj_volume']]
data['HL_PCT']=(data['adj_high']-data['adj_low'])/data['adj_close']*100.0
data['PCT_change']=(data['adj_close']-data['adj_open'])/data['adj_open']*100.0
data=data[['adj_open','HL_PCT','PCT_change','adj_close','adj_volume']]

#print(data.head())
forecast_col='adj_close'
data.fillna(-99999,inplace=True)
forecast_out=int(math.ceil(0.01*len(data)))
data['label']=data[forecast_col].shift(-forecast_out)

#print(data.head())
data.dropna(inplace=True)
#print(data.tail())

x=np.array(data.drop(['label'],1))
y=np.array(data['label'])

x=preprocessing.scale(x)
x=x[:-forecast_out+1]
data.dropna(inplace=True)
y=np.array(data['label'])

print(len(x),len(y))



