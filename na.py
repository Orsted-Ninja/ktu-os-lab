import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.metrics import r2_score,accuracy_score,precision_score,recall_score,confusion_matrix
df=datasets.load_iris()
dp=pd.DataFrame(df.data,columns=df.feature_names)
#print(df.DESCR)
dp['target']=df.target
X=np.array(dp.drop('target',axis=1))
y=np.array(dp['target'])           
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred,average="weighted")
recall=recall_score(y_test,y_pred,average="weighted")
cm=confusion_matrix(y_test,y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm,annot=True,fmt="d",cmap="Blues",xticklabels=df.target_names,yticklabels=df.target_names)
plt.title("CM")
plt.show()

metrics=['Accuracy','Precision','Recll']
values=[accuracy,precision,recall]
plt.bar(metrics,values)
plt.title("performance")
plt.ylim(0,1)
plt.show()
print(r2_score(y_test,y_pred))




