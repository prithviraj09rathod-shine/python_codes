""" The following four types of unsupervised techniques are used:

1.PCA Decomposition (Dimensionality Reduction)
2.K-Means Clustering (Centroid Based) Clustering
3.Hierarchical (Divisive and Agglomerative) Clustering
4.DBSCAN (Density Based) Clustering
 """
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
##Data analysis baseline library
import dabl
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

#get data from kaggle and read it
data = pd.read_csv('input/unsupervised-learning-on-country-data/Country-data.csv')
print(data.head())
print(data.info())
data.describe()
#checking for null values
print(data.isnull().sum())
#To know the 10 headinsg values of the dataset like country,income,gdpp etc
data.head(10)
#no null values found

warnings.filterwarnings('ignore')
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 6)
dabl.plot(data, target_col = 'gdpp')
"""We can observe very close positive correlation between "Income" and "GDPP". Also, "Exports", "Imports", "Health" have sort of positive correlation with "GDPP".
"Country" is a feature which is not required here for unsupervised learning.Because it is not a deciding parameter to keep/not-keep a particular record within a cluster.
"""
# Hence exclude "Country" column
data = data.drop('country', axis=1)

""" 1) Principal Component Analysis
Principal Component Analysis (PCA) is a popular technique for deriving a set of low dimensional features from a large set of variables.
This could represent distinct no. of groups with similar characteristics. 
Hence PCA can be an insightful clustering tool (or a preprocessing tool before applying clustering as well). 
We will standardize our data first and will use the scaled data for all clustering works. """
#scaling the data
sc=StandardScaler()
data_scaled=sc.fit_transform(data)


pc = PCA(svd_solver='auto')
pc.fit(data_scaled)
print('Total no. of principal components =',pc.n_components_)
#Print Principal Components
print('Principal Component Matrix :\n',pc.components_)
#The amount of variance that each PC explains
var = pc.explained_variance_ratio_
print(var)

#Plot explained variance ratio for each PC
plt.bar([i for i, _ in enumerate(var)],var,color='black')
plt.title('PCs and their Explained Variance Ratio', fontsize=15)
plt.xlabel('Number of components',fontsize=12)
plt.ylabel('Explained Variance Ratio',fontsize=12)
#For convenience of observation, we are converting the figures to percentages here.
#Cumulative Variance explained by each PC
import numpy as np
cum_var = np.cumsum(np.round(pc.explained_variance_ratio_, decimals=4)*100)
print(cum_var)

# Scree Plot : used to determine the number of principal components to keep in this principal component analysis
plt.plot(cum_var, marker='o')
plt.title('Scree Plot: PCs and their Cumulative Explained Variance Ratio',fontsize=15)
plt.xlabel('Number of components',fontsize=12)
plt.ylabel('Cumulative Explained Variance Ratio',fontsize=12)
#The plot indicates the threshold of 90% is getting crossed at PC = 4. 
# Ideally, we can keep 4 (or atmost 5) components here
""" Before PC = 5, the plot is following an upward trend. After crossing 5, it is almost steady.
However, we have retailed all 9 PCs here to get the full data in results. And for visualization purpose in 2-D figure,
we have plotted only PC1 vs PC2. """
#Principal Component Data Decomposition
colnames = list(data.columns)
pca_data = pd.DataFrame({ 'Features':colnames,'PC1':pc.components_[0],'PC2':pc.components_[1],'PC3':pc.components_[2],
                          'PC4':pc.components_[3],'PC5':pc.components_[4], 'PC6':pc.components_[5], 'PC7':pc.components_[6], 
                          'PC8':pc.components_[7], 'PC9':pc.components_[8]})
print(pca_data)
#Visualize 2 main PCs
fig = plt.figure(figsize = (12,6))
#sns.scatterplot(pca_data.PC1,pca_data.PC2,hue=pca_data.Features,marker='o', s=500)
sns.scatterplot(x=pca_data.PC1, y=pca_data.PC2, hue=pca_data.Features, marker='o', s=500)

plt.title('PC1 vs PC2',fontsize=15)
plt.xlabel('Principal Component 1',fontsize=12)
plt.ylabel('Principal Component 2',fontsize=12)
plt.show()
""" We can see that 1st Principal Component (X-axis) is gravitated mainly towards features like:
life expectancy, gdpp, income. 2nd Principal Component (Y-axis) is gravitated predominantly
towards features like: imports, exports """
#Export PCA results to file
pca_data.to_csv("PCA_results.csv", index=False)
###Sucefssfully completed PCA Decomposition ###
