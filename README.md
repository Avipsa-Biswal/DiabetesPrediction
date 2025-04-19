#Diabetes Prediction Using Machine Learning 🩺 

Early detection of diabetes can significantly improve patient outcomes and reduce the risk of complications. This project applies machine learning techniques to predict the likelihood of diabetes based on medical and demographic data. It serves as both a practical healthcare tool and a hands-on ML learning project.

🎯 Objective
To build and evaluate multiple machine learning models that can accurately classify individuals as diabetic or non-diabetic using features such as glucose level, BMI, age, and other clinical measurements.

📊 Dataset
Source: Pima Indians Diabetes Dataset (available on Kaggle and UCI ML Repository)

Records: 768 patient entries

Features: 8 medical predictors + 1 target variable

Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, Diabetes Pedigree Function, Age

Target: Outcome (0 = non-diabetic, 1 = diabetic)

🧪 Methodology
Exploratory Data Analysis (EDA)

Visualized distributions and correlations using histograms, heatmaps, and pairplots.

Data Preprocessing

Handled missing or zero values using imputation techniques

Normalized/standardized features for model compatibility

Model Training

Trained and compared various classification models:

Logistic Regression

K-Nearest Neighbors (KNN)

Decision Tree

Random Forest

Support Vector Machine (SVM)

Evaluation Metrics

Accuracy, Precision, Recall, F1-score, and Confusion Matrix used to assess model performance.

Model Selection

Best-performing model saved using pickle for potential deployment.

🚀 Results
Models were evaluated and compared based on their predictive accuracy and generalization.

Ensemble approaches or hyperparameter tuning could further enhance performance in future iterations.

📁 Project Structure
data/: Contains the diabetes.csv dataset from the Pima Indians Diabetes Database.

notebooks/: Jupyter notebooks for EDA, model training, and evaluation.

Diabetes_Prediction.ipynb: Complete ML pipeline.

src/: Modular code scripts.

preprocessing.py: Handles missing values and scaling.

train_models.py: Trains and evaluates ML models.

models/: Stores saved models for reuse (trained_model.pkl).

results/: Includes performance outputs like confusion_matrix.png and metrics_report.txt.

requirements.txt: Lists project dependencies.

README.md: Project documentation and overview.

💡 Motivation
Healthcare Impact: Diabetes is a global health issue — early prediction can guide early intervention.

Educational Value: Offers a practical implementation of ML classification pipelines.

Scalability: Models can be extended for deployment into web apps or APIs for real-world use.

🔧 Installation & Setup

Clone the repository:
git clone https://github.com/Avipsa-Biswal/DiabetesPrediction.git

cd DiabetesPrediction


Create a virtual environment and install dependencies:

pip install -r requirements.txt


Run the Jupyter Notebook:

jupyter notebook notebooks/Diabetes_Prediction.ipynb
