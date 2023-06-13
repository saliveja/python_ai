import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")
x = data.iloc[:,0:20] #columns
y = data.iloc[:,-1] #last column is target feature

model = ExtraTreesClassifier()
model.fit(x, y)
print(model.feature_importances_)

feat_importance = pd.Series(model.feature_importances_, index=x.columns)
feat_importances.nlargest(5).plot(kind='barh')
plot.show()

