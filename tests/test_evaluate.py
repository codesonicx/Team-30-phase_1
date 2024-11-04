def test_evaluation_report():
    with open('reports/logistic_evaluation.txt', 'r') as f:
        report = f.read()
    assert 'accuracy' in report, "Accuracy metric missing in the report"
