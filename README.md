# 🍷 Wine Quality Risk Calculator  
**Data Science Final Project — Ironhack (Case Study 1)**

---

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0C4B5A?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

---

## Table of Contents

1. Project Overview  
2. Business Problem 
3. Dataset & Risk Definition  
4. Exploratory Data Analysis  
5. Modeling Strategy & Decision Framework  
6. Final Model Comparison (Validation)  
7. Final Model Selection  
8. Streamlit Demo App  
9. Limitations & Next Steps  
10. Repository Structure  

---

## 📌 Project Overview

Wine production involves long decision cycles: blending, bottling, pricing, and positioning decisions are made months (or years) before a wine reaches the market.

If a wine with low technical quality is released under normal or premium positioning, the negative impact is rarely immediate. Consumer trust erodes gradually, and corrective action becomes costly and delayed.

This project builds a **preventive Machine Learning risk system** that flags wines with **low technical quality risk** using **chemical composition only**.  
The goal is not to explain quality after the fact, but to provide an **early warning tool** for conservative, preventive decisions before market exposure.

---

## 🧠 Business Problem (Cost Asymmetry)

Wineries must decide whether a wine is safe to release and position normally, or whether it requires caution (price adjustment, blending revision, or repositioning).

From a business perspective, errors are asymmetric:

- **False Negatives (FN)**: risky wines classified as safe  
  → highest cost: potential long-term brand damage and trust loss
- **False Positives (FP)**: safe wines flagged as risky  
  → conservative cost: additional checks / operational friction

**Core business objective:** minimize FNs by detecting risk early, even at the cost of extra FPs.

This implies a **recall-first decision framework**, where the threshold is treated as a **business policy** (not fixed at 0.5).

---

## 📊 Dataset & Risk Definition

### Dataset

- Physicochemical attributes of wines (chemical composition)
- Features include acidity measures, alcohol content, pH, sugar, sulphates, density
- Target variable: expert quality score (integer scale)

### Risk target

- `risk = 1` if `quality ≤ 5`
- `risk = 0` otherwise

This framing reflects a **preventive quality control perspective**.

---

## 🔍 Exploratory Data Analysis (Notebook 01)

EDA focused on data integrity and feature–target relationships:

- Clean dataset schema (no engineered columns leaked)
- Min / max + percentile sanity checks
- Mutual Information analysis (ML-oriented feature dependency)
- Risk defined explicitly from `quality`
- No feature elimination

---

## 🤖 Modeling Strategy & Decision Framework

### Models compared (same validation split)

- Logistic Regression (balanced)
- Random Forest (balanced)
- Histogram Gradient Boosting (HistGB)
- KNN (scaled) as experimental baseline (not final candidate)

### Threshold tuning policy (recall-first)

- The decision threshold is **not** fixed at 0.5
- Threshold is tuned on the **validation set only** to enforce a recall target for `risk = 1`
- Threshold is **frozen** before test and deployment

This ensures comparisons are fair and prevents leakage.

---

## 📈 Final Model Comparison (Validation)

Validation performance after recall-oriented threshold tuning:

| Model              | FN | FP | Recall (risk=1) | Precision | Accuracy |
|--------------------|----|----|-----------------|-----------|----------|
| **HistGB (final)** | **0** | **20** | **0.90** | **0.67** | **0.91** |
| Random Forest      | 10 | 50 | 0.90 | 0.65 | 0.74 |
| Logistic Regression| 10 | 63 | 0.90 | 0.60 | 0.68 |
| KNN (scaled)       | 25 | 33 | 0.76 | 0.71 | 0.75 |

### Why recall values tie

A recall tie is expected: recall was **intentionally equalized** through threshold tuning to meet the same recall target.  
Model selection is therefore based on **error composition** (especially FN) and **precision–recall trade-off**, not recall alone.

---

## 🏆 Final Model Selection

- **Winner:** Histogram Gradient Boosting (HistGB)
- **Frozen threshold:** `0.288` (validation-tuned, then frozen)

**Reason:**

- Meets recall target
- **Zero false negatives** in validation
- Best precision–recall balance among tied models
- Minimizes total misclassification errors

---

## ⭐ Key Visual for Slides (Model Selection)

The key model selection graphic is:

- `figures/model_results_simple_validation.png`

What it shows:

- 🟢 Correct predictions (TP + TN)
- 🔴 Errors (FP + FN)

HistGB clearly minimizes errors and supports the final choice.

---

## 💻 Streamlit Demo App

Run locally:

- `streamlit run app/app.py`

App behavior:

- Loads final HistGB model + frozen threshold
- Inputs chemical composition features
- Outputs:
  - Risk probability
  - High / Low Risk classification
  - Business-friendly interpretation

Designed for **live demo** in the presentation.

---

## ⚠️ Limitations & Next Steps

Limitations:

- Dataset size limits generalization
- No external validation on unseen wineries
- Expert quality scores are subjective (no causal claims)

Next steps:

- External data validation
- Model monitoring after deployment
- Cost-sensitive threshold policy aligned to real operational cost

---

## 📁 Repository Structure

- `notebooks/`
  - `01_wine_quality_EDA.ipynb` (final)
  - `02_wine_quality_model.ipynb` (baseline)
  - `03_risk_framework.ipynb` (decision framework)
  - `04_model_comparison.ipynb` (final selection)
  - `05_risk_calculator.ipynb` (inference-only)

- `figures/`
  - `model_results_simple_validation.png` (key slide graph)
  - `model_comparison_recall_validation.png`
  - `model_errors_stacked_validation.png` (optional)

- `models/`
  - `histgb_risk_model.joblib`
  - `risk_thresholds.joblib`

- `app/`
  - `app.py`

---

## 🎓 Academic Context

**Ironhack — Data Analytics Bootcamp**  
Case Study 1 — Machine Learning

---

## 👩‍💻 Author

**Marta García Luceño**
