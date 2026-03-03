import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


from sklearn.neighbors import KNeighborsClassifier # KNN
from sklearn.tree import DecisionTreeClassifier # Decision tree
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.ensemble import GradientBoostingClassifier # Gradient Boosting
from sklearn.linear_model import LogisticRegression # Logistic Regression

from sklearn.metrics import accuracy_score, roc_curve, auc

## Step 0: Business understanding, Data preparation, Quality checks, Outliers
## Step 1: Knowing Dependent Variables (DV), Independent Variables (IDVs)
  # Scale the IDVs for algorithms like KNN if variables are not comprable
## Step 2: Exploratory Analysis
## Step 3: Building model - OLS
       # KNN
       # Decision tree
       # Random Forest
       # Gradient Boosting
       # Logistic Regression
## Step 4: Evaluating model
       # Confusion Matrix
       # Accuracy, TPR (Recall), FPR, Precision
       # ROC (Receiver Operating Characteristics) Curve, AUC
       # Building model on training data and evaluating on test data
       # k fold cross validation
## Step 5: Go live and start predicting

irisdata = pd.read_csv("data/iris.csv")

################## Manual Classification ######################################

""" irisdata_withclasslabel = irisdata.copy()

"""
Pazhanivel
P.L < 3 and P.W < 0.5, setosa
P.L <> 3-5, P.W <> 0.5 - 1.5, versicolor
P.L > 5, P.W > 1.5, virginica
"""
irisdata_withclasslabel["Pazhanivel"] = "none"
irisdata_withclasslabel.loc[(irisdata["Petal.Length"] < 3) & 
                             (irisdata["Petal.Width"] < 0.5), "Pazhanivel"] = "setosa"
irisdata_withclasslabel.loc[(irisdata["Petal.Length"] >= 3) &
                             (irisdata["Petal.Length"] < 5) &
                             (irisdata["Petal.Width"] >= 0.5) &
                             (irisdata["Petal.Width"] < 1.5), "Pazhanivel"] = "versicolor"
irisdata_withclasslabel.loc[(irisdata["Petal.Length"] >= 5) & 
                             (irisdata["Petal.Width"] >= 1.5), "Pazhanivel"] = "virginica"
                        
"""
Anandraj
PL < 2 and PW < 1 then setosa
(PL > 3 and PL <5) and (PW >1 and PW <2) then  versicolor
else  virginica
"""
irisdata_withclasslabel["Anandraj"] = "virginica"
irisdata_withclasslabel.loc[(irisdata["Petal.Length"] < 2) & 
                             (irisdata["Petal.Width"] < 1), "Anandraj"] = "setosa"
irisdata_withclasslabel.loc[(irisdata["Petal.Length"] > 3) &
                             (irisdata["Petal.Length"] < 5) &
                             (irisdata["Petal.Width"] > 1) &
                             (irisdata["Petal.Width"] < 2), "Anandraj"] = "versicolor"

"""
Pradeep
Setosa = Petal.Length < 2, Petal.Width <0.6
Versicolor = 3 < Petal.Length < 5, 1 < Petal.Width < 1.8
Virginica = 5 < Petal.Length < 7, Petal.Width > 1.8
"""
irisdata_withclasslabel["Pradeep"] = "none"
irisdata_withclasslabel.loc[(irisdata["Petal.Length"] < 2) & 
                             (irisdata["Petal.Width"] < 0.6), "Pradeep"] = "setosa"
irisdata_withclasslabel.loc[(irisdata["Petal.Length"] > 3) &
                             (irisdata["Petal.Length"] < 5) &
                             (irisdata["Petal.Width"] > 1) &
                             (irisdata["Petal.Width"] < 1.8), "Pradeep"] = "versicolor"
irisdata_withclasslabel.loc[(irisdata["Petal.Length"] > 5) &
                             (irisdata["Petal.Length"] < 7) &
                             (irisdata["Petal.Width"] > 1.8) , "Pradeep"] = "virginica"

irisdata["Species"].value_counts() # 50 obs for each species
### Evaluate the results
sum(irisdata_withclasslabel["Species"] == irisdata_withclasslabel["Pazhanivel"])
126/150; #84% accuracy
pd.crosstab(irisdata_withclasslabel["Species"], irisdata_withclasslabel["Pazhanivel"])

sum(irisdata_withclasslabel["Species"] == irisdata_withclasslabel["Anandraj"])
135/150 #90% accuracy
pd.crosstab(irisdata_withclasslabel["Species"], irisdata_withclasslabel["Anandraj"])

sum(irisdata_withclasslabel["Species"] == irisdata_withclasslabel["Pradeep"])
119/150 #79.3% accuracy
pd.crosstab(irisdata_withclasslabel["Species"], irisdata_withclasslabel["Pradeep"])

irisspecies_properties = irisdata.groupby("Species").agg([min,np.mean,max])

"""
Karthik
"""
irisdata_withclasslabel["Karthik"] = "virginica"
irisdata_withclasslabel.loc[(irisdata["Petal.Width"] <= 0.8),"Karthik"] = "setosa" 
irisdata_withclasslabel.loc[(irisdata["Petal.Width"] > 0.8) & 
                             (irisdata["Petal.Width"] < 1.7), "Karthik"] = "versicolor"
sum(irisdata_withclasslabel["Species"] == irisdata_withclasslabel["Karthik"])
144/150 # 96% accuracy
pd.crosstab(irisdata_withclasslabel["Species"], irisdata_withclasslabel["Karthik"])
 """
