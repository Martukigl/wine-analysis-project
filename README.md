# 🍷 Wine Quality Risk Calculator

**Data Science Final Project – Ironhack (Case Study 1)**

---

## 🛠️ Tools & Technologies

<p align="left"> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="Pandas" width="40" height="40"/> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="NumPy" width="40" height="40"/> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/matplotlib/matplotlib-original.svg" alt="Matplotlib" width="40" height="40"/> 
  <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="80" height="40"/> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg" alt="Scikit-learn" width="40" height="40"/> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="Git" width="40" height="40"/> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" alt="GitHub" width="40" height="40"/> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" alt="Jupyter Notebook" width="40" height="40"/> 
</p>

---

## Table of Contents

1. Project Overview  
2. Data Description  
3. Exploratory Data Analysis (Notebook 01)  
4. Baseline Risk Model (Notebook 02)  
5. Risk Framework & Evaluation Strategy (Notebook 03)  
6. Risk Modeling & Threshold Optimization (Notebook 04)  
7. Risk Calculator (Notebook 05)  
8. Conclusions & Limitations  

---

## 📌 Project Overview

Wine production involves long decision cycles: blending, bottling, pricing, and positioning decisions are often made months or years before a wine reaches the market.

When a wine with low technical quality is released under normal or premium positioning, the negative impact is rarely immediate. Instead, consumer trust erodes gradually, making corrective action costly and delayed.

This project develops an interpretable **Machine Learning risk classifier** that predicts whether a wine presents a **high risk of low technical quality**, based solely on its chemical composition.

The goal is not to explain quality after the fact, but to provide an **early warning tool** that supports preventive, conservative decision-making before market exposure.

---

## 🧠 Business Problem

Wineries must decide whether a wine is safe to release and position normally, or whether it requires additional caution (price adjustment, blending revision, or repositioning).

From a business perspective, errors are asymmetric:

- **False negatives** (high-risk wines classified as safe)  
  → Potential long-term brand damage and loss of consumer trust

- **False positives** (safe wines flagged as risky)  
  → Conservative decisions, but limited strategic downside

🎯 **Core business objective:**  
Minimize false negatives by detecting low-quality risk as early as possible, even at the cost of some false positives.

---

## 📊 Dataset Description

### Wine Quality Dataset
- Physicochemical attributes of wines  
- Represents technical and analytical wine quality  
- Features include acidity measures, alcohol content, pH, sugar, sulphates, and density  
- Target variable: expert quality score (integer scale)

### Risk Target Definition
risk = 1 if quality ≤ 5
risk = 0 if quality > 5

- High-risk rate ≈ **45.7%**
- Dataset is not severely imbalanced  
- Framing reflects a preventive quality control perspective

---

## 🔍 Exploratory Data Analysis (EDA)

EDA focused on understanding distributions and relationships between chemical attributes and quality.

### EDA Highlights
- Strong association between alcohol content and technical quality
- Volatile acidity consistently aligns with low-quality outcomes
- Some variables exhibit monotonic but non-linear relationships, motivating the use of both Pearson and Spearman correlation
- Exploratory patterns motivated a hypothesis-driven experiment evaluated later during modeling, without assuming any decision at the EDA stage

---

## 🤖 Modeling Approach

- Supervised binary classification  
- Interpretable baseline: **Logistic Regression**  
- Non-linear models evaluated for performance comparison  
- Standardized features where required  
- Class imbalance handled explicitly  
- **Primary metric:** Recall for the high-risk class  
- **Supporting metrics:** ROC-AUC and PR-AUC

---

## 📈 Baseline Risk Model (Notebook 02)
📈 Baseline Model Evaluation Summary

- **High Risk Recall:** ~0.75
- **High Risk Precision:** ~0.72
- **ROC-AUC:** ~0.82
- **PR-AUC:** ~0.78

Evaluation emphasizes recall for the high-risk class, in line with the asymmetric business cost of false negatives.

---

## 🧪 Modeling Experiments

### Alcohol-Based Filtering Experiment

- Hypothesis-driven experiment motivated by exploratory patterns
- Controlled experiment with identical pipeline and split  
- Filtering reduced recall for high-risk wines  
- Slight ROC-AUC decrease, no meaningful PR-AUC gain  

✅ **Decision:**  
Alcohol-based filtering rejected to avoid increasing false negatives.  
Final model uses the **full dataset**.

---
## Risk Framework & Evaluation Strategy

This project frames low technical wine quality as a **risk prevention problem**, not a pure prediction task.

A wine is labeled as **High Risk** when `quality ≤ 5`, and **Low Risk** otherwise.  
The model is designed as an **early warning system**, supporting conservative, preventive decisions before market release.

## 🧠 Risk Modeling & Threshold Optimization (Notebook 04)

Multiple classification models were evaluated in parallel under a unified, validation-driven decision framework.

---

### Model comparison

The following models were trained and compared using the same train/validation/test split:

- Logistic Regression (interpretable baseline)
- Random Forest
- Histogram Gradient Boosting

For each model:
- Training was performed on the training set
- The decision threshold was selected using the validation set to achieve a **minimum target recall** for high-risk wines
- Models were compared on validation using recall, precision, ROC-AUC, PR-AUC, and Brier score

---

### Threshold policy

- Thresholds were **not fixed at 0.5**
- The operating threshold was selected to ensure **high recall for the risk class**, prioritizing the reduction of false negatives
- Among eligible thresholds, the most conservative option meeting the recall target was chosen

---

### Final model selection

The **Histogram Gradient Boosting classifier** achieved the best precision–recall trade-off while meeting the same recall target as the baseline model.

As a result, it was selected as the **final model** for the project.

---

### Final evaluation on test set

The final model was evaluated once on a held-out test set using the frozen decision threshold:

- **Recall (risk = 1):** ~0.85  
- **Precision (risk = 1):** ~0.65  
- **ROC-AUC:** ~0.83  
- **PR-AUC:** ~0.81  

These results confirm that the model generalizes well and effectively prioritizes the detection of low-quality wines in line with the preventive business objective.

---

### Business cost asymmetry

- **False Negatives** (risky wines classified as safe) are considered more costly than **False Positives**.
- As a result, the primary objective is to **minimize missed risk cases**, even at the expense of allowing more false alarms.

---

### Evaluation strategy

- **Recall for the High-Risk class (risk = 1)** is the primary evaluation metric.
- Accuracy is not optimized, as it treats all errors equally and does not reflect the business objective.
- **ROC-AUC** and **PR-AUC** are used as supporting metrics to compare models independently of a specific decision threshold.

---

### Decision threshold

- The default probability threshold of 0.5 is treated as a convention, not a business rule.
- Threshold selection is considered part of the decision policy and is tuned in later stages to achieve a minimum target recall for high-risk wines.

This framework is defined **before model optimization** and governs all subsequent modeling, threshold tuning, and risk calculator design.

---

## ⚠️ Scope and Limitations

- Focus on interpretability and business actionability  
- While a non-linear model is used in the final stage, full interpretability is limited compared to linear models  
- No causal claims  
- Expert quality scores are subjective  
- External market outcomes are not modeled

---

## 📁 Repository Structure

notebooks/
├── 01_wine_quality_EDA.ipynb
├── 02_wine_quality_model.ipynb
├── 03_risk_framework.ipynb
├── 04_risk_modeling.ipynb
├── 05_risk_calculator.ipynb

models/
config.yaml
README.md


---

## 🎓 Academic Context

**Ironhack – Data Analytics Bootcamp**  
Case Study 1 – Machine Learning

---

## 👩‍💻 Author

**Marta**
