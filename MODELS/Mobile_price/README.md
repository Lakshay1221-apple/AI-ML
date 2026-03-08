# Mobile Price Range Prediction — ML Pipeline Documentation

**Author:** Lakshay  
**Date:** March 2026  
**Notebook:** `mobile.ipynb`  
**Datasets:** `mobile_train.csv`, `mobile_test.csv`  
**Task Type:** Multi-class Classification  

---

## Dataset

This project uses the Kaggle dataset:

**Mobile Price Classification**

Download it from:
[https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)

Place the following files inside the `MODELS/Mobile_price/` folder:

```
mobile_train.csv
mobile_test.csv
```

---

## Table of Contents

- [Mobile Price Range Prediction — ML Pipeline Documentation](#mobile-price-range-prediction--ml-pipeline-documentation)
  - [Dataset](#dataset)
  - [Table of Contents](#table-of-contents)
  - [1. Project Overview](#1-project-overview)
  - [2. Dataset Description](#2-dataset-description)
    - [Training Dataset (`mobile_train.csv`)](#training-dataset-mobile_traincsv)
    - [Test Dataset (`mobile_test.csv`)](#test-dataset-mobile_testcsv)
    - [Original Columns](#original-columns)
  - [3. Libraries Used](#3-libraries-used)
  - [4. Pipeline Stages](#4-pipeline-stages)
    - [Stage 1 — Data Loading](#stage-1--data-loading)
    - [Stage 2 — Exploratory Data Analysis (EDA)](#stage-2--exploratory-data-analysis-eda)
    - [Stage 3 — Data Quality Checks](#stage-3--data-quality-checks)
    - [Stage 4 — Outlier Detection \& Removal](#stage-4--outlier-detection--removal)
    - [Stage 5 — Feature Engineering](#stage-5--feature-engineering)
      - [5.1 — Screen Resolution](#51--screen-resolution)
      - [5.2 — Screen Size](#52--screen-size)
      - [5.3 — Connectivity Score](#53--connectivity-score)
      - [5.4 — Total Camera Megapixels](#54--total-camera-megapixels)
      - [5.5 — CPU Power](#55--cpu-power)
      - [5.6 — Weight per Screen Depth](#56--weight-per-screen-depth)
      - [Feature Engineering Summary](#feature-engineering-summary)
    - [Stage 6 — Feature-Target Split](#stage-6--feature-target-split)
    - [Stage 7 — Train-Test Split](#stage-7--train-test-split)
    - [Stage 8 — Feature Scaling](#stage-8--feature-scaling)
    - [Stage 9 — Model Training](#stage-9--model-training)
    - [Stage 10 — Model Evaluation](#stage-10--model-evaluation)
      - [Predictions](#predictions)
      - [Accuracy Score](#accuracy-score)
      - [Confusion Matrix](#confusion-matrix)
      - [Classification Report](#classification-report)
    - [Stage 11 — Inference on Unseen Test Data](#stage-11--inference-on-unseen-test-data)
  - [5. Results Summary](#5-results-summary)
  - [6. Feature Summary Table](#6-feature-summary-table)

---

## 1. Project Overview

This pipeline predicts the **price range** of a mobile phone based on its hardware and connectivity specifications. The price range is a categorical label with four classes:

| Class | Meaning       |
|-------|---------------|
| 0     | Low cost      |
| 1     | Medium cost   |
| 2     | High cost     |
| 3     | Very high cost|

The pipeline covers the full ML workflow: data loading, EDA, data cleaning, feature engineering, scaling, model training, validation evaluation, and inference on a separate unlabelled test set.

---

## 2. Dataset Description

### Training Dataset (`mobile_train.csv`)

| Property          | Value              |
|-------------------|--------------------|
| File              | `mobile_train.csv` |
| Total Records     | 2,000 rows         |
| Original Features | 21 columns         |
| Target Column     | `price_range`      |
| Class Balance     | Perfectly balanced — 500 samples per class |

### Test Dataset (`mobile_test.csv`)

| Property          | Value              |
|-------------------|--------------------|
| File              | `mobile_test.csv`  |
| Purpose           | Unlabelled inference — no `price_range` column |
| Extra Column      | `id` — row identifier, dropped before processing |
| Features          | Same 20 raw feature columns as training data |

### Original Columns

| Feature         | Description                            | Type    |
|-----------------|----------------------------------------|---------|
| `battery_power` | Total energy a battery can store (mAh) | Numeric |
| `blue`          | Bluetooth support (0/1)                | Binary  |
| `clock_speed`   | CPU clock speed (GHz)                  | Numeric |
| `dual_sim`      | Dual SIM support (0/1)                 | Binary  |
| `fc`            | Front camera megapixels                | Numeric |
| `four_g`        | 4G support (0/1)                       | Binary  |
| `int_memory`    | Internal memory (GB)                   | Numeric |
| `m_dep`         | Mobile depth (cm)                      | Numeric |
| `mobile_wt`     | Weight of the mobile (g)               | Numeric |
| `n_cores`       | Number of processor cores              | Numeric |
| `pc`            | Primary camera megapixels              | Numeric |
| `px_height`     | Pixel resolution height                | Numeric |
| `px_width`      | Pixel resolution width                 | Numeric |
| `ram`           | RAM (MB)                               | Numeric |
| `sc_h`          | Screen height (cm)                     | Numeric |
| `sc_w`          | Screen width (cm)                      | Numeric |
| `talk_time`     | Longest time a battery charge lasts    | Numeric |
| `three_g`       | 3G support (0/1)                       | Binary  |
| `touch_screen`  | Touch screen support (0/1)             | Binary  |
| `wifi`          | Wi-Fi support (0/1)                    | Binary  |
| `price_range`   | **Target** — Price category (0–3)      | Target  |

---

## 3. Libraries Used

```python
import pandas as pd               # Data manipulation
import numpy as np                # Numerical operations
import matplotlib.pyplot as plt   # Visualizations
import seaborn as sns             # Statistical visualizations

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```

---

## 4. Pipeline Stages

---

### Stage 1 — Data Loading

```python
df = pd.read_csv('mobile_train.csv')
```

- Loads the dataset into a Pandas DataFrame.
- Resulting shape: **(2000, 21)**.

---

### Stage 2 — Exploratory Data Analysis (EDA)

The following exploratory steps were performed to understand the data:

| Step                         | Code                                           | Purpose                                      |
|------------------------------|------------------------------------------------|----------------------------------------------|
| Preview top rows             | `df.head()`                                    | Inspect first 5 rows                         |
| Preview bottom rows          | `df.tail()`                                    | Inspect last 5 rows                          |
| Statistical summary          | `df.describe()`                                | Mean, std, min, max for all numeric features  |
| Data types & memory          | `df.info()`                                    | Column dtypes and null counts overview        |
| Column list                  | `df.columns`                                   | List all feature names                       |
| Target distribution          | `df["price_range"].value_counts()`             | Confirm class balance (500 per class)        |
| Feature-target correlation   | `df.corr()["price_range"].sort_values()`       | Rank features by linear correlation with target |
| Full correlation matrix      | `df.corr()`                                    | Pairwise feature correlations                |
| Correlation heatmap          | `sns.heatmap(corr_matrix, annot=True, ...)`    | Visual representation of feature relationships |

**Key Insight from EDA:**  
`ram` was identified as the feature with the highest positive correlation to `price_range`, making it the most predictive individual feature.

---

### Stage 3 — Data Quality Checks

```python
df.isnull().sum()       # Check for missing values
df.duplicated().sum()   # Check for duplicate rows
```

| Check           | Result                    |
|-----------------|---------------------------|
| Missing values  | 0 — No nulls found        |
| Duplicate rows  | 0 — No duplicates found   |

The dataset is clean with no missing values or duplicate entries.

---

### Stage 4 — Outlier Detection & Removal

**Visualization:**
```python
plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.show()
```
A boxplot was generated for all features to visually identify outliers.

**Removal using the IQR Method:**
```python
Q1  = df.quantile(0.25)
Q3  = df.quantile(0.75)
IQR = Q3 - Q1

df_clean = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
```

- Any row where **any feature** fell outside the range `[Q1 − 1.5×IQR, Q3 + 1.5×IQR]` was removed.
- The cleaned dataset `df_clean` was stored separately for reference; the main `df` continued through the pipeline.

---

### Stage 5 — Feature Engineering

Six new composite features were engineered from the original columns to capture richer information, reduce dimensionality, and improve model interpretability. After each feature was created, the original raw columns were dropped.

---

#### 5.1 — Screen Resolution

```python
df["resolution"] = df["px_height"] * df["px_width"]
df = df.drop(["px_height", "px_width"], axis=1)
```

| Original Columns | New Feature  | Formula                        |
|------------------|--------------|--------------------------------|
| `px_height`, `px_width` | `resolution` | `px_height × px_width` |

Captures total pixel count as a single measure of display quality.

---

#### 5.2 — Screen Size

```python
df["screen_size"] = df["sc_h"] * df["sc_w"]
df = df.drop(["sc_h", "sc_w"], axis=1)
```

| Original Columns | New Feature   | Formula            |
|------------------|---------------|--------------------|
| `sc_h`, `sc_w`   | `screen_size` | `sc_h × sc_w`      |

Approximates the physical display area of the phone.

---

#### 5.3 — Connectivity Score

```python
df["connectivity_score"] = df["blue"] + df["wifi"] + df["three_g"] + df["four_g"] + df["dual_sim"]
df = df.drop(["blue", "wifi", "three_g", "four_g", "dual_sim"], axis=1)
```

| Original Columns                            | New Feature           | Formula                                |
|---------------------------------------------|-----------------------|----------------------------------------|
| `blue`, `wifi`, `three_g`, `four_g`, `dual_sim` | `connectivity_score` | Sum of all 5 binary connectivity flags |

Aggregates all connectivity capabilities into a single score (range: 0–5).

---

#### 5.4 — Total Camera Megapixels

```python
df["camera_total_mp"] = df["fc"] + df["pc"]
df = df.drop(["fc", "pc"], axis=1)
```

| Original Columns | New Feature       | Formula       |
|------------------|-------------------|---------------|
| `fc`, `pc`       | `camera_total_mp` | `fc + pc`     |

Combines front and primary camera megapixels into a single total camera quality metric.

---

#### 5.5 — CPU Power

```python
df["cpu_power"] = df["n_cores"] * df["clock_speed"]
df = df.drop(["n_cores", "clock_speed"], axis=1)
```

| Original Columns          | New Feature | Formula                     |
|---------------------------|-------------|-----------------------------|
| `n_cores`, `clock_speed`  | `cpu_power` | `n_cores × clock_speed`     |

Approximates the overall processing power of the chip.

---

#### 5.6 — Weight per Screen Depth

```python
df["weight_per_screen"] = df["mobile_wt"] / df["m_dep"]
df = df.drop(["mobile_wt", "m_dep"], axis=1)
```

| Original Columns        | New Feature        | Formula                  |
|-------------------------|--------------------|--------------------------|
| `mobile_wt`, `m_dep`    | `weight_per_screen`| `mobile_wt / m_dep`      |

Captures a combined physical form-factor metric relating weight to device depth.

---

#### Feature Engineering Summary

| Engineered Feature   | Derived From                              | Operation    | Originals Dropped |
|----------------------|-------------------------------------------|--------------|-------------------|
| `resolution`         | `px_height`, `px_width`                   | Multiply     | Yes               |
| `screen_size`        | `sc_h`, `sc_w`                            | Multiply     | Yes               |
| `connectivity_score` | `blue`, `wifi`, `three_g`, `four_g`, `dual_sim` | Sum    | Yes               |
| `camera_total_mp`    | `fc`, `pc`                                | Sum          | Yes               |
| `cpu_power`          | `n_cores`, `clock_speed`                  | Multiply     | Yes               |
| `weight_per_screen`  | `mobile_wt`, `m_dep`                      | Divide       | Yes               |

**Result:** Dataset reduced from **21 columns → 12 columns** (11 features + 1 target).

**Final feature set:**  
`battery_power`, `int_memory`, `ram`, `talk_time`, `touch_screen`, `resolution`, `screen_size`, `connectivity_score`, `camera_total_mp`, `cpu_power`, `weight_per_screen`

---

### Stage 6 — Feature-Target Split

```python
X = df.drop("price_range", axis=1)   # Feature matrix — shape: (2000, 11)
y = df["price_range"]                 # Target vector  — shape: (2000,)
```

---

### Stage 7 — Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

| Split     | Size | Rows  |
|-----------|------|-------|
| Training  | 80%  | 1,600 |
| Testing   | 20%  | 400   |

- `random_state=42` ensures reproducibility.

---

### Stage 8 — Feature Scaling

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # Fit on train, transform train
X_test_scaled  = scaler.transform(X_test)         # Transform test only (no fit)
```

- **StandardScaler** standardizes each feature to zero mean and unit variance:  
  $z = \dfrac{x - \mu}{\sigma}$
- The scaler was **fit only on the training set** to prevent data leakage from the test set.
- Post-scaling distributions were verified with a histogram grid of all scaled features.

---

### Stage 9 — Model Training

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train_scaled, y_train)
```

| Parameter         | Value                    |
|-------------------|--------------------------|
| Algorithm         | Logistic Regression      |
| Solver            | `lbfgs` (default)        |
| Multi-class       | `auto` (OvR / multinomial) |
| Regularization    | L2 (default, `C=1.0`)    |
| Training set size | 1,600 samples            |

---

### Stage 10 — Model Evaluation

#### Predictions

```python
y_pred = model.predict(X_test_scaled)
```

---

#### Accuracy Score

```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

```
Accuracy: 0.935
```

**The model achieved 93.5% accuracy on the test set.**

---

#### Confusion Matrix

```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
```

```
         Predicted
         0    1    2    3
Actual 0 [102   3   0   0]
       1 [  3  85   3   0]
       2 [  0   6  81   5]
       3 [  0   0   6 106]
```

Visualized using a `sns.heatmap` with `fmt='d'` and `cmap='Blues'`.

---

#### Classification Report

```
              precision    recall  f1-score   support

           0       0.97      0.97      0.97       105
           1       0.90      0.93      0.92        91
           2       0.90      0.88      0.89        92
           3       0.95      0.95      0.95       112

    accuracy                           0.94       400
   macro avg       0.93      0.93      0.93       400
weighted avg       0.94      0.94      0.93       400
```

Visualized using a `sns.heatmap` on the `df_report` DataFrame for a color-coded per-class view.

> **Note:** All evaluation metrics above (accuracy, confusion matrix, classification report) are computed against `y_test` — the 20% validation split held out from `mobile_train.csv`. They do **not** use `mobile_test.csv`, which has no ground-truth labels.

---

### Stage 11 — Inference on Unseen Test Data

The trained model is applied to `mobile_test.csv`, which contains no labels. The same preprocessing pipeline used during training is replicated exactly.

```python
# Reload raw test data (safe for re-runs)
test_df = pd.read_csv("mobile_test.csv")

# Drop id column — not a training feature
if "id" in test_df.columns:
    test_df = test_df.drop("id", axis=1)

# Replicate all feature engineering steps
test_df["resolution"]         = test_df["px_height"] * test_df["px_width"]
test_df["screen_size"]        = test_df["sc_h"] * test_df["sc_w"]
test_df["connectivity_score"] = test_df["blue"] + test_df["wifi"] + test_df["three_g"] + test_df["four_g"] + test_df["dual_sim"]
test_df["camera_total_mp"]    = test_df["fc"] + test_df["pc"]
test_df["cpu_power"]          = test_df["n_cores"] * test_df["clock_speed"]
test_df["weight_per_screen"]  = test_df["mobile_wt"] / test_df["m_dep"]
# Drop all original raw columns
...

# Scale using the already-fitted scaler (no re-fit)
test_scaled = scaler.transform(test_df)

# Predict
predictions = model.predict(test_scaled)
```

**Key design decisions:**

| Decision | Reason |
|---|---|
| Reload CSV at top of cell | Prevents `KeyError` on re-runs caused by columns already being dropped |
| Drop `id` conditionally (`if "id" in ...`) | Safe guard — works even if CSV format changes |
| `scaler.transform()` only — no `fit_transform()` | Prevents data leakage; scaling parameters come from training data only |
| Identical feature engineering order | Ensures column names and order match exactly what the scaler was fitted on |

**Output:** A `predictions` array of shape `(n_samples,)` with predicted price range classes (0–3) for each row in `mobile_test.csv`.

> A classification report cannot be generated for these predictions as `mobile_test.csv` contains no true labels.

---

## 5. Results Summary

| Metric            | Value  |
|-------------------|--------|
| Test Accuracy     | 93.5%  |
| Macro Avg F1      | 0.93   |
| Weighted Avg F1   | 0.93   |
| Best Class (F1)   | Class 0 — 0.97 |
| Weakest Class (F1)| Class 2 — 0.89 |

The model performs strongly and uniformly across all four price range categories. Class 2 (High cost) shows slightly lower precision and recall, suggesting it is the most difficult category to separate — likely due to feature overlap with Class 1 and Class 3.

---

## 6. Feature Summary Table

| Feature              | Origin                                   | Type        | Kept in Final Model |
|----------------------|------------------------------------------|-------------|---------------------|
| `battery_power`      | Original                                 | Numeric     | Yes                 |
| `int_memory`         | Original                                 | Numeric     | Yes                 |
| `ram`                | Original (highest corr. with target)     | Numeric     | Yes                 |
| `talk_time`          | Original                                 | Numeric     | Yes                 |
| `touch_screen`       | Original                                 | Binary      | Yes                 |
| `resolution`         | Engineered from `px_height × px_width`   | Numeric     | Yes                 |
| `screen_size`        | Engineered from `sc_h × sc_w`            | Numeric     | Yes                 |
| `connectivity_score` | Engineered from 5 binary flags           | Numeric     | Yes                 |
| `camera_total_mp`    | Engineered from `fc + pc`                | Numeric     | Yes                 |
| `cpu_power`          | Engineered from `n_cores × clock_speed`  | Numeric     | Yes                 |
| `weight_per_screen`  | Engineered from `mobile_wt / m_dep`      | Numeric     | Yes                 |
| `price_range`        | Target variable                          | Categorical | Target              |

---

*End of Documentation*
****