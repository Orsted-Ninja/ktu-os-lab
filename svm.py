from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
import numpy as np
dp=datasets.load_digits()
X=dp.data
y=dp.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
model=SVC(kernel='linear')
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(f"Confusion is {confusion_matrix(y_test,y_pred)}")
print(f"fSupp vecorts::::{model.support_vectors_}")
print(f"Total support vector{len(model.support_vectors_)}")
