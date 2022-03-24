#Visualising the effect of paternal age on offspring health
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
PC={30:1.03,35:1.07,40:1.11,45:1.17,50:1.23,55:1.32,60:1.42,65:1.55,70:1.72,75:1.94}
print(PC)

#draw the scatter plot
import matplotlib.pyplot as plt
#add data
x=paternal_age
y=chd
plt.scatter(x,y)
#add labels
plt.xlabel('paternal_age')
plt.ylabel('chd')
plt.show()

#print chd for a givin paternal_age
age=40
risk=PC[age]
print(risk)

#List manipulation
marks=[45,36,86,57,53,92,65,45]
#sort the list of marks
marks.sort()
marks=sorted(marks)
print(marks)

#draw the boxplot
import matplotlib.pyplot as plt
plt.boxplot(marks,vert=True,whis=1.5,patch_artist=True,meanline=True,showbox=True,
            showcaps=True,showfliers=True,notch=False)
plt.show()

#calculate the average mark
print(sum(marks)/8)
#the average mark is 59.875,which is smaller than 60,so Rob has failed this ICA.