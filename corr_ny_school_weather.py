#python3
#Investigate if the weather in NY impacts school attendance numbers in NY schools
#5 datasets used
#4 datasets from NYC Open Data https://opendata.cityofnewyork.us/
#1 dataset from wunderground.com

>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> df = pd.read_csv("/Users/2024450/Documents/Stats/2006-2009_Historical_Daily_Attendance_By_School.csv")
>>> print(df.info())
#determine the structure of the dataset

RangeIndex: 806851 entries, 0 to 806850
Data columns (total 7 columns):
School        806851 non-null object
Date          806851 non-null int64
SchoolYear    806851 non-null int64
Enrolled      806851 non-null int64
Present       806851 non-null int64
Absent        806851 non-null int64
Released      806851 non-null int64
dtypes: int64(6), object(1)
memory usage: 43.1+ MB

#the date needs to be reformatted from int to datetime and used as the index

>>> df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
>>> df = df.sort_values(by=["Date"], ascending=[True])
>>> df.set_index("Date", inplace=True)
>>> print(df.head())
            School  SchoolYear  Enrolled  Present  Absent  Released
Date                                                               
2006-09-05  01M015    20062007       252      226      26         0
2006-09-05  12X273    20062007       258      226      32         0
2006-09-05  26Q158    20062007      1141     1106      35         0
2006-09-05  04M155    20062007       348      322      26         0
2006-09-05  26Q133    20062007       501      470      31         0

#to make the datetime index unique, resample the data to be daily

>>> df = df.resample("D").sum()
>>> print(df.head())
              SchoolYear  Enrolled   Present    Absent  Released
Date                                                            
2006-09-05  2.927047e+10  985547.0  839149.0  144263.0    2135.0
2006-09-06  2.927047e+10  991406.0  876899.0  112555.0    1952.0
2006-09-07  2.931059e+10  995089.0  895097.0   99372.0     620.0
2006-09-08  2.913003e+10  995489.0  889907.0  102291.0    3291.0
2006-09-09           NaN       NaN       NaN       NaN       NaN

#we no longer need the SchoolYear variable and remove it from the dataset 

>>> del(df["SchoolYear"])
>>> print(df.head())
            Enrolled   Present    Absent  Released
Date                                              
2006-09-05  985547.0  839149.0  144263.0    2135.0
2006-09-06  991406.0  876899.0  112555.0    1952.0
2006-09-07  995089.0  895097.0   99372.0     620.0
2006-09-08  995489.0  889907.0  102291.0    3291.0
2006-09-09       NaN       NaN       NaN       NaN

#we repeat the process for dataset containing 2009 to 2012

>>> df2 = pd.read_csv("/Users/2024450/Documents/Stats/2009-2012_Historical_Daily_Attendance_By_School.csv")
>>> df2["Date"] = pd.to_datetime(df2["Date"], format="%Y%m%d")
>>> df2 = df2.sort_values(by="Date", ascending=[True])
>>> df2.set_index("Date", inplace=True)
>>> df2 = df2.resample("D").sum()
>>> print(df2.info())

DatetimeIndex: 1023 entries, 2009-09-09 to 2012-06-27
Freq: D
Data columns (total 5 columns):
SchoolYear    550 non-null float64
Enrolled      550 non-null float64
Present       550 non-null float64
Absent        550 non-null float64
Released      550 non-null float64
dtypes: float64(5)
memory usage: 48.0 KB

>>> print(df2.head())
              SchoolYear  Enrolled   Present   Absent  Released
Date                                                           
2009-09-09  3.128326e+10  971921.0  878443.0  92170.0    1308.0
2009-09-10  3.128326e+10  977406.0  898846.0  77741.0     819.0
2009-09-11  3.102206e+10  977778.0  888802.0  87465.0    1511.0
2009-09-12           NaN       NaN       NaN      NaN       NaN
2009-09-13           NaN       NaN       NaN      NaN       NaN

>>> del(df2["SchoolYear"])
>>> print(df2.head())
            Enrolled   Present   Absent  Released
Date                                             
2009-09-09  971921.0  878443.0  92170.0    1308.0
2009-09-10  977406.0  898846.0  77741.0     819.0
2009-09-11  977778.0  888802.0  87465.0    1511.0
2009-09-12       NaN       NaN      NaN       NaN
2009-09-13       NaN       NaN      NaN       NaN

#merge 2006-2009 with 2009-2012

>>> df_all = pd.concat([df, df2])

#repeat for dataset 2012-2015

>>> df3 = pd.read_csv("/Users/2024450/Documents/Stats/2012_-_2015_Historical_Daily_Attendance_By_School.csv")
>>> df3["Date"] = pd.to_datetime(df3["Date"], format="%Y%m%d")
>>> df3 = df3.sort_values(by=["Date"], ascending=[True])
>>> df3.set_index("Date", inplace=True)
>>> df3 = df3.resample("D").sum()
>>> print(df3.head())
              SchoolYear  Enrolled   Present    Absent  Released
Date                                                            
2012-09-06  3.219522e+10  976983.0  861711.0  113740.0    1532.0
2012-09-07  3.195376e+10  978662.0  866717.0  110679.0    1266.0
2012-09-08           NaN       NaN       NaN       NaN       NaN
2012-09-09           NaN       NaN       NaN       NaN       NaN
2012-09-10  3.225559e+10  984584.0  917677.0   66502.0     405.0

>>> del(df3["SchoolYear"])
>>> print(df3.head())
            Enrolled   Present    Absent  Released
Date                                              
2012-09-06  976983.0  861711.0  113740.0    1532.0
2012-09-07  978662.0  866717.0  110679.0    1266.0
2012-09-08       NaN       NaN       NaN       NaN
2012-09-09       NaN       NaN       NaN       NaN
2012-09-10  984584.0  917677.0   66502.0     405.0

>>> df_all = pd.concat([df_all, df3])
>>> print(df_all.head())
            Enrolled   Present    Absent  Released
Date                                              
2006-09-05  985547.0  839149.0  144263.0    2135.0
2006-09-06  991406.0  876899.0  112555.0    1952.0
2006-09-07  995089.0  895097.0   99372.0     620.0
2006-09-08  995489.0  889907.0  102291.0    3291.0
2006-09-09       NaN       NaN       NaN       NaN
>>> print(df_all.tail())
            Enrolled   Present    Absent  Released
Date                                              
2015-06-22  722105.0  597600.0   93001.0   31504.0
2015-06-23  720626.0  591335.0   96854.0   32437.0
2015-06-24  720969.0  578078.0  110246.0   32645.0
2015-06-25  718736.0  566306.0  119695.0   32735.0
2015-06-26  964486.0  761847.0  173540.0   29099.0

#repeat for dataset 2015-2017

>>> df4 = pd.read_csv("/Users/2024450/Documents/Stats/2015-2017_Historical_Daily_Attendance_By_School.csv")
>>> df4["Date"] = pd.to_datetime(df4["Date"], format="%Y%m%d")
>>> df4 = df4.sort_values(by=["Date"], ascending=True)
>>> df4.set_index("Date", inplace=True)
>>> df4 = df4.resample("D").sum()
>>> del(df4["SchoolYear"])
>>> print(df4.head())
            Enrolled   Present   Absent  Released
Date                                             
2015-09-08    1265.0    1033.0    232.0       0.0
2015-09-09  970354.0  886772.0  81545.0    2037.0
2015-09-10  973945.0  895214.0  77986.0     745.0
2015-09-11  974089.0  900833.0  71300.0    1956.0
2015-09-12       NaN       NaN      NaN       NaN

>>> df_all = pd.concat([df_all, df4])

>>> print(df_all.head())
            Enrolled   Present    Absent  Released
Date                                              
2006-09-05  985547.0  839149.0  144263.0    2135.0
2006-09-06  991406.0  876899.0  112555.0    1952.0
2006-09-07  995089.0  895097.0   99372.0     620.0
2006-09-08  995489.0  889907.0  102291.0    3291.0
2006-09-09       NaN       NaN       NaN       NaN
>>> print(df_all.tail())
            Enrolled   Present    Absent  Released
Date                                              
2017-06-24       NaN       NaN       NaN       NaN
2017-06-25       NaN       NaN       NaN       NaN
2017-06-26       NaN       NaN       NaN       NaN
2017-06-27  954296.0  659321.0  284896.0   10079.0
2017-06-28  956253.0  723893.0  222140.0   10220.0

#fill the non applicable with zeros as these are weekends/public holidays 

>>> df_all = df_all.fillna(value=0)
>>> print(df_all.head())
            Enrolled   Present    Absent  Released
Date                                              
2006-09-05  985547.0  839149.0  144263.0    2135.0
2006-09-06  991406.0  876899.0  112555.0    1952.0
2006-09-07  995089.0  895097.0   99372.0     620.0
2006-09-08  995489.0  889907.0  102291.0    3291.0
2006-09-09       0.0       0.0       0.0       0.0
>>> print(df_all.tail())
            Enrolled   Present    Absent  Released
