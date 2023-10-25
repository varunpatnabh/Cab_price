# from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor, XGBRFRegressor

from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import xgboost as xgb
from catboost import CatBoostClassifier

model_list1 = [("XgBoost ", XGBRegressor()),
              ("CatBoost", CatBoostRegressor(verbose=False)),
            #   ("LGBM ",LGBMRegressor(verbose=-1))
              ]

model_list = [("Logistic Regression", LogisticRegression(max_iter=10000)),
              #("Random Forest", RandomForestClassifier()),
              #("xgb",xgb.XGBClassifier()), 
              #("cat_boost",CatBoostClassifier(iterations=1000, learning_rate=0.1, depth=6, loss_function='MultiClass', verbose=100)),       
              #("Neural Network", MLPClassifier(max_iter=1000))
              ]