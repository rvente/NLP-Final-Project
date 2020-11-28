from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.svm import LinearSVC
from sacred import Experiment
from dataset_ingredient import auth100docs50, load_data


# add the Ingredient while creating the experiment
ex = Experiment('support vector classifier', ingredients=[auth100docs50])


@ex.automain
def svc(_log):
    X_train, X_test, y_train, y_test = load_data()
    svm = LinearSVC()
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")
    ex.log_scalar("test.accuracy", accuracy)
    ex.log_scalar("test.confusion", str(confusion))
    ex.log_scalar("test.f1_score", f1)
    _log.info(f"acc={accuracy}, f1={f1}")
    return accuracy
