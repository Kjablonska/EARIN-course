import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import numpy as np


def validate_data(model, y_test, x_test, predition):

    print("\tData validation\n")
    print("\nAccuracy:\t\t ", metrics.accuracy_score(y_test, predition))
    print("Balanced accuracy:\t ", metrics.balanced_accuracy_score(y_test, predition))
    print("Average precision:\t ", metrics.average_precision_score(y_test, predition))
    print("F1 score:\t\t ", metrics.f1_score(y_test, predition))
    print("Recall score:\t\t ", metrics.recall_score(y_test, predition))
    print("ROC curve:\t \n", np.asarray(metrics.roc_curve(y_test, predition)))
    print("Area under ROC curve:\t ", metrics.roc_auc_score(y_test, predition))

    print("Jaccard score:\t\t ", metrics.jaccard_score(y_test, predition))

    print("\nClassification report:\n\t", metrics.classification_report(y_test, predition))
    confusion_matrix = metrics.confusion_matrix(y_test, predition)
    print("\nConfusion matrix\t\n ", np.asarray(confusion_matrix))

    metrics.plot_confusion_matrix(model, x_test, y_test, normalize='true')
    plt.title("Confusion marix")
    plt.show()

    metrics.plot_roc_curve(model, x_test, y_test)
    plt.title("Roc curve")
    plt.show()
