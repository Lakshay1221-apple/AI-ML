# BMW Global Sales Analysis & Predictive Modeling

> Exploratory Data Analysis and Machine Learning modeling of BMW global sales data (2018–2025) covering revenue trends, regional performance, model-level insights, EV adoption patterns, and sales prediction.

---

## Table of Contents

- [BMW Global Sales Analysis & Predictive Modeling](#bmw-global-sales-analysis--predictive-modeling)
  - [Overview](#overview)
  - [Dataset](#dataset)
    - [Columns](#columns)
  - [Project Structure](#project-structure)
  - [Pipeline Walkthrough](#pipeline-walkthrough)
    - [1. Data Loading & Inspection](#1-data-loading--inspection)
    - [2. Feature Engineering](#2-feature-engineering)
    - [3. Revenue Validation](#3-revenue-validation)
    - [4. Exploratory Data Analysis (EDA)](#4-exploratory-data-analysis-eda)
    - [5. Predictive Modeling](#5-predictive-modeling)
  - [Key Results & Findings](#key-results--findings)
    - [Overall Stats](#overall-stats)
    - [Regional Performance](#regional-performance)
    - [Model Performance](#model-performance)
    - [EV Adoption Trend](#ev-adoption-trend)
    - [Pricing Insights](#pricing-insights)
    - [Machine Learning Insights](#machine-learning-insights)
  - [Visualizations](#visualizations)
  - [Tech Stack](#tech-stack)

---

## Overview

This project performs a full exploratory data analysis (EDA) and implements an end-to-end Machine Learning pipeline on BMW's global sales dataset spanning **2018 to 2025**. The goal is to extract actionable insights on:

- How sales and revenue have evolved over time
- Which regions and models drive the most revenue
- The trajectory of BMW's electric vehicle (BEV) adoption
- Pricing patterns across regions and models
- Predicting sales volume using historical features via a Random Forest Regressor

---

## Dataset

| Property | Value |
|---|---|
| **File** | `bmw_sales.csv` |
| **Rows** | 3,072 |
| **Columns** | 11 |
| **Time Range** | January 2018 – December 2025 |
| **Granularity** | Monthly, per Region, per Model |

### Columns

| Column | Description |
|---|---|
| `Year` | Year of record |
| `Month` | Month of record |
| `Region` | Sales region (Europe, China, USA, RestOfWorld) |
| `Model` | BMW model (3 Series, 5 Series, X3, X5, X7, i4, iX, MINI) |
| `Units_Sold` | Number of vehicles sold |
| `Avg_Price_EUR` | Average selling price in EUR |
| `Revenue_EUR` | Total revenue in EUR |
| `BEV_Share` | Battery Electric Vehicle share (%) |
| `Premium_Share` | Premium segment share (%) |
| `GDP_Growth` | Regional GDP growth rate |
| `Fuel_Price_Index` | Regional fuel price index |

---

## Project Structure

```
BMW/
├── bmw.ipynb            # Main analysis & modeling notebook
├── bmw_sales.csv        # Raw dataset
└── README.md            # This file
```

---

## Pipeline Walkthrough

### 1. Data Loading & Inspection

The dataset is loaded into a Pandas DataFrame. We ensure that there are no null values and the numerical/categorical columns are in shape for deeper analysis. The data covers 4 regions, 8 models, and 96 months.

### 2. Feature Engineering

A unified `Date` column was created from the `Year` and `Month` features to enable proper time-series grouping and plotting operations.

### 3. Revenue Validation

We algorithmically verified that `Revenue_EUR = Units_Sold × Avg_Price_EUR` holds exactly for every record — confirming data integrity before performing downstream tasks.

### 4. Exploratory Data Analysis (EDA)

The EDA covers multiple dimensions including total units vs time, average EV adoption over the years, the impact of fuel price indices, and heatmaps correlating model profitability per region to uncover market potential.

### 5. Predictive Modeling

A **Random Forest Regressor** is implemented to predict `Units_Sold`.
- Categorical features (`Region`, `Model`) are transformed using `LabelEncoder`.
- Features are scaled utilizing standard normalization (`StandardScaler`).
- The model evaluates feature importance, residual errors, Mean Absolute Error (MAE), and R-squared scores.
- A discrete categorization function transforms regression output into 'Low', 'Medium', and 'High' prediction tiers, evaluated via standard `classification_report` metrics.

---

## Key Results & Findings

### Overall Stats

| Metric | Value |
|---|---|
| **Total Revenue** | €1.571 Trillion |
| **Total Units Sold** | 24,515,445 |
| **Avg Units / Month** | ~7,980 |
| **Avg Price / Vehicle** | €63,855 |

---

### Regional Performance

**Revenue (EUR) — All Regions are near-equal, with China leading:**

| Region | Revenue (EUR) | Units Sold |
|---|---|---|
| 🥇 **China** | €401.76B | 6,256,750 |
| 🥈 **RestOfWorld** | €391.07B | 6,113,872 |
| 🥉 **USA** | €389.31B | 6,099,647 |
| **Europe** | €388.88B | 6,045,176 |

> **Insight:** Revenue is remarkably balanced across all four regions (~25% each), indicating BMW's highly globalised sales strategy. China holds a marginal lead in both revenue and volume.

---

### Model Performance

**Top 3 Revenue Drivers:**

| Rank | Model | Total Revenue (EUR) |
|---|---|---|
| 1 | **X7** | €286.4B |
| 2 | **iX** | €235.1B |
| 3 | **X5** | €212.8B |

> **Insight:** The **X7 SUV is the top revenue driver**. Notably, **two EV models (iX and i4) rank highly**, signalling BMW's successful EV transition at the premium end.

---

### EV Adoption Trend

> **Insight:** BEV share has grown **~9.5× from 2018 to 2025**, nearly doubling every 2–3 years. The dual-line overlay against the Fuel Price Index confirms a strong **positive correlation between rising fuel prices and accelerating EV adoption**.

---

### Machine Learning Insights

Using feature permutations on the Random Forest model:
- The core features driving changes in vehicle sales include **Model**, **Region**, and macroeconomic indicators like **GDP Growth** and **Premium Share**.
- The Regressor is effectively diagnosing relationships capturing non-linear interactions across time and geographical inputs. Residuals show homoscedastic properties outlining prediction stabilities.

---

## Visualizations

The notebook embeds 10+ professional visualizations:
- Time-Series Multi-line over regional growths
- Correlation matrices and Pair-wise scatter overlays
- Aggregated Heatmaps summarizing Revenue across models and territories
- Residual diagnostic charts for regression fit analysis

---

## Tech Stack

| Library | Purpose |
|---|---|
| `pandas` / `numpy` | Data manipulation, loading, transformations |
| `matplotlib` / `seaborn` | Advanced data visualization |
| `scikit-learn` | Regression, Preprocessing, Feature Selection, Metrics |

---

*Analysis & Modeling conducted as part of the AI-ML project portfolio.*
