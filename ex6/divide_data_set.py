import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

data_file = "./dataset/winequality-red.csv"

# TODO: describe this well
def divide_data_set():
    wine = pd.read_csv(data_file)
    bins = (2, 6.5, 8)
    group_names = ['bad', 'good']
    wine['quality'] = pd.cut(wine['quality'], bins = bins, labels = group_names)
    label_quality = LabelEncoder()
    wine['quality'] = label_quality.fit_transform(wine['quality'])
    wine['quality'].value_counts()

    X = wine.drop('quality', axis = 1)
    y = wine['quality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    sc = StandardScaler()

    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    return X_train, y_train, X_test, y_test
