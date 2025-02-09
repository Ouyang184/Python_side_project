# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("HepatitisCdata.csv")

# Inspect the data structure
print(data.info())
print(data.describe())

# Data Preprocessing
# Convert target variable to category type
data['Category'] = data['Category'].astype('category')
data['Sex'] = data['Sex'].astype('category')

# Handle missing values - impute with median
data.fillna(data.median(), inplace=True)

# Split the data into training and test sets
X = data.drop(columns=['Category'])
y = data['Category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Train a Random Forest model
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# Predict on the test set and evaluate
y_pred = rf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Feature Importance
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': rf.feature_importances_})
feature_importance.sort_values(by='Importance', ascending=False, inplace=True)

# Plot feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance)
plt.title("Feature Importance in Disease Prediction")
plt.show()

# Partial Dependence Plots
from sklearn.inspection import PartialDependenceDisplay

features = X.columns[:3]  # Change to include all relevant features
fig, ax = plt.subplots(figsize=(15, 10))
PartialDependenceDisplay.from_estimator(rf, X, features=features, ax=ax)
plt.tight_layout()
plt.show()
