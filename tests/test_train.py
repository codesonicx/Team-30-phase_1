import pickle

def test_model_saving():
    with open('models/logistic_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
    assert model is not None, "Model could not be loaded"
