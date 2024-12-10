# import seaborn as sb
# df = sb.load_dataset('taxis')
# import pandas as pd



# # df = pd.read_csv("HIMYMdataset.csv")    #importing a csv file into dataframe
# # print(df)
# # print(df.describe())
# #print(df.dtypes)
# #print(df.describe(include = 'int64' ))
# # print(df["passengers"] )  #working with columns and unique entries
# # print(df["passengers"].unique())


# # print((df['Imb rating' > 4]) and (df["passengers"]=="Chris"))
# # print(df.loc[9, "passengers"])                        # indexing and slicing
# # print(df.iloc[1,2])
# # df.to_csv("csv file link")                            #exporting data to csv file
# df.isnull().sum()                                       #getting number of null values for each column
# print(df.dropna())                                      #creates a copy of df where all null values removed
# print(df.dropna(inplace = True))                        #makes modification in original df
# x = df["passengers"].mean()                             # mean of colum passengers
# df['viewers'].fillna(x, inplace = True)   
# df.drop('passengers', axis =1)                          #deletes column
# print(df.sort_values(by "passengers", ascending = False))       #sorting values