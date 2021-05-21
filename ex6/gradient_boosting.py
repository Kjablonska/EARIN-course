from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report
from validate_data import validate_data


def gradient_boosting(X_train, y_train, X_test, y_test):
    gradient_boosting = GradientBoostingClassifier()
    gradient_boosting.fit(X_train, y_train)
    predictions = gradient_boosting.predict(X_test)
    print("\t=======================    GRADIENT BOOSTING  =======================")
    validate_data(gradient_boosting, y_test, X_test, predictions)
