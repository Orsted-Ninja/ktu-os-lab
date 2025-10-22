import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn import tree

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
col_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
pima = pd.read_csv(url, header=None, names=col_names)

print("First 5 rows of the dataset:")
print(pima.head())
print("-" * 30)

feature_cols = ['Pregnancies', 'Glucose', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = pima[feature_cols] 
y = pima.Outcome      

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier(max_depth=3, random_state=1)
clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f"Accuracy: {metrics.accuracy_score(y_test, y_pred):.4f}")

fig = plt.figure(figsize=(15, 8))
tree.plot_tree(clf, 
               feature_names=feature_cols,
               class_names=['No Diabetes', 'Diabetes'], # 0 and 1
               filled=True,
               rounded=True)
plt.title("Decision Tree for Pima Diabetes Prediction")
plt.show()

# Save the figure to a file
fig.savefig("decision_tree.png")