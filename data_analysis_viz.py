#py3!
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#now apply Pandas correlation function on the dataframe

df_weather.corr()

#to take a more indepth look between two variables

df_weather[["Present", "avg"]].corr()

#get a cut of the data

pre_corr = df_weather[["Present", "avg"]].corr()

#create a scatterplot to show the results

df_weather[["Present", "avg"]].plot(x="avg", y="Present", kind="scatter")
plt.xlabel("Average NY weather")
plt.ylabel("Students Present")
plt.title("Relationship between NY Weather and School Attendance")
plt.show()

#the negative correlation between the average temperature and school attendance/absence suggests there is an inverse relationship between the two variables
#However, the correlation is relatively weak and therefore suggests that the weather plays a small role in school attendance
