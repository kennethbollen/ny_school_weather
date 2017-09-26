#py3!
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

#fill the non applicable with zeros as these are weekends/public holidays 

df_all = df_all.fillna(value=0)

#need to create headers for the weather dataset

headers = [['temp', 'temp', 'temp', 'dew_point', 'dew_point', 'dew_point', 'humidity', 'humidity', 'humidity', 'sea_lv_pass', 'sea_lv_pass', 'sea_lv_pass', 'visibility', 'visibility', 'visibility', 'wind', 'wind', 'wind', 'percip(mm)','events', 'extra'],['high', 'avg', 'low', 'high', 'avg', 'low', 'high', 'avg', 'low', 'high', 'avg', 'low','high', 'avg', 'low','high', 'avg', 'low','sum','descrip', 'extra']]
weather.index.rename("date", inplace=True)
weather.columns = headers

#the average weather variable is the only observation we need from the weather dataset and therefore extracted into a new data Series

avg_weather = pd.DataFrame(weather["temp"]["avg"])

#merge the average weather data into the school data

df_weather = pd.merge(df_all, avg_weather, left_index=True, right_index=True)

#avg variable contains non-integer observations that cannot be transformed into a float datatype
#Non-integer observations relate to the use of hypens ("-") to represent zero degrees 
#need to remove all non-integer observations and turn into 0

df_weather.loc[df_weather["avg"] == "-", "avg"] = 0

#transform the avg variable from a object to a float datatype

df_weather["avg"] = df_weather["avg"].astype(float)

