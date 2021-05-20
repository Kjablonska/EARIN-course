import sklearn.metrics as metrics
import matplotlib.pyplot as plt


def validate_data(model, y_test, x_test, predition):

    print("\tData validation\n")
    print("\nAccuracy: ", metrics.accuracy_score(y_test, predition))
    print("Balanced accuracy: ", metrics.balanced_accuracy_score(y_test, predition))
    print("Average precision: ", metrics.average_precision_score(y_test, predition))
    print("F1 score: ", metrics.f1_score(y_test, predition))
    print("Recall score: ", metrics.recall_score(y_test, predition))
    print("ROC curve: \n", metrics.roc_curve(y_test, predition))
    print("Area under ROC curve: ", metrics.roc_auc_score(y_test, predition))

    print("Jaccard score: ", metrics.jaccard_score(y_test, predition))

    confusion_matrix = metrics.confusion_matrix(y_test, predition)
    print("Confusion matrix\n: ", confusion_matrix)

    metrics.plot_confusion_matrix(model, x_test, y_test, normalize='true')
    plt.title("Confusion marix")
    plt.show()

    metrics.plot_roc_curve(model, x_test, y_test)
    plt.title("Roc curve")
    plt.show()
