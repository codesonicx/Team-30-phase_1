import pandas as pd

def test_load_data_structure():
    data = pd.read_csv('data/raw/ai4i2020.csv')
    assert 'Product ID' in data.columns, "Column 'Product ID' is missing"
    assert len(data) > 0, "Data should not be empty"
