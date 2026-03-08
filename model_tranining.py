import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score, accuracy_score
import pickle

data = pd.read_csv('dataset.csv')


X_reg = data[['Age', 'Experience', 'Matches Played', 'Total Runs', 'Performance Rating']]
y_reg = data['Salary']


X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

reg_model = LinearRegression()
reg_model.fit(X_train_reg, y_train_reg)

y_pred_reg = reg_model.predict(X_test_reg)
r2 = r2_score(y_test_reg, y_pred_reg)
print(f"R² Score: {r2}")

with open('model.pkl', 'wb') as f:
    pickle.dump(reg_model, f)


def classify_salary(salary):
    if salary < 50000:
        return 'Low'
    elif 50000 <= salary < 100000:
        return 'Medium'
    else:
        return 'High'

data['Salary Category'] = data['Salary'].apply(classify_salary)

X_clf = data[['Age', 'Experience', 'Matches Played', 'Total Runs', 'Performance Rating']]
y_clf = data['Salary Category']


X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

clf_model = RandomForestClassifier(random_state=42)
clf_model.fit(X_train_clf, y_train_clf)

y_pred_clf = clf_model.predict(X_test_clf)
accuracy = accuracy_score(y_test_clf, y_pred_clf)
print(f"Classification Accuracy: {accuracy}")

with open('classifier.pkl', 'wb') as f:
    pickle.dump(clf_model, f)