Date                                              
2017-06-24       0.0       0.0       0.0       0.0
2017-06-25       0.0       0.0       0.0       0.0
2017-06-26       0.0       0.0       0.0       0.0
2017-06-27  954296.0  659321.0  284896.0   10079.0
2017-06-28  956253.0  723893.0  222140.0   10220.0

#import the weather data

>>> weather = pd.read_csv("/Users/2024450/Documents/Stats/weather_ny.csv", header=None)
>>> print(weather.head())
           0   1   2   3   4   5   6    7   8   9  ...     12  13  14  15 16  \
0  05/09/2006  21  18  16  17  16  13  100  85  70 ...   1015  16   7   1  -   
1  06/09/2006  24  20  16  16  15  14  100  79  57 ...   1014  16  10   3  -   
2  07/09/2006  27  22  16  16  14  13   90  68  45 ...   1017  16  16  14  -   
3  08/09/2006  27  23  19  17  16  14   81  63  45 ...   1016  16  15   8  -   
4  09/09/2006  28  24  19  17  15  12   81  59  37 ...   1015  16  13   6  -   

  17 18     19    20   21  
0  -  -  11.68  Rain  NaN  
1  -  -      0  Rain  NaN  
2  -  -      0   NaN  NaN  
3  -  -      0   NaN  NaN  
4  -  -      0   NaN  NaN  


#need to reindex the date column into a datetime index for the weather dataset

>>> weather.set_index(weather[0], inplace=True)
>>> print(weather.head())
                    0   1   2   3   4   5   6    7   8   9  ...     12  13  \
0                                                           ...              
05/09/2006  05/09/2006  21  18  16  17  16  13  100  85  70 ...   1015  16   
06/09/2006  06/09/2006  24  20  16  16  15  14  100  79  57 ...   1014  16   
07/09/2006  07/09/2006  27  22  16  16  14  13   90  68  45 ...   1017  16   
08/09/2006  08/09/2006  27  23  19  17  16  14   81  63  45 ...   1016  16   
09/09/2006  09/09/2006  28  24  19  17  15  12   81  59  37 ...   1015  16   

            14  15 16 17 18     19    20   21  
0                                              
05/09/2006   7   1  -  -  -  11.68  Rain  NaN  
06/09/2006  10   3  -  -  -      0  Rain  NaN  
07/09/2006  16  14  -  -  -      0   NaN  NaN  
08/09/2006  15   8  -  -  -      0   NaN  NaN  
09/09/2006  13   6  -  -  -      0   NaN  NaN  

#remove the redundant date 

>>> del(weather[0])
>>> print(weather.head())
            1   2   3   4   5   6    7   8   9     10 ...     12  13  14  15  \
0                                                     ...                      
05/09/2006  21  18  16  17  16  13  100  85  70  1019 ...   1015  16   7   1   
06/09/2006  24  20  16  16  15  14  100  79  57  1017 ...   1014  16  10   3   
07/09/2006  27  22  16  16  14  13   90  68  45  1020 ...   1017  16  16  14   
08/09/2006  27  23  19  17  16  14   81  63  45  1020 ...   1016  16  15   8   
09/09/2006  28  24  19  17  15  12   81  59  37  1017 ...   1015  16  13   6   

           16 17 18     19    20   21  
0                                      
05/09/2006  -  -  -  11.68  Rain  NaN  
06/09/2006  -  -  -      0  Rain  NaN  
07/09/2006  -  -  -      0   NaN  NaN  
08/09/2006  -  -  -      0   NaN  NaN  
09/09/2006  -  -  -      0   NaN  NaN


#need to create headers for the weather dataset

>>> headers = [['temp', 'temp', 'temp', 'dew_point', 'dew_point', 'dew_point', 'humidity', 'humidity', 'humidity', 'sea_lv_pass', 'sea_lv_pass', 'sea_lv_pass', 'visibility', 'visibility', 'visibility', 'wind', 'wind', 'wind', 'percip(mm)','events'],['high', 'avg', 'low', 'high', 'avg', 'low', 'high', 'avg', 'low', 'high', 'avg', 'low','high', 'avg', 'low','high', 'avg', 'low','sum','descrip']]

>>> headers[1].append("extra")
>>> headers[0].append("extra")
>>> weather.index.rename("date", inplace=True)
>>> weather.columns = headers
>>> print(weather.head())
           temp         dew_point         humidity         sea_lv_pass  ...   \
           high avg low      high avg low     high avg low        high  ...    
date                                                                    ...    
05/09/2006   21  18  16        17  16  13      100  85  70        1019  ...    
06/09/2006   24  20  16        16  15  14      100  79  57        1017  ...    
07/09/2006   27  22  16        16  14  13       90  68  45        1020  ...    
08/09/2006   27  23  19        17  16  14       81  63  45        1020  ...    
09/09/2006   28  24  19        17  15  12       81  59  37        1017  ...    

                 visibility         wind         percip(mm)  events extra  
             low       high avg low high avg low        sum descrip extra  
