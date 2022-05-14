#The Pandas Library is a useful tool that enables us to read and explore datasets.
import pandas as pd
import numpy as np

# read date
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud"
df = pd.read_csv(path, header=None)

# show the first 5 rows
print("The first 5 rows of the dataframe")
df.head(5)

# the last 10 rows
print("The last 10 rows of the dataframe\n")
df.tail(10)

# create and add headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
df.head(10)

# replace ? with NaN
df1=df.replace('?',np.NaN)

# drop missing values
df=df1.dropna(subset=["price"], axis=0)
df.head(20)

# read and save data
pd.read_csv() df.to_csv()
pd.read_json() df.to_json()
pd.read_excel()	df.to_excel()
pd.read_hdf()	df.to_hdf()
pd.read_sql()	df.to_sql()

# check data type of each columns
df.dtypes()

# get a statistical summary of each column
df.describe()

# describe all the columns in "df"
df.describe(include = "all")

# look at the info of "df"
df.info()
