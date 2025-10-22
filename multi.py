from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
df=datasets.fetch_california_housing()
dp=pd.DataFrame(df.data,columns=df.feature_names)
print(dp.head())
dp['target']=df.target
X=np.array(dp.drop('target',axis=1))
y=dp['target']
sns.lmplot(x="HouseAge",y='target',data=dp,ci=None)
plt.show()

sns.lmplot(x="AveRooms",y='target',data=dp,ci=None)
plt.show()
sns.lmplot(x="AveOccup",y='target',data=dp,ci=None)
plt.show()
sns.lmplot(x="MedInc",y='target',data=dp,ci=None)
plt.show()
sns.lmplot(x="AveBedrms",y='target',data=dp,ci=None)
plt.show()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LinearRegression()
sc=StandardScaler()
X_tr=sc.fit_transform(X_train)
X_te=sc.transform(X_test)
model.fit(X_tr,y_train)
y_pred=model.predict(X_te)
print(f"R2 is{r2_score(y_test,y_pred)}")