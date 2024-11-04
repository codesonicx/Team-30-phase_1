import pandas as pd
import sys
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os
import mlflow

def evaluate_model(model_path, X_test_path, y_test_path, output_path, run_id):
    mlflow.set_tracking_uri("http://127.0.0.1:5000")  # Ajusta esto si es necesario
    try:
        # Verificar si el run_id existe
        run = mlflow.get_run(run_id)
        if run is None or run.info.status == "FINISHED":
            raise mlflow.exceptions.MlflowException(f"Run '{run_id}' not found or already finished.")

        model = joblib.load(model_path)
        X_test = pd.read_csv(X_test_path)
        y_test = pd.read_csv(y_test_path)

        predictions = model.predict(X_test)

        report = classification_report(y_test, predictions, zero_division=1)
        cm = confusion_matrix(y_test, predictions)

        with mlflow.start_run(run_id=run_id):
            accuracy = accuracy_score(y_test, predictions)
            mlflow.log_metric("accuracy", accuracy)

            report_dict = classification_report(y_test, predictions, output_dict=True)
            
            mlflow.log_metric("precision", report_dict['weighted avg']['precision'])
            mlflow.log_metric("recall", report_dict['weighted avg']['recall'])
            mlflow.log_metric("f1-score", report_dict['weighted avg']['f1-score'])
            
            mlflow.log_dict({"confusion_matrix": cm.tolist()}, "confusion_matrix.json")
        
        write_evaluation_report(output_path, report, cm)
    except mlflow.exceptions.MlflowException as e:
        print(f"Error: {e}")

def write_evaluation_report(file_path, report, confusion_matrix):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write("Classification Report:\n")
        f.write(report)
        f.write("\nConfusion Matrix:\n")
        f.write(str(confusion_matrix))

if __name__ == '__main__':
    model_path = sys.argv[1]
    X_test_path = sys.argv[2]
    y_test_path = sys.argv[3]
    output_path = sys.argv[4]

    run_id_file = sys.argv[5]
    with open(run_id_file, "r") as f:
        run_id = f.read().strip()

    evaluate_model(model_path, X_test_path, y_test_path, output_path, run_id)
