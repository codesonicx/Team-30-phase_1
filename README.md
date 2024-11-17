# README phase_1.0.0 - Gobernanza del Modelo de Machine Learning para Predicción de Fallos de Maquinaria

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Phase 3 of predictive maintenance and setup of all tools and libraries for the project to be more scalable and maintainable.

## Descripción del Proyecto
Este proyecto utiliza técnicas de machine learning para predecir fallos en maquinaria industrial. El objetivo es identificar patrones y señales tempranas de fallos para realizar mantenimientos preventivos y reducir el tiempo de inactividad.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         phase_1.0.0 and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── phase_1.0.0   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes phase_1.0.0 a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

- **data/**: Contiene los conjuntos de datos utilizados para entrenar y evaluar el modelo.
- **notebooks/**: Jupyter notebooks con el análisis exploratorio de datos (EDA) y el desarrollo del modelo.
- **src/**: Código fuente del modelo y scripts de preprocesamiento de datos.
- **models/**: Modelos entrenados y sus versiones.
- **reports/**: Informes y visualizaciones de resultados.
- **docs/**: Documentación del proyecto.

## Requisitos
- Python 3.11
- Bibliotecas: requirements.txt

## Instalación

0. Install Python 3.11.9
   Ensure that you have Python 3.11.9 installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

1. Clonar el repositorio (Windows PowerShell):
   git clone https://github.com/ferchooz4/Team-30-phase_1 

2. Navegar al directorio del proyecto:
    cd Team-30-phase_1

3. Activar el Virtual Environment 
   .env\Scripts\Activate.ps1

4. Instalar las dependencias:
    pip install -r requirements.txt

5. Uso (por separado)
    Cargar los datos:
    python src/load_data.py
    
    Preprocesar los datos:
    python src/preprocess_data.py

    Entrenar el modelo:
    python src/train.py

    Evaluar el modelo:
    python src/evaluate.py

6. Uso (pipline)
    dvc repro

## Gobernanza del Modelo

### Transparencia y Trazabilidad
Registro de Datos: Todos los conjuntos de datos utilizados están documentados en docs/
Versionado de Modelos: Cada versión del modelo se almacena en el directorio models/ 

### Evaluación y Documentación
Métricas de Rendimiento: Las métricas de evaluación del modelo se documentan en reports/
Se utilizan herramientas GIT, DVC, MLFlow para el versionado de código, datos y modelos.

### Monitoreo y Mantenimiento
Monitoreo en Producción: Se implementan scripts para monitorear el rendimiento del modelo en producción y detectar posibles degradaciones.
Actualización del Modelo: Procedimientos para reentrenar y actualizar el modelo con nuevos datos se documentan en docs/

## Roles y responsabilidades

### Line of Business y Subject Matter Expert
**Responsable:** Jorge Mariles Estrada
- Definir el impacto de la problemática del negocio.
- Entender los datos capturados y su relevancia para el negocio.
- Colaborar con el equipo técnico para asegurar que las soluciones propuestas se alineen con los objetivos del negocio.
- Proveer contexto y conocimiento especializado sobre el dominio del problema.

### Data Scientist
**Responsable:** Jose Luis Artigas Arroyo
- Preparar y explorar los datos disponibles.
- Realizar análisis exploratorio de datos (EDA) para identificar patrones y relaciones.
- Seleccionar y crear características relevantes para el modelo.
- Desarrollar y evaluar modelos de machine learning.
- Documentar y comunicar los hallazgos y resultados del análisis de datos.

### ML Architect 1
**Responsable:** Antonio Olvera Donlucas
- Diseñar y mejorar el modelo de machine learning.
- Seleccionar algoritmos y técnicas adecuadas para el problema.
- Optimizar el rendimiento del modelo mediante ajuste de hiperparámetros.
- Implementar técnicas de validación cruzada y evaluación del modelo.
- Asegurar la escalabilidad y eficiencia del modelo en producción.

### ML Architect 2
**Responsable:** Jorge Antonio Acosta Rosales
- Refactorizar el código del modelo para mejorar su eficiencia y mantenibilidad.
- Implementar buenas prácticas de codificación y diseño de software.
- Asegurar la modularidad y reutilización del código.
- Colaborar con el equipo de data engineering para integrar el modelo en el pipeline de datos.
- Realizar pruebas unitarias y de integración para asegurar la calidad del código.

### Data Engineer
**Responsable:** Fernando Jaime Sánchez
- Diseñar y construir pipelines de datos eficientes y escalables.
- Implementar procesos de extracción, transformación y carga (ETL) de datos.
- Gestionar el versionado de datos y asegurar la reproducibilidad de los experimentos.
- Colaborar con los científicos de datos y arquitectos de ML para asegurar la disponibilidad y calidad de los datos.
- Monitorear y mantener los pipelines de datos en producción.


--------

