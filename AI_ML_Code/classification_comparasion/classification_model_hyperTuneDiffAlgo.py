import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


from sklearn.neighbors import KNeighborsClassifier # KNN
from sklearn.tree import DecisionTreeClassifier # Decision tree
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.ensemble import GradientBoostingClassifier # Gradient Boosting
from sklearn.linear_model import LogisticRegression # Logistic Regression

from sklearn.metrics import accuracy_score, roc_curve, auc

## Step 1:KNow your IDVs and DVs
# DV: Species (setosa, versicolor, virginica)
# IDVs: S.L, S.W, P.L, P.W

irisdata = pd.read_csv("data/iris.csv")

## Step 2 :Exploratory Analysis
irisspecies_properties = irisdata.groupby("Species").agg([min,np.mean,max])

for i in irisdata.columns[:4]:
    plt.figure()
    irisdata.groupby("Species")[i].agg(np.mean).plot.bar()

for i in irisdata.columns[:4]:
    irisdata.boxplot(by = "Species", column = i) 

sns.pairplot(irisdata, hue = "Species")

## Step 3: Building Model 
#split the data into train and test
""" iris_train, iris_test = train_test_split(
        irisdata,
        test_size = 0.3,
        stratify = irisdata["Species"],
        random_state = 1234
    ) """

# use train test split function to even split DVs and IDVs
X_iris_train, X_iris_test, y_iris_train, y_iris_test = train_test_split(
        irisdata.iloc[:,:4], # IDVs (X)
        irisdata["Species"], # DV (y)
        test_size = 0.3,
        random_state = 1234)

# Building model on training data
iris_knn1 = KNeighborsClassifier(n_neighbors = 1).fit(X_iris_train,y_iris_train)
iris_dtree = DecisionTreeClassifier(criterion = "gini", max_depth = 2,
                random_state = 1234).fit(X_iris_train,y_iris_train)
iris_dtree.feature_importances_

# Evaluating on training data
iris_species_pred_tr_knn1 = iris_knn1.predict(X_iris_train)
pd.crosstab(y_iris_train,iris_species_pred_tr_knn1) # confusion matrix
# 100% accuracy on training data

# Evaluating on test data
iris_species_pred_te_knn1 = iris_knn1.predict(X_iris_test)
pd.crosstab(y_iris_test,iris_species_pred_te_knn1)
#44/45# 97.7% accuracy on test data

## Cross validation
np.mean(cross_val_score(KNeighborsClassifier(n_neighbors = 1),
                 irisdata.iloc[:,:4], # IDVs (X)
                 irisdata["Species"], # DV (y)
                 cv = 5)) # 5 fold cross validation
# 96% cross validated accuracy

# Hyper parameter tuning for KNN
print("Hyper parameter tuning for KNN")
for ki in range(1,20):
    print ("k = ",ki, "Accuracy = ",   
    np.mean(cross_val_score(KNeighborsClassifier(n_neighbors = ki),
                     irisdata.iloc[:,:4], # IDVs (X)
                     irisdata["Species"], # DV (y)
                     cv = 5))) # 5 fold cross validation
# k = 6 is the optimal with 98% cross validated accuracy

# Hyper parameter tuning for Decision tree
print("Hyper parameter tuning for Decision tree")
for cri in ["gini","entropy"]:
    for depthi in range(1,10):
        print ("Criterion = ", cri,
               "Max Depth = ",depthi, "Accuracy = ",   
        np.mean(cross_val_score(DecisionTreeClassifier(
                        criterion = cri,
                        max_depth = depthi, random_state = 1234),
                         irisdata.iloc[:,:4], # IDVs (X)
                         irisdata["Species"], # DV (y)
                         cv = 5))) # 5 fold cross validation
# Max depth = 4, criterion = gini is the optimal with 96.6% cross validated accuracy

## Hyper parameter tuning for Random Forest
print("Hyper parameter tuning for Random Forest")  
model_perf_rf_dict = dict()
for esti in range(1,11):
    for depthi in range(1,10):    
        model_perf_rf_dict["Estimators = " + str(esti) + 
                        "Max Depth = " + str(depthi)] = np.mean(
                           cross_val_score(RandomForestClassifier(
                        n_estimators  = esti,
                        max_depth = depthi, random_state = 1234),
                         irisdata.iloc[:,:4], # IDVs (X)
                         irisdata["Species"], # DV (y)
                         cv = 5)) # 5 fold cross validation
# Number of estimatrs= 5, Depth = 6 has 96.6% cross validated accuracy

print("Hyper parameter tuning for Gradient Boosting")      
## Hyper parameter tuning for Boosting
model_perf_gbm_dict = dict()
for esti in range(10,500,50):
    for learni in [0.1,0.2,0.3,0.4,0.5]:    
        model_perf_gbm_dict["Estimators = " + str(esti) + 
                        " Learning Rate= " + str(learni)] = np.mean(
                            cross_val_score(GradientBoostingClassifier(
                        n_estimators  = esti,
                        learning_rate  = learni, 
                        random_state = 1234),
                         irisdata.iloc[:,:4], # IDVs (X)
                         irisdata["Species"], # DV (y)
                         cv = 5)) # 5 fold cross validation
# Estimatore = 10, Learning Rate = 0.2 gives 96.6% accuracy

print("Final model for production")
# Final model for production
iris_knn6 = KNeighborsClassifier(n_neighbors = 6).fit(
                                irisdata.iloc[:,:4],
                                irisdata["Species"])