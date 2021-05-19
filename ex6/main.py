from divide_data_set import divide_data_set
from forest_classifier import forest_classifier
from svm import svm
from gradient_boosting import gradient_boosting

def main():
    X_train, y_train, X_test, y_test = divide_data_set()
    predition = forest_classifier(X_train, y_train, X_test, y_test)
    svm(X_train, y_train, X_test, y_test)
    gradient_boosting(X_train, y_train, X_test, y_test)

main()