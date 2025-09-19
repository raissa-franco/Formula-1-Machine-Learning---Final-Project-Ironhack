# 🏎️ Formula 1 - Machine Learning Project

A machine learning project that analyzes historical Formula 1 data to predict whether a driver will finish in the **Top 10** of a given race. The project explores the most influential features and compares the performance of different classification models.

---

## 📌 1. General Description

This project uses a consolidated dataset with results from over **27,000 races** since 1950, provided by the **Ergast API** and available on Kaggle. The main goal is to understand which factors most influence a driver's race outcome and to build predictive models capable of estimating their chances of finishing in the Top 10.

---

## 📊 2. Project Overview

### 🔍 What does this project do?

- Analyzes historical F1 race data focused on driver performance.
- Applies **feature engineering**, **data balancing**, and **classification modeling**.
- Evaluates model performance using **Random Forest**, **CatBoost**, and **XGBoost**.

### 🎯 What problem does it solve?

- Identifies key features that increase a driver's likelihood of finishing in the Top 10.
- Provides actionable insights for F1 teams, fans, and analysts.
- Demonstrates real-world machine learning application on imbalanced, multi-source data.

### 🌍 Potential Impact / Practical Applications

- **F1 Teams**: Data-driven decision support based on race history and probability.
- **Data Scientists**: Hands-on experience with imbalanced, real-world sports data.

---

## 📁 3. Dataset Description

- 📦 **Source**: [Kaggle - Formula 1 Race Data](https://www.kaggle.com/datasets/jtrotman/formula-1-race-data)
- 📅 Covers races from 1950 to recent seasons.
- 📂 Contains 14 structured CSV files (drivers, constructors, circuits, results, standings, etc.).
- ✅ Clean and well-organized data, no significant missing values.

---

## 🎯 4. Project Objective / ML Problem

- Binary classification problem: **Predict whether a driver will finish in the Top 10**.
- Compare performance across different models and balancing strategies.
- Analyze feature importance and their influence on final race outcomes.

---

## ⚙️ 5. Steps Taken

### 1. Feature Engineering
- Merged multiple sources (drivers, races, constructors, results, etc.).
- Created new features such as number of past races, average position, total points, and more.

### 2. Data Preprocessing & Analysis
- Correlation analysis to detect feature relationships.
- Encoding of categorical variables.
- Feature scaling and transformation.

### 3. Data Balancing
- Applied the **ADASYN** technique to handle class imbalance (Top 10 vs. Not Top 10).

### 4. Model Training
- Models tested: **Random Forest**, **CatBoostClassifier**, **XGBoostClassifier**.
- Best performance achieved using **XGBoost + ADASYN** with **~70% accuracy**.

---

## 🔍 6. Key Findings

- **XGBoost with ADASYN** achieved the highest accuracy (~70%).
- Top influential features included:
  - Driver’s past performance
  - Constructor (team)
  - Number of prior races
  - Starting position
- The model showed good generalization and could be further improved with contextual data (e.g., weather, penalties, incidents).

---


## 🧪 7. How to Run the Project

You can reproduce this project in two parts:

- 📒 A Jupyter Notebook for data analysis and model training  
- 🖥️ A Streamlit web app for deploying the trained model

---

### 🔧 Notebook Environment

Recommended Python version: 3.11+

Install the notebook requirements:

pip install -r Formula_1_Project/requirements_notebook.txt

Run the notebook:

jupyter notebook Formula_1_Project/Project_top10.ipynb

---

### 🚀 Streamlit Web App

Install the app requirements:

pip install -r Streamlit_app/requirements.txt

Run the app:

cd Streamlit_app  
streamlit run app.py

Make sure the following files are present in the Streamlit_app folder:

- app.py – Streamlit application code  
- best_model.pkl – Trained model file  
- label_enc.pkl – Label encoder for categorical variables  

Once the app starts, it will open in your browser at:

http://localhost:8501/

## 🗂️ 8. Repository Structure

| Path                          | Description                                        |
|-------------------------------|------------------------------------------------    |
| `Formula_1_Project/`          | Main project folder with notebook and dependencies |
| ├── `Project_top10.ipynb`     | Main Jupyter notebook with analysis and modeling   |
| ├── `requirements_notebook.txt` | Python packages required for the notebook        |
| `Streamlit_app/`              | Streamlit app for web deployment                   |
| ├── `app.py`                  | Streamlit application code                         |
| ├── `best_model.pkl`          | Trained model file                                 |
| ├── `label_enc.pkl`           | Label encoder for categorical features             |
| ├── `requirements.txt`        | Streamlit app dependencies                         |
| `FORMULA 1.pdf`               | Slide deck with project presentation               |
| `README.md`                   | Project documentation (this file)                  |

---

## 🚀 9. Next Steps / Improvements

- Include contextual features such as weather, penalties, and race incidents to improve model accuracy.
- Explore deep learning models to capture sequential and temporal race data.
- Expand the prediction task from binary (Top 10 or not) to multiclass (exact finishing position).
- Enhance the Streamlit app’s user interface and add more interactive visualizations.
- Perform hyperparameter tuning and cross-validation to optimize model performance.
- Investigate feature importance consistency across different models and seasons.
