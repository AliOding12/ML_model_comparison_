from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_and_evaluate(model, X_train, X_test, y_train, y_test):
    """
    Trains the model and evaluates accuracy on test set.
    Returns accuracy score.
    """
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return acc, preds

def detailed_report(y_true, y_pred):
    """
    Returns classification report and confusion matrix.
    """
    report = classification_report(y_true, y_pred)
    matrix = confusion_matrix(y_true, y_pred)
    return report, matrix
# Add training and evaluation script
# Enhance training loop
