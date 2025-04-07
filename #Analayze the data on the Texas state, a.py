#Analayze the data on the Texas state, and make THE
import pandas as pd
import numpy as np


data_2001 = pd.read_csv("C:/Users/kkr84/OneDrive - Texas A&M University/Desktop/Storms/StormEvents_details-ftp_v1.0_d2001_c20220425.csv")

data_2002 = pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2002_c20220425.csv")#check
data_2003 = pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2003_c20220425.csv")#check
data_2004 = pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2004_c20220425.csv")#check
data_2005 = pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2005_c20220425.csv")#check
data_2006 = pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2006_c20250122.csv")#check
data_2007= pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2007_c20240216.csv")
data_2008= pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2008_c20240620.csv")
data_2009= pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2009_c20231116.csv")
data_2010 = pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2010_c20220425.csv")
data_2011  =pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2011_c20230417.csv")
data_2012=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2012_c20221216.csv")
data_2013=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2013_c20230118.csv")
data_2014=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2014_c20231116.csv")
data_2015=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2015_c20240716.csv")
data_2016=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2016_c20220719.csv")
data_2017=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2017_c20250122.csv")
data_2018=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2018_c20240716.csv")
data_2019=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2019_c20240117.csv")
data_2020=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2020_c20240620.csv")
data_2021=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2021_c20240716.csv")
data_2022=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2022_c20241121.csv")
data_2023=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2023_c20250216.csv")
data_2024=pd.read_csv("/content/drive/MyDrive/ecen 360/StormEvents_details-ftp_v1.0_d2024_c20250216.csv")

dfs = [
    data_2001, data_2002, data_2003, data_2004, data_2005, data_2006,
    data_2007, data_2008, data_2009, data_2010, data_2011, data_2012,
    data_2013, data_2014, data_2015, data_2016, data_2017, data_2018,
    data_2019, data_2020, data_2021, data_2022, data_2023, data_2024
]

# Combine them into one big DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

combined_df.head()



