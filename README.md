# 🍷 Strategic ML Framework for Wine Pricing Risk  
### Data Science Final Project – Ironhack

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

## 📌 Project Overview

The wine industry faces a **structural delay between decisions and consequences**.  
Pricing and positioning choices made today often impact brand perception and sales **two to three years later**, when corrective action is limited or nearly irreversible.

At the same time, **climate change is increasing vintage-to-vintage variability** in grape composition, making technical wine quality less predictable and amplifying strategic risk.

This project develops an **interpretable, business-oriented Machine Learning framework** to help wineries **anticipate perception and pricing risk before negative market effects materialize**.

Rather than focusing only on explaining past outcomes, the objective is to **support preventive decision-making** for future wine releases, enabling wineries to adjust pricing and positioning strategies while preserving long-term consumer trust.

---

## 🧠 Business Problem

Wineries must decide **how to price and position a wine today** for a product that will reach the market years later, often under uncertain quality conditions.

If a winery overprices a weaker vintage or maintains premium positioning when technical quality declines, the negative impact may not be immediate. Instead, **consumer trust erodes gradually**, and sales decline becomes visible only after several years.

**Core strategic question:**

> How can wineries detect early warning signals of misalignment between technical quality and market expectations, before long-term damage occurs?

---

## 📊 Data Description

This project is based on two independent and complementary datasets:

### 1️⃣ Wine Quality Dataset
- Physicochemical attributes of wines
- Represents **technical and analytical wine quality**
- Includes acidity, alcohol, pH, sugar, sulphates, and expert quality scores

### 2️⃣ Wine Reviews Dataset
- Professional and consumer wine reviews
- Represents **market perception**
- Includes price, rating points, country, variety, and textual descriptions

**Methodological note:**  
The datasets are **not joined at a row level**.  
They are analyzed separately and connected conceptually through **model outputs and scenario-based comparison**, reflecting real-world decision-making constraints.

---

## 🔍 Machine Learning & Analytical Approach

This project follows a **multi-layer decision-support architecture**:

### 🔹 Layer 1 – Technical Quality Model
- Supervised regression models predict expected technical wine quality from chemical composition
- Provides early signals of quality variation before market exposure

### 🔹 Layer 2 – Market Expectation Model
- Supervised regression models estimate expected market perception (ratings and/or price context)
- Captures how the market typically evaluates wines with similar characteristics

### 🔹 Layer 3 – Strategic Risk Segmentation
- An explicit risk indicator combines:
  - predicted technical quality
  - expected market perception
  - observed pricing signals
- Wines are segmented into:
  - **Low Risk**
  - **Medium Risk**
  - **High Risk**

The objective is **risk mitigation and strategic alignment**, not maximizing predictive accuracy alone.

---

## 📈 Key Deliverables

- End-to-end Machine Learning pipeline in Python
- Interpretable models with clear evaluation metrics
- Strategic risk segmentation and scenario analysis
- Visualizations supporting executive decision-making
- Fully documented and reproducible GitHub repository
- Final presentation slides

---

## 📁 Project Structure

- `data/` – Raw and processed datasets  
- `notebooks/` – EDA, modeling, and risk framework notebooks  
- `src/` – Reusable preprocessing, modeling, and risk logic modules  
- `figures/` – Exported visualizations  
- `slides/` – Final presentation  

---

## 🎓 Academic Context (Ironhack)

**Project type:**  
Data Science End-to-End Project (Case Study 1)

### ❓ Research Questions
- Which chemical attributes are most strongly associated with technical wine quality?
- How does market perception typically respond to different quality and pricing patterns?
- Where do misalignments between analytical quality and market perception appear?
- Which scenarios represent higher long-term perception and pricing risk?

### ⚠️ Main Dataset Challenges
- Missing values and outliers
- Subjectivity and bias in expert ratings
- Market selection bias in wine reviews
- Absence of direct long-term sales data

### 🛠️ Mitigation Strategies
- Robust data cleaning and preprocessing
- Conservative, interpretable modeling choices
- Explicit acknowledgment of assumptions and limitations
- Scenario-based reasoning instead of causal claims

---

## 👩‍💻 Author

**Marta**  
Ironhack – Data Analytics Bootcamp

---

## 🔄 README Update Log

- Project reframed as **Strategic Machine Learning** project  
- Business problem updated to include **delayed market impact**
- Methodology updated to **ML + risk segmentation architecture**
- Deliverables aligned with **Case Study 1 (Data Science)**

---

## Step 1 - Data Ingestion Status

- Wine Quality dataset (`WineQT.csv`) loaded as technical quality source
- Wine Reviews dataset (`winemag-data-130k-v2.csv`) loaded as market perception source
- Raw data stored in `data/raw/` and treated as immutable
- Initial sanity checks completed prior to cleaning

## Step 2 — Wine Quality EDA (Technical Quality)

- Confirmed target distribution and class concentration around mid-quality scores
- Checked missing values and duplicates
- Screened correlations between physicochemical features and quality to guide modeling
- Documented initial observations prior to any cleaning or feature engineering
  
## Step 3 — Wine Reviews Ingestion & Initial Exploration (Market Perception)

- Wine Reviews dataset loaded as market perception source
- Initial inspection of ratings (`points`), prices, and key categorical variables
- Missing values identified across price and regional fields
- Distribution ranges reviewed to assess modeling feasibility

## Step 4 — Technical Quality Modeling (Machine Learning)

- Framed technical quality prediction as a supervised regression problem
- Trained baseline Linear and Ridge regression models
- Evaluated performance using RMSE and R²
- Identified key chemical drivers of technical wine quality
- Established an interpretable technical benchmark for strategic comparison

## Step 5 — Market Expectation Modeling (Machine Learning)

- Framed market perception prediction as a supervised regression problem
- Developed two models to estimate expected ratings, with and without price
- Quantified the influence of price on perceived quality
- Established a market expectation benchmark for risk analysis

## Step 6 — Risk Score Framework

- Defined business risk as misalignment between technical quality and market expectations
- Built a continuous Risk Score (0–100) to quantify latent overvaluation risk
- Refined risk segmentation into four actionable categories
- Visualized risk distribution to support strategic decision-making
