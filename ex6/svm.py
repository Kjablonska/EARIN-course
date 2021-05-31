from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

from validate_data import validate_data


def svm(X_train, y_train, X_test, y_test):
    svc = SVC()
    svc.fit(X_train, y_train)
    pred_svc = svc.predict(X_test)
    print("\t=======================    SVC  =======================")
    validate_data(svc, y_test, X_test, pred_svc)
