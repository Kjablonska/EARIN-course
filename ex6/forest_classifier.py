from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

from validate_data import validate_data


def forest_classifier(X_train, y_train, X_test, y_test):
    random_forest = RandomForestClassifier()
    random_forest.fit(X_train, y_train)
    pred_random_forest = random_forest.predict(X_test)
    print("\t=======================    RANDOM FOREST  =======================")
    print(classification_report(y_test, pred_random_forest))
    print(confusion_matrix(y_test, pred_random_forest))

    validate_data(random_forest, y_test, X_test, pred_random_forest)
