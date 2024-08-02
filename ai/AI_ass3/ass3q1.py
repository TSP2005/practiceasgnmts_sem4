import pandas as pd
a={
    'Std_Name' : ["john","Abraham","Micheal","Sung jin woo"], 'Roll_no':[1,2,3,4],'CPI':[90,34,50,75]}
df = pd.DataFrame(a)
print("Data frame is\n",df)
ndf = df[df['CPI'] > 60]
print("New Data frame is\n",ndf)
mean=df['CPI'].mean()
median=df['CPI'].median()
sd=df['CPI'].std()
print("\nOverall mean CPI:", mean)
print("Overall median CPI:", median)
print("Overall standard deviation CPI:", sd)