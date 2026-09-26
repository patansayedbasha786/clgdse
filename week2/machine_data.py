import pandas as p
df=p.read_csv("mechian_data.csv")
print(df)

#display complete dataset
print("ENGINEERING DATASET")
print(df)
#display first 5 records
print("\nFIRST 5 RECORDS")
print(df.head())
#display last 5 records
print("\nLAST 5 RECORDS")
print(df.tail())
#display number of rows & columns
print("\nDATASET SHAPE")
print(df.shape)
#display column names
print("\nCOLUMN NAMES")
print(df.columns)
#display data types
print("\nDATA TYPES")
print(df.dtypes)
#diplay basic imformation
print("\nDATASET IMFORMATION")
df.info()
#check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())
#generate statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())
#calculate mean values
print("\nAVERAGE VALUES")
print("Temperature:",df["tempature"].mean())
print("Pressure:",df["pressure"].mean())
print("Vibration:",df["vibration"].mean())
print("Operating_hours:",df["operating-hours"].mean())
#find maximum and minimum temperature
print("\nTEMPERATURE ANALYSIS")
print("MAXIMUM TEMPERATURE:",df["tempature"].max())
print("MINIMUM TEMPERATURE:",df["tempature"].min())
#count machine according to status
print("\nMACHINE STATUS")
print(df["status"].value_counts())
#display machines with high temperature
print("\nMACHINES WITH TEMPERATURE ABOVE 85")
print(df[df["tempature"]>85])
