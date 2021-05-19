from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

def forest_classifier(X_train, y_train, X_test, y_test):
    rfc = RandomForestClassifier(n_estimators=200)
    rfc.fit(X_train, y_train)
    pred_rfc = rfc.predict(X_test)
    print(classification_report(y_test, pred_rfc))
    print(confusion_matrix(y_test, pred_rfc))