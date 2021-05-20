from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report
from validate_data import validate_data


def gradient_boosting(X_train, y_train, X_test, y_test):
    gradient_boosting = GradientBoostingClassifier(
        n_estimators=20, learning_rate=0.5, max_features=2, max_depth=2, random_state=0)
    gradient_boosting.fit(X_train, y_train)
    predictions = gradient_boosting.predict(X_test)
    print("\t=======================    GRADIENT BOOSTING  =======================")
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))

    validate_data(gradient_boosting, y_test, X_test, predictions)
