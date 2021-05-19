from sklearn.svm import SVC
from sklearn.metrics import classification_report

def svm(X_train, y_train, X_test, y_test):
    svc = SVC()
    svc.fit(X_train, y_train)
    pred_svc = svc.predict(X_test)
    print(classification_report(y_test, pred_svc))