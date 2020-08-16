import pandas as pd 
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import pandas as pd
import numpy as np




df=pd.read_csv("student-data.csv")
print(df)
#create a linear regression object
lr = lm.LinearRegression()

x= df.failures[:,np.newaxis]#indipendent variable
y= df.absences.values#dependent variables

lr.fit(x, y) 
print ("Intercept: ", lr.intercept_ )
print ("Coefficient: ", lr.coef_)

print("using predict function:",lr.predict(x))

plt.scatter(x,y, color='black')
plt.plot(x,lr.predict(x),color='blue',linewidth=3)
plt.title('Linear regression of student data pass/fail')
plt.ylabel("absences")
plt.xlabel("failures")



df.plot(kind="scatter",x="passed",y="schoolsup",title="Student perfomance analysis")

print(df.corr())