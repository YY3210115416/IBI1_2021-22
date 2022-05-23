import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import full_data.csv
covid_data=pd.read_csv("full_data.csv")

#show the first and third columns from rows 10-20
print(covid_data.iloc[10:21,0:3:2])

#use a Boolean to show "total_cases" for all rows corresponding to Afghanistan
Afghanistan=[False,False,False,False,True,False]
print(covid_data.iloc[0:82,Afghanistan])

#check the rows one by one, if the location is China, add a "True" in the list"China", otherwise add a "False"
China=[]
for i in range(7996):
    if covid_data.iloc[i,1]=="China":
        China.append(True)
    else:
        China.append(False)
#find all rows where the location is China
China_data=covid_data.iloc[China] 

#Select the data of new cases and new deaths in China 
China_new_data=China_data.iloc[:,2:4]
#computed the mean number of new cases and new deaths in China 
print(np.mean(China_new_data,axis=0)) 
#The mean number of new cases in China is 893.923913, and the mean number of new deaths is 35.967391.

#created a boxplot of new cases and new deaths in China worldwide with labels
labels='new cases in China','new deaths in China'
boxplot=plt.boxplot(China_new_data,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False,
            labels=labels)
plt.ylabel('number')
plt.title('new cases and new deaths in China')
plt.show()

#plot new cases in China over time with labels
China_dates=China_data.iloc[:,0]
China_new_cases=China_data.iloc[:,2]
plt.plot(China_dates,China_new_cases,'b+')
plt.xlabel('date')
plt.ylabel('new cases in China')
plt.show()

#plot new deaths in China over time with labels
China_dates=China_data.iloc[:,0]
China_new_deaths=China_data.iloc[:,3]
plt.plot(China_dates,China_new_deaths,'r+')
plt.xlabel('date')
plt.ylabel('new deaths in China')
plt.show()

#code to answer the question stated in file question.txt
#Question: How have total cases developed overtime in Spain?
#check the rows one by one, if the location is Spain, add a "True" in the list"Spain", otherwise add a "False"
Spain=[]
for i in range(7996):
    if covid_data.iloc[i,1]=="Spain":
        Spain.append(True)
    else:
        Spain.append(False)
#find all rows where the location is Spain
Spain_data=covid_data.iloc[Spain] 
#Select the data of dates and total cases in Spain 
Spain_dates=Spain_data.iloc[:,0]
Spain_total_cases=Spain_data.iloc[:,4]
#plot total cases in Spain over time with labels
plt.plot(Spain_dates,Spain_total_cases,'b+')
plt.xlabel('date')
plt.ylabel('total cases in Spain')
plt.show()