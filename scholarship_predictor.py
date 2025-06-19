# scholarship_predictor.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample data
data = {
    "GPA": [3.9, 2.5, 3.2, 3.7, 3.0, 2.8, 4.0],
    "Family_Income": [25000, 60000, 40000, 30000, 70000, 50000, 20000],
    "Extracurriculars": [3, 0, 2, 4, 1, 1, 5],
    "Community_Hours": [120, 20, 60, 80, 10, 30, 150],
    "Test_Score": [1300, 900, 1100, 1200, 950, 1050, 1450],
    "Eligible": [1, 0, 1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)
X = df.drop("Eligible", axis=1)
y = df["Eligible"]

model = RandomForestClassifier()
model.fit(X, y)

def predict_eligibility(gpa, income, extracurriculars, hours, score):
    input_data = pd.DataFrame([[gpa, income, extracurriculars, hours, score]],
                              columns=X.columns)
    result = model.predict(input_data)[0]
    return "Eligible for scholarship" if result == 1 else "Not eligible for scholarship"
