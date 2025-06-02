# Import necessary modules
import data_preprocessor as dp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the dataset
messy_data = pd.read_csv(r'C:\Users\simra\BINF-5507-Materials\Assignment1\Data\messy_data.csv')
clean_data = messy_data.copy()

# 2. Explore the dataset
# print("Initial Data Overview:")
# messy_data.head()
# messy_data.info()
# messy_data.describe()

#Convert target to categorical data
clean_data['target'] = clean_data['target'].astype('category')

messy_data['target'] = messy_data['target'].astype('category')
clean_data['target'] = clean_data['target'].astype('category')

#Identify outliers using histogram and scatter plot
# plt.figure(figsize=(10, 6))
# sns.histplot(messy_data['b'], bins=30, kde=True)
# plt.title('Distribution of Feature B')
# plt.xlabel('B')
# plt.ylabel('Frequency')
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.histplot(messy_data['c'], bins=30, kde=True)
# plt.title('Distribution of Feature C')
# plt.xlabel('C')
# plt.ylabel('Frequency')
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.histplot(messy_data['f'], bins=30, kde=True)
# plt.title('Distribution of Feature F')
# plt.xlabel('D')
# plt.ylabel('Frequency')
# plt.show()

# sns.scatterplot(data=messy_data, x='b', y='c', hue='target', alpha=0.6)
# plt.title('Scatter Plot of Features B vs C')
# plt.xlabel('B')
# plt.ylabel('C')
# plt.show()

# sns.scatterplot(data=messy_data, x='c', y='f', hue='target', alpha=0.6)
# plt.title('Scatter Plot of Features C vs F')
# plt.xlabel('C')
# plt.ylabel('D')
# plt.show()

sns.countplot(messy_data['target'])
plt.title('Bar Graph of Target')
plt.show()

sns.countplot(messy_data['d'])
plt.title('Bar Graph of D - Type of Defect')
plt.show()

sns.countplot(messy_data['s'])
plt.title('Bar Graph of S - Sex')
plt.show()

# clean_data = clean_data.drop(columns=['x', 'd', 'j', 'z'], axis=1)
# #print(clean_data.isnull().sum().sum())

# # 3. Impute missing values
# clean_data = dp.impute_missing_values(clean_data, strategy='mean')
# #print(clean_data.isnull().sum().sum())

# # clean_data.head()
# clean_data = dp.remove_duplicates(clean_data)
# ## clean_data.head()
# clean_data = dp.normalize_data(clean_data)
# #print(clean_data.shape)
# # clean_data.head()
# clean_data = dp.remove_redundant_features(clean_data, threshold=0.7)
# # clean_data.head()

# clean_data.to_csv(r'C:\Users\simra\BINF-5507-Materials\Assignment1\Data\clean_data.csv', index=False)

# dp.simple_model(clean_data)
# # Histogram for a numeric column
# plt.figure(figsize=(8, 5))
# plt.hist(messy_data['column_name'], bins=30, color='skyblue', edgecolor='black')
# plt.title('Histogram of column_name')
# plt.xlabel('column_name')
# plt.ylabel('Frequency')
# plt.show()

# # Scatter plot between two columns
# plt.figure(figsize=(8, 5))
# plt.scatter(messy_data['x_column'], messy_data['y_column'], alpha=0.6)
# plt.title('Scatter Plot of x_column vs y_column')
# plt.xlabel('x_column')
# plt.ylabel('y_column')
# plt.show()