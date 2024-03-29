from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler

def load_iris(test_size=0.3, random_state=42):
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    return _prepare_data(X, y, test_size, random_state)

def load_wine(test_size=0.3, random_state=42):
    wine = datasets.load_wine()
    X, y = wine.data, wine.target
    return _prepare_data(X, y, test_size, random_state)

def load_digits(test_size=0.3, random_state=42):
    digits = datasets.load_digits()
    X, y = digits.data, digits.target
    return _prepare_data(X, y, test_size, random_state)

def _prepare_data(X, y, test_size, random_state):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test

def load_titanic(test_size=0.3, random_state=42):
    df = pd.read_csv("F:\\Coding_Projects\\ml_models_project\\data\\train.csv")
    
    # Example preprocessing: drop missing values & select columns
    df = df.dropna(subset=["Age", "Fare", "Sex", "Pclass"])
    
    # Convert categorical 'Sex' to numeric
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    
    # Features and target
    X = df[["Pclass", "Sex", "Age", "Fare"]]
    y = df["Survived"]
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test

# Add data loader script
