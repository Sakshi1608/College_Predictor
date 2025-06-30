import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("COMEDKLIST-final.csv").sample(frac=1)

label_encoders = {}
for col in ['CITY', 'CATEGORY', 'BRANCH']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df[['CITY', 'CATEGORY', 'BRANCH', 'RANK']]
y = df.iloc[:, 0] 

model = RandomForestClassifier(n_estimators=100, bootstrap=True, max_features='sqrt')
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))
