import pandas as pd

def test_preprocess_output_shapes():
    X_train = pd.read_csv('data/processed/X_train.csv')
    y_train = pd.read_csv('data/processed/y_train.csv')
    assert X_train.shape[0] == y_train.shape[0], "Mismatch in training data sizes"
