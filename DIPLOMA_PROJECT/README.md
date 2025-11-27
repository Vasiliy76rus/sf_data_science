# 🔮 NGO Funding Predictor
> *Data Science Diploma Project by V.A. Kokorin*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![SkillFactory](https://img.shields.io/badge/SkillFactory-Data_Science-green?style=for-the-badge)](https://skillfactory.ru/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)]()

---

## 🧠 About The Project

**Can we predict which Non-Profit Organizations (NGOs) will receive state funding?**

This project analyzes the Russian NGO sector to identify key success factors for obtaining grants and government contracts. Using machine learning, we uncover patterns hidden in regional data, organization age, and activity types.

**Key Objectives:**
*   🕵️ **Detect** hidden dependencies in NGO funding.
*   🧪 **Test** statistical hypotheses (Region, Age, Activity).
*   🤖 **Build** a predictive ML model (ROC-AUC > 0.75).
*   💡 **Interpret** results for strategic decision-making.

---

## 🛠️ Tech Stack

The project is built with a focus on **efficiency** and **minimalism**.

| Category | Tools |
|----------|-------|
| **Core** | `Pandas` `NumPy` `Pathlib` |
| **Viz** | `Matplotlib` `Seaborn` |
| **Stats** | `SciPy` (Chi-square, Mann-Whitney) |
| **ML** | `Scikit-learn` `CatBoost` `Imbalanced-learn` |
| **XAI** | `SHAP` (Model Interpretability) |

---

## 📂 Project Structure

We follow a **"Maximum Minimalism"** philosophy. No clutter, just code.

```text
📦 DIPLOMA_PROJECT
 ┣ 📂 data
 ┃ ┗ 📂 raw                 # 💾 Split-archives (GitHub friendly <100MB)
 ┣ 📂 notebooks
 ┃ ┗ 📜 DIPLOMA_PROJECT...  # 📓 The Core: Analysis + Report + Code
 ┣ 📂 reports
 ┃ ┣ 📂 figures             # 📊 Generated Charts
 ┃ ┗ 🧠 best_model.pkl      # 🤖 Saved Model
 ┣ 📜 requirements.txt      # 📦 Dependencies
 ┗ 📜 README.md             # 📖 You are here
```

---

## 💡 Key Insights

<details>
<summary><b>Click to reveal findings</b></summary>

### 1. Geography Matters 🌍
Statistical tests confirmed that the **Region of Registration** significantly impacts funding probability. Some regions are "grant-magnets".

### 2. Experience Pays Off ⏳
Older organizations are more likely to receive funding. The "Survival of the fittest" rule applies here.

### 3. Digital Footprint 🌐
Organizations with a website and active social media presence have a drastically higher chance of success.

</details>

---

## 🚀 Getting Started

### 1. Clone & Install
```bash
git clone https://github.com/NeuroLoft/SF_DATA_SCIENCE.git
cd SF_DATA_SCIENCE/DIPLOMA_PROJECT
pip install -r requirements.txt
```

### 2. Data Setup
The data is already included! 🎁
We used a **split-zip strategy** to bypass GitHub limits. The notebook automatically stitches `ngo_dump_*.zip` files together.
*Just run the code, no manual download needed.*

### 3. Run Analysis
Open the main notebook:
```bash
jupyter notebook notebooks/DIPLOMA_PROJECT_KOKORIN_VA.ipynb
```

---

## 👨‍💻 Author

**Vladimir Kokorin**
*Data Scientist in training*

> *"Minimalism is not a lack of something, but a perfect amount of something."*

---
