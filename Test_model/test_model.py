import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset.csv")

X = df[["Temp", "Vibration", "Carbon"]]
y = df["Label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred,
      target_names=["Normal", "Warning", "Critical"]))  # ← Added labels

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
labels = ["Normal", "Warning", "Critical"]           # ← Added labels
sns.heatmap(cm, annot=True, fmt="d",
            xticklabels=labels, yticklabels=labels,  # ← Shows names
            cmap="Blues")
plt.title("Confusion Matrix - Laptop Health Monitor")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.tight_layout()
plt.savefig("confusion_matrix.png")                  # ← Saves as image
plt.show()

# Save model
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")
