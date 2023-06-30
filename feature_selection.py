import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

data = pd.read_csv('data/train.csv')

x = data.iloc[:,0:20] #columns
y = data.iloc[:,-1] #last column for target feature

bestfeatures = SelectKBest(score_func=chi2, k=5)
#select the five best options

fit = bestfeatures.fit(x, y)

dfscores = pd.DataFrame(fit.scores_)
# scores from all features

dfcolumns = pd.DataFrame(x.columns)
# name of all features

scores = pd.concat([dfcolumns, dfscores], axis=1)
# name and score for all features

scores.columns = ['specs', 'score']
# name of columns

print(scores.nlargest(5, 'score'))
# printing five best features