######################
## Step 1:KNow your IDVs and DVs
# DV: Species (setosa, versicolor, virginica)
# IDVs: S.L, S.W, P.L, P.W

## Step 2 :Exploratory Analysis
irisspecies_properties = irisdata.groupby("Species").agg([min,np.mean,max])
""" . 1.	
• 	Groups the DataFrame by the unique values in the  column.
• 	Creates separate groups for each species (e.g., setosa, versicolor, virginica).
2. 	
• 	Applies three aggregation functions — , , and  — to each numeric column (like , , etc.).
• 	Uses NumPy’s  function for clarity and performance.
3. 	Result
• 	A new DataFrame  with a multi-level column index:
• 	Outer level: original column names (e.g., )
• 	Inner level: aggregation function (, , )
• 	Each row corresponds to a species, and each cell shows the result of the aggregation """.


for i in irisdata.columns[:4]:
    plt.figure()
    irisdata.groupby("Species")[i].agg(np.mean).plot.bar()

for i in irisdata.columns[:4]:
    irisdata.boxplot(by = "Species", column = i) 

sns.pairplot(irisdata, hue = "Species")

## Step 3: Building Model 
iris_train, iris_test = train_test_split(
        irisdata,
        test_size = 0.3,
        random_state = 1234)
iris_knn1 = KNeighborsClassifier(n_neighbors = 1).fit(
        iris_train.iloc[:,:4],iris_train["Species"])

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

# petal length and petal width are the most important features
## Step 4

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
for ki in range(1,20):
    print ("k = ",ki, "Accuracy = ",   
    np.mean(cross_val_score(KNeighborsClassifier(n_neighbors = ki),
                     irisdata.iloc[:,:4], # IDVs (X)
                     irisdata["Species"], # DV (y)
                     cv = 5))) # 5 fold cross validation
# k = 6 is the optimal with 98% cross validated accuracy

# Hyper parameter tuning for Decision tree
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

# Final model for production
iris_knn6 = KNeighborsClassifier(n_neighbors = 6).fit(
                                irisdata.iloc[:,:4],
                                irisdata["Species"])



################ Wine ##############################
winedata = pd.read_csv("data/wine.data", header = None)
winedata.columns = ["Wine_Class", "Alcohol","Malic_acid","Ash","Alcalinity_of_ash",
                       "Magnesium","Total_phenols","Flavanoids","Nonflavanoid_phenols",
                       "Proanthocyanins","Color_intensity","Hue","OD280_OD315",
                       "Proline"]

# DV: Wine Class
# IDVs: 13 attributes

# k = 1; test = 95+% accuracy

#######################3 Diabetes data ##############################
diabetes_data = pd.read_csv("data/diabetes_data.csv")

## Step 1
# DV: Class (1 - diabetic, 0 - Non diabetic)
# IDVs: 8 diagnostic measures

## Learn the mean and standard deviation from the given data
diabetes_scaling = StandardScaler().fit(diabetes_data.iloc[:,:8])

## Transforming the data to a common scale
diabetes_scaled = pd.DataFrame(diabetes_scaling.transform(
        diabetes_data.iloc[:,:8]),
                        columns = diabetes_data.columns[:8])
diabetes_scaled.apply(np.mean)
diabetes_scaled.apply(np.std)
diabetes_scaled["Class"] = diabetes_data["Class"]

## Step 2
diabetes_properties = diabetes_data.groupby("Class").agg([min,np.mean,max])

for i in diabetes_data.columns[:8]:
    plt.figure()
    diab_bar = diabetes_data.groupby("Class")[i].agg(np.mean).plot.bar()
    diab_bar.set_title(i)
