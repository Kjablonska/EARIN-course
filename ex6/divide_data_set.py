import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

data_file = "./dataset/winequality-red.csv"

# -------------------------------------------------------------------------------------
#
# Function for splitting data into training, test and validation sets.
# It randomly splits data into training and test sets in ratio 80:20.
# We divide the wine based on the quality - bad is for qualities 2-6 and good is for 6-8.
# We assign bad qualities to 0 and good to 1.
#
# -------------------------------------------------------------------------------------

def divide_data_set():
    wine = pd.read_csv(data_file)
    # Divide data based on quality.
    bins = (2, 6, 8)
    group_names = ['bad', 'good']
    wine['quality'] = pd.cut(wine['quality'], bins = bins, labels = group_names)

    # Assign labels.
    labels = LabelEncoder()
    wine['quality'] = labels.fit_transform(wine['quality'])
    wine['quality'].value_counts()

    X = wine.drop('quality', axis = 1)
    y = wine['quality']

    # Plot showing wine quolities.
    # ax = sns.countplot(wine['quality'])
    # plt.show()

    # Divide data into training and test.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    sc = StandardScaler()

    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    return X_train, y_train, X_test, y_test
