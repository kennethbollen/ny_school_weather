#py3!
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pull data from nyc open data api
df = pd.read_csv("https://data.cityofnewyork.us/resource/ffyc-sb9d.csv")

#the date needs to be reformatted from int to datetime and used as the index

df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
df = df.sort_values(by=["Date"], ascending=[True])
df.set_index("Date", inplace=True)

#to make the datetime index unique, resample the data to be daily

df = df.resample("D").sum()

#no longer need the SchoolYear variable and remove it from the dataset 

del(df["SchoolYear"])

#repeat the process for dataset containing 2009 to 2012

df2 = pd.read_csv("https://data.cityofnewyork.us/resource/we4e-hyf9.csv")
df2["Date"] = pd.to_datetime(df2["Date"], format="%Y%m%d")
df2 = df2.sort_values(by="Date", ascending=[True])
df2.set_index("Date", inplace=True)
df2 = df2.resample("D").sum()

del(df2["SchoolYear"])

#concatenate 2006-2009 with 2009-2012

df_all = pd.concat([df, df2])

#repeat for dataset 2012-2015

df3 = pd.read_csv("https://data.cityofnewyork.us/resource/cewk-aqyn.csv")
df3["Date"] = pd.to_datetime(df3["Date"], format="%Y%m%d")
df3 = df3.sort_values(by=["Date"], ascending=[True])
df3.set_index("Date", inplace=True)
df3 = df3.resample("D").sum()

del(df3["SchoolYear"])

#concatenate 2006-2012 with 2012-2015

df_all = pd.concat([df_all, df3])

#repeat for dataset 2015-2017

df4 = pd.read_csv("https://data.cityofnewyork.us/resource/cewk-aqyn.csv")
df4["Date"] = pd.to_datetime(df4["Date"], format="%Y%m%d")
df4 = df4.sort_values(by=["Date"], ascending=True)
df4.set_index("Date", inplace=True)
df4 = df4.resample("D").sum()

del(df4["SchoolYear"])

#concatenate 2006-2015 with 2015-2017

df_all = pd.concat([df_all, df4])

#import the weather data

weather = pd.read_csv("weather_ny.csv", header=None)

#set the date column as the index for the dataframe

weather.set_index(weather[0], inplace=True)

#remove the redundant date 

del(weather[0])