for i in diabetes_data.columns[:8]:
    diabetes_data.boxplot(by = "Class", column = i)

sns.pairplot(diabetes_data, hue = "Class")


## Step 3 & Step 4

X_diab_train, X_diab_test, y_diab_train, y_diab_test = train_test_split(
        diabetes_scaled.iloc[:,:8], # IDVs (X)
        diabetes_scaled["Class"], # DV (y)
        test_size = 0.3,
        random_state = 1234)


for ki in range(1,30):
    print ("k = ",ki, "Accuracy = ",   
    np.mean(cross_val_score(KNeighborsClassifier(n_neighbors = ki),
                     diabetes_scaled.iloc[:,:8], # IDVs (X)
                     diabetes_scaled["Class"], # DV (y)
                     cv = 5))) # 5 fold cross validation
# k = 13 looks optimal with 78% cross validate accuracy

diabetes_knn13 = KNeighborsClassifier(n_neighbors = 13).fit(
        diabetes_scaled.iloc[:,:8],
        diabetes_scaled["Class"])

## Saving the model object as pickle file, very imp for deployment
diab_knn6_pickle = "output/diab_knn6_model.sav"
pickle.dump(diabetes_knn13, open(diab_knn6_pickle,"wb"))

## For future prediction in deployment scenario
diab_knn6_loaded = pickle.load(open("output/diab_knn6_model.sav","rb"))

# randomly sampling from raw data to simulate new data scenario
diab_new_data = diabetes_data.iloc[
        np.random.randint(1,392,10),:8] # new data for 10 patients. Only IDVs
diab_Scaled_new = diabetes_scaling.transform(diab_new_data)
pred_class = diab_knn6_loaded.predict(diab_Scaled_new)


########################33 Logistic Reression ################################

X_diab_train, X_diab_test, y_diab_train, y_diab_test = train_test_split(
        diabetes_data.iloc[:,:8], # IDVs (X)
        diabetes_data["Class"], # DV (y)
        test_size = 0.3,
        random_state = 1234)

diab_logistic = LogisticRegression().fit(X_diab_train,y_diab_train)

diab_pred_prob = diab_logistic.predict_proba(X_diab_test)
prob_diabetic = diab_pred_prob[:,1] # probability of being diabetic will be between 0 and 1

####### Prob cutoff = 0.5
diabetic_pred_class = np.zeros(len(y_diab_test))
diabetic_pred_class[prob_diabetic >= 0.5] = 1
pd.crosstab(y_diab_test,diabetic_pred_class)
y_diab_test.value_counts()
# Out of 85 non diabetic patients, 74 got correctly classified
# Out of 33 diabetic patients, 20 got correctly classified
#(74 + 20)/118 # 79.6% accuracy
#20/33 # 60.6% TPR
#11/85 # 12.9% FPR

accuracy_score(y_diab_test,diabetic_pred_class) # inbuilt function for calculating accuracy

## By default, predict function uses 0.5 cutoff
diabetic_pred_class_default = diab_logistic.predict(X_diab_test)
accuracy_score(y_diab_test,diabetic_pred_class_default)

######### Prob Cutoff = 0.3 to increase TPR
diabetic_pred_class = np.zeros(len(y_diab_test))
diabetic_pred_class[prob_diabetic >= 0.3] = 1
pd.crosstab(y_diab_test,diabetic_pred_class)
# Out of 85 non diabetic patients, 54 got correctly classified
# Out of 33 diabetic patients, 29 got correctly classified
#(54 + 29)/118 # 70.3% accuracy
#29/33 # 87.8% TPR
#31/85 # 36.4% FPR

######### Prob Cutoff = 0.7 to decrease FPR
diabetic_pred_class = np.zeros(len(y_diab_test))
diabetic_pred_class[prob_diabetic >= 0.7] = 1
pd.crosstab(y_diab_test,diabetic_pred_class)
# Out of 85 non diabetic patients, 3 got correctly classified
# Out of 33 diabetic patients, 8 got correctly classified#
#(82 + 8)/118 # 76.2% accuracy
#8/33 # 24.2% TPR
#3/85 # 3.5% FPR

### ROC Curve
diab_fpr, diab_tpr, diab_thresholds = roc_curve(y_diab_test,prob_diabetic)
plt.plot(diab_fpr,diab_tpr)
# TPR vs FPR tradeoff (ROC Curve, Receiver Operating Characteristics Curve)
# Precision vs Recall tradeoff (F1 score)

## AUC
# AUC will be between 0.5 to 1 where AUC=1 is a good model and AUC=0.5 is a bad model
auc(diab_fpr,diab_tpr) # 0.837 AUC