date                                                                       
05/09/2006  1015         16   7   1    -   -   -      11.68    Rain   NaN  
06/09/2006  1014         16  10   3    -   -   -          0    Rain   NaN  
07/09/2006  1017         16  16  14    -   -   -          0     NaN   NaN  
08/09/2006  1016         16  15   8    -   -   -          0     NaN   NaN  
09/09/2006  1015         16  13   6    -   -   -          0     NaN   NaN  

#the average weather variable is the only observation we need from the weather dataset and therefore extracted into a new data Series

>>> avg_weather = pd.DataFrame(weather["temp"]["avg"])

#merge the average weather data into the school data

>>> df_weather = pd.merge(df_all, avg_weather, left_index=True, right_index=True)
>>> print(df_weather.head())
            Enrolled   Present    Absent  Released avg
2006-09-05  985547.0  839149.0  144263.0    2135.0  18
2006-09-06  991406.0  876899.0  112555.0    1952.0  20
2006-09-07  995089.0  895097.0   99372.0     620.0  22
2006-09-08  995489.0  889907.0  102291.0    3291.0  23
2006-09-09       0.0       0.0       0.0       0.0  24

#check the data structure 

>>> print(df_weather.info())
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 3733 entries, 2006-09-05 to 2017-06-28
Data columns (total 5 columns):
Enrolled    3733 non-null float64
Present     3733 non-null float64
Absent      3733 non-null float64
Released    3733 non-null float64
avg         3733 non-null object
dtypes: float64(4), object(1)
memory usage: 175.0+ KB

#avg variable needs to be converted to a float datatype to allow for aggregation and stats functions

>>> df_weather["avg"] = df_weather["avg"].astype(float)
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    df_weather["avg"] = df_weather["avg"].astype(float)
  File "C:\Users\2024450\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\util\_decorators.py", line 91, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\2024450\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 3410, in astype
    **kwargs)
  File "C:\Users\2024450\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals.py", line 3224, in astype
    return self.apply('astype', dtype=dtype, **kwargs)
  File "C:\Users\2024450\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals.py", line 3091, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\2024450\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals.py", line 471, in astype
    **kwargs)
  File "C:\Users\2024450\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals.py", line 521, in _astype
    values = astype_nansafe(values.ravel(), dtype, copy=True)
  File "C:\Users\2024450\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\dtypes\cast.py", line 636, in astype_nansafe
    return arr.astype(dtype)
ValueError: could not convert string to float: '-'

#avg variable contains non-integer observations that cannot be transformed into a float datatype
#Non-integer observations relate to the use of hypens ("-") to represent zero degrees 
#need to remove all non-integer observations and turn into 0

>>> df_weather.loc[df_weather["avg"] == "-", "avg"] = 0

#now can transform the avg variable from a object to a float datatype

>>> df_weather["avg"] = df_weather["avg"].astype(float)

#now apply Pandas correlation function on the dataframe

>>> df_weather.corr()
          Enrolled   Present    Absent  Released       avg
Enrolled  1.000000  0.998000  0.862910  0.186844 -0.171710
Present   0.998000  1.000000  0.830216  0.160747 -0.172754
Absent    0.862910  0.830216  1.000000  0.249666 -0.143012
Released  0.186844  0.160747  0.249666  1.000000  0.017153
avg      -0.171710 -0.172754 -0.143012  0.017153  1.000000

#to take a more indepth look between two variables

>>> df_weather[["Present", "avg"]].corr()
          Present       avg
Present  1.000000 -0.172754
avg     -0.172754  1.000000

#create a scatterplot to show the results

>>> pre_corr = df_weather[["Present", "avg"]].corr()
>>> df_weather[["Present", "avg"]].plot(x="avg", y="Present", kind="scatter")
<matplotlib.axes._subplots.AxesSubplot object at 0x0000000008633A20>
>>> plt.xlabel("Average NY weather")
<matplotlib.text.Text object at 0x0000000008310748>
>>> plt.ylabel("Students Present")
<matplotlib.text.Text object at 0x00000000082C3CF8>
>>> plt.title("Relationship between NY Weather and School Attendance")
<matplotlib.text.Text object at 0x00000000082B6780>
>>> plt.show()

#the negative correlation between the average temperature and school attendance/absence suggests there is an inverse relationship between the two variables
#However, the correlation is relatively weak and therefore suggests that the weather plays a small role in school attendance

