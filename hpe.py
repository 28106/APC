# Heart Disease Prediction using SVM
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

# -----------------------------
# Step 1: Load the dataset
# -----------------------------
data = pd.read_csv("heart.csv")  # Make sure heart.csv is in the same folder

# -----------------------------
# Step 2: Data Preprocessing
# -----------------------------
X = data.drop(columns='target', axis=1)
y = data['target']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------------
# Step 3: Train the SVM model
# -----------------------------
model = SVC(kernel='rbf', class_weight='balanced', probability=True, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# Step 4: Evaluate the Model
# -----------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# Step 5: Predict for a New Person
# -----------------------------
new_data = np.array([[63, 1, 3, 145, 233, 1, 2, 150, 1, 2.3, 3, 2, 3]])
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)
probability = model.predict_proba(new_data_scaled)[0][1]

if prediction[0] == 1:
    print("🩺 The person is likely to have Heart Disease.")
    print(f"Probability: {probability*100:.2f}%")
else:
    print("✅ The person is not likely to have Heart Disease.")
    print(f"Probability: {probability*100:.2f}%")

# -----------------------------
# Step 6: Visualization
# -----------------------------
pl.close('all')

# 🔹 Scatter Plot — Age vs Cholesterol
pl.figure(figsize=(8, 6))
pl.scatter(data['age'][data['target'] == 0], data['chol'][data['target'] == 0],
           color='green', label='No Heart Disease', alpha=0.7)
pl.scatter(data['age'][data['target'] == 1], data['chol'][data['target'] == 1],
           color='red', label='Heart Disease', alpha=0.7)
pl.title('Age vs Cholesterol - Heart Disease Distribution')
pl.xlabel('Age')
pl.ylabel('Cholesterol')
pl.legend()
pl.grid(True)
pl.show()

# 🔹 Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap='coolwarm')
pl.title("Confusion Matrix - Heart Disease Prediction (SVM)")
pl.show()
