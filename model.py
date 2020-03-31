import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("COMEDKLIST - final.csv")
df=df.sample(frac=1)
enc=LabelEncoder()
enc.fit(df.CITY)
df.CITY=enc.transform(df.CITY)
enc.fit(df.CATEGORY)
df.CATEGORY=enc.transform(df.CATEGORY)
enc.fit(df.BRANCH)
df.BRANCH=enc.transform(df.BRANCH)
x=df.iloc[:,[1,2,3,4]].values
y=df.iloc[:,0]
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100, 
                               bootstrap = True,
                               max_features = 'sqrt')

classifier.fit(x,y)


pickle.dump(classifier,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

