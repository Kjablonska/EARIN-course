import sklearn.metrics as metrics


def validate_data(y_test, x_test, predition):
    print("\nAccuracy: ", metrics.accuracy_score(y_test, predition))
    # print("Accuracy score", rmodel.score(x_test, y_test))
    print("Balanced accuracy: ", metrics.balanced_accuracy_score(y_test, predition))
    print("Average precision: ", metrics.average_precision_score(y_test, predition))
    print("F1 score: ", metrics.f1_score(y_test, predition))
    print("Recall score: ", metrics.recall_score(y_test, predition))
    print("ROC curve: ", metrics.roc_curve(y_test, predition))
    print("Area under ROC curve: ", metrics.roc_auc_score(y_test, predition))
    print("Confusion matrix: ", metrics.confusion_matrix(y_test, predition))
    print("Jaccard score: ", metrics.jaccard_score(y_test, predition))

    # print("Top K accuracy: ", metrics.top_k_accuracy())
    # print("Brier score loss: ", metrics.brier_score_loss(y_test, proba))
