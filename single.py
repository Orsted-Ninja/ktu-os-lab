import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn import datasets
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
df=datasets.load_diabetes()
dp=pd.DataFrame(df.data,columns=df.feature_names)
dp['target']=df.target
X=np.array(dp['bmi']).reshape(-1,1)#check if dropping target changes anything
y=np.array(dp['target'])
sns.lmplot(x='bmi',y='target',ci=None,data=dp)
sc=StandardScaler()
plt.show()

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LinearRegression()
X_tr=sc.fit_transform(X_train)
X_te=sc.transform(X_test)
model.fit(X_tr,y_train)
y_pred=model.predict(X_te)
plt.plot(X_te,y_pred,color="blue")
plt.show()
print(f"r2 is:{r2_score(y_test,y_pred)}")