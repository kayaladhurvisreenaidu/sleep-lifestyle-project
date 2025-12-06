📊 Sleep & Lifestyle Analysis Project
    A data analysis project exploring how lifestyle factors such as physical activity, BMI, stress levels, and daily steps influence sleep duration and sleep quality.

📁 Project Structure
sleep_lifestyle_project/
│
├── README.md
├── explore_data.py
├── reports/
│   └── h1_report
    ├── h2_report
    ├── h3_report
    └──h4_report
├── notebooks/
│   ├── H1_PhysicalActivity_vs_SleepQuality.ipynb
│   ├── H2_BMI_vs_SleepDuration.ipynb
│   ├── H3_Correlation_Between_DailySteps_and_SleepDuration.ipynb
│   └── H4_sleep_vs_stress_relation.ipynb
├── data/
│   └── Sleep_Health_and_Lifestyle_Dataset.csv
├── images/
│   └── (plots and visualizations)

📥 Dataset Information
    Dataset Name: Sleep Health and Lifestyle Dataset
    Source: Kaggle
    Kaggle Link: https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset
    Dataset Author: UoM190346A (as per Kaggle dataset page)
    License: Refer to the dataset license terms on Kaggle.

🔍 Project Description

  This project investigates how different lifestyle factors impact sleep health.
  Using statistical tests and data visualizations, we explore relationships between:
  Physical activity & sleep quality
  Body Mass Index (BMI) & sleep duration
  Daily steps & sleep duration
  Stress levels & sleep duration

🧪 Hypotheses Analyzed (H1–H4)
  H1: Physical activity affects sleep quality
  Test used: Independent t-test
  Notebook: H1_PhysicalActivity_vs_SleepQuality.ipynb
  
  H2: BMI category has an effect on sleep duration
  Test used: ANOVA → Kruskal-Wallis (due to non-normality)
  Notebook: H2_BMI_vs_SleepDuration.ipynb
  
  H3: Daily steps are correlated with sleep duration
  Test used: Pearson / Spearman correlation
  Notebook:
  H3_Correlation_Between_DailySteps_and_SleepDuration.ipynb
  
  H4: Stress level impacts sleep duration
  Test used: Mann-Whitney U test
  Notebook: H4_sleep_vs_stress_relation.ipynb

📁 Exploratory Data Analysis

  The explore_data.py script and notebook visualizations include:
  Missing value analysis
  Data cleaning
  Distribution plots
  These help understand the dataset before formal hypothesis testing.

📄 Academic Report

A full academic-style report summarizing:
✔ Data preparation
✔ Hypothesis testing methodology
✔ Statistical results
✔ Interpretation & conclusion

🛠 Tools & Libraries Used
  Python
  Pandas
  NumPy
  SciPy
  Matplotlib
  Seaborn

Jupyter Notebook
