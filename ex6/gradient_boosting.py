from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report
from validate_data import validate_data


def gradient_boosting(X_train, y_train, X_test, y_test):
    gb = GradientBoostingClassifier(n_estimators=20, learning_rate=0.5, max_features=2, max_depth=2, random_state=0)
    gb.fit(X_train, y_train)
    predictions = gb.predict(X_test)
    print("============================================")
    print("GRADIENT BOOSTING")
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))

    validate_data(y_test, X_test, predictions)