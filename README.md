# 🍷 Wine Quality vs Market Perception
### Data Analytics Final Project – Ironhack

## 🛠️ Tools & Technologies

<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="Pandas" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="NumPy" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/matplotlib/matplotlib-original.svg" alt="Matplotlib" width="40" height="40"/>
  <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="80" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg" alt="SQL" width="40" height="40"/>
  <img src="https://cdn.worldvectorlogo.com/logos/tableau-software.svg" alt="Tableau" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="Git" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" alt="GitHub" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" alt="Jupyter Notebook" width="40" height="40"/>
</p>


---

## 📌 Project Overview

Because we are facing **accelerating climate change**, winemaking is becoming increasingly unpredictable. Variations in temperature, rainfall, and extreme weather events are already affecting grape composition and, consequently, **wine quality from one vintage to another**.

For winemakers, changing global climate policies or reversing climate change is **not an immediate or realistic solution**. The practical challenge is therefore to **adapt** to this variability by understanding how changes in technical wine quality translate into **consumer perception** in the market.

This project analyzes the relationship between **analytical wine quality** (based on chemical composition) and **market perception** (ratings, reviews, and price). The goal is to develop a **data-driven analytical framework** that helps wineries **adjust pricing and positioning strategies** when wine quality fluctuates across vintages.

Rather than focusing only on explaining past behavior, the project aims to **support strategic decision-making for future wine releases**, enabling wineries to align pricing with consumer expectations, **maintain trust**, and preserve long-term brand loyalty even in lower-quality years.

---

## 📊 Data Description

This analysis is based on two independent and complementary datasets:

- **Wine Quality Dataset**
  - Physicochemical attributes of wines
  - Used to evaluate *technical and analytical quality*
  - Includes variables such as acidity, alcohol, pH, sugar, sulphates, and expert quality scores

- **Wine Reviews Dataset**
  - Professional and consumer wine reviews
  - Used to assess *market perception*
  - Includes price, rating points, country, variety, and textual descriptions

**Important note:**  
The datasets are **not joined at a row level**. They are analyzed **separately and comparatively** to identify patterns, alignments, and mismatches between technical quality and market perception.

---

## 🔍 Methodology Overview

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Correlation and pattern analysis
- Comparative analysis between technical quality indicators and market outcomes
- Business-oriented interpretation of analytical results

---

## 📈 Key Deliverables

- Python notebooks documenting the full analytical workflow
- SQL scripts for structured data querying
- Tableau dashboard for visual storytelling
- Final presentation slides
- Fully documented and reproducible GitHub repository

---

## 📁 Project Structure

- `data/` – Raw and cleaned datasets  
- `notebooks/` – Python notebooks for exploration and analysis  
- `sql_scripts/` – SQL queries and database scripts  
- `figures/` – Exported visualizations  
- `slides/` – Final presentation  
- `src/` – Reusable functions and utilities  

---

## 👩‍💻 Author

**Marta**  
Ironhack – Data Analytics Bootcamp

---

## 🎓 Academic Project Requirements (Ironhack)

This section documents the academic components required for the Ironhack Data Analytics final project.

### ❓ Research Questions
- How strongly is technical wine quality associated with market perception indicators such as price and ratings?
- Which chemical attributes show the strongest relationship with expert quality scores?
- Are higher-quality wines consistently priced higher in the market?
- Where do mismatches between analytical quality and consumer perception appear?

### ⚠️ Main Dataset Issues
- Missing values in chemical and review variables
- Potential outliers in quality scores and prices
- Subjectivity in expert ratings
- Market and selection bias in wine reviews

### 🛠️ Solutions for Dataset Issues
- Data cleaning and filtering
- Outlier detection and treatment
- Robust descriptive statistics
- Clear documentation of assumptions and limitations

### 📈 Conclusions *(to be completed)*
This section will summarize the main analytical findings and their implications for pricing and positioning strategies.

### 🔮 Next Steps *(to be completed)*
- Deeper segmentation by country, variety, or wine type
- Additional statistical modeling
- Potential NLP analysis of wine descriptions
- Extension to additional vintages or external datasets

