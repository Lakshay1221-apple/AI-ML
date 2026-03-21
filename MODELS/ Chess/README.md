# Chess Game Outcome Prediction

A machine learning project that predicts the winner of chess games (white or black) using game metadata from Lichess. Two classification models — **Logistic Regression** and **Random Forest** — are trained, evaluated, and compared.

---

## Table of Contents

- [Chess Game Outcome Prediction](#chess-game-outcome-prediction)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Dataset](#dataset)
    - [Original Features](#original-features)
  - [Project Structure](#project-structure)
  - [Installation \& Setup](#installation--setup)
    - [Prerequisites](#prerequisites)
    - [Install Dependencies](#install-dependencies)
    - [Run the Notebook](#run-the-notebook)
  - [Workflow \& Methodology](#workflow--methodology)
    - [1. Data Loading \& Exploration](#1-data-loading--exploration)
    - [2. Data Cleaning \& Preprocessing](#2-data-cleaning--preprocessing)
    - [3. Feature Engineering](#3-feature-engineering)
    - [Final Feature Set (Model 1 — Logistic Regression)](#final-feature-set-model-1--logistic-regression)
    - [Reduced Feature Set (Model 2 — Random Forest)](#reduced-feature-set-model-2--random-forest)
    - [4. Train-Test Split](#4-train-test-split)
    - [5. Feature Scaling](#5-feature-scaling)
    - [6. Model Training \& Evaluation](#6-model-training--evaluation)
      - [Model 1: Logistic Regression](#model-1-logistic-regression)
      - [Model 2: Logistic Regression (Reduced Features)](#model-2-logistic-regression-reduced-features)
      - [Model 3: Random Forest Classifier](#model-3-random-forest-classifier)
    - [7. Feature Importance Analysis](#7-feature-importance-analysis)
      - [Logistic Regression](#logistic-regression)
      - [Random Forest](#random-forest)
    - [8. Model Comparison](#8-model-comparison)
  - [Results](#results)
    - [Classification Metrics (Logistic Regression)](#classification-metrics-logistic-regression)
    - [Classification Metrics (Random Forest)](#classification-metrics-random-forest)
    - [Feature Importance Highlights](#feature-importance-highlights)
  - [Visualizations](#visualizations)
  - [Key Findings](#key-findings)
  - [Technologies Used](#technologies-used)
  - [Future Improvements](#future-improvements)
  - [License](#license)

---

## Project Overview

The goal of this project is to predict whether **white** or **black** wins a chess game based on structured game-level features such as player ratings, number of turns, time control, opening family, and an engineered rating difference feature. Draw outcomes are excluded to frame the task as a **binary classification** problem.

---

## Dataset

| Property         | Detail                                      |
| ---------------- | ------------------------------------------- |
| **Source**        | Lichess (via Kaggle `games.csv`)            |
| **Records**       | ~20,058 games                               |
| **Original Columns** | 16                                      |
| **File**          | `games.csv`                                 |

### Original Features

| Column            | Description                                |
| ----------------- | ------------------------------------------ |
| `id`              | Unique game identifier                     |
| `rated`           | Whether the game was rated (True / False)  |
| `created_at`      | Timestamp of game creation                 |
| `last_move_at`    | Timestamp of last move                     |
| `turns`           | Total number of turns in the game          |
| `victory_status`  | How the game ended (mate, resign, etc.)    |
| `winner`          | Outcome — white, black, or draw            |
| `increment_code`  | Time control (e.g., `15+2`)                |
| `white_id`        | Username of white player                   |
| `white_rating`    | Elo rating of white player                 |
| `black_id`        | Username of black player                   |
| `black_rating`    | Elo rating of black player                 |
| `moves`           | Full move sequence (PGN)                   |
| `opening_eco`     | ECO code of the opening (e.g., `B00`)      |
| `opening_name`    | Name of the opening played                 |
| `opening_ply`     | Number of plies in the opening phase       |

---

## Project Structure

```
MODELS/Chess/
├── Chess.ipynb        # Main Jupyter notebook with full analysis
├── games.csv          # Dataset
└── README.md          # This file
```

---

## Installation & Setup

### Prerequisites

- Python 3.10+
- pip

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Run the Notebook

Open `Chess.ipynb` in Jupyter Notebook or VS Code and execute all cells sequentially.

---

## Workflow & Methodology

### 1. Data Loading & Exploration

- Loaded `games.csv` using Pandas.
- Inspected the dataset with `df.head()`, `df.tail()`, `df.info()`, and `df.describe()`.
- Identified column data types — categorical (`object`) vs numerical columns.

### 2. Data Cleaning & Preprocessing

**Dropped irrelevant columns** that do not contribute to prediction or would cause data leakage:

| Dropped Column     | Reason                                    |
| ------------------ | ----------------------------------------- |
| `id`               | Unique identifier — no predictive value   |
| `created_at`       | Timestamp — not useful as raw value       |
| `last_move_at`     | Timestamp — not useful as raw value       |
| `white_id`         | Player identity — would overfit           |
| `black_id`         | Player identity — would overfit           |
| `moves`            | Raw move text — requires NLP processing   |
| `victory_status`   | Leaks outcome information                 |
| `opening_name`     | High cardinality — replaced by ECO family |

**Encoded categorical variables:**

| Feature     | Encoding                                              |
| ----------- | ----------------------------------------------------- |
| `winner`    | white → 0, black → 1, draw → 2                       |
| `rated`     | True → 1, False → 0                                  |
| `eco_family`| A → 0, B → 1, C → 2, D → 3, E → 4                   |

**Removed draw games** (`winner == 2`) to simplify to binary classification, then reset the index.

### 3. Feature Engineering

| New Feature      | Derivation                                             |
| ---------------- | ------------------------------------------------------ |
| `rating_diff`    | `white_rating - black_rating`                          |
| `base_time`      | Extracted from `increment_code` (before `+`)           |
| `increment`      | Extracted from `increment_code` (after `+`)            |
| `eco_family`     | First letter of `opening_eco` (A–E)                    |

After engineering, the `increment_code` and `opening_eco` columns were dropped.

### Final Feature Set (Model 1 — Logistic Regression)

| Feature         | Type    |
| --------------- | ------- |
| `rated`         | Binary  |
| `turns`         | Integer |
| `white_rating`  | Integer |
| `black_rating`  | Integer |
| `opening_ply`   | Integer |
| `rating_diff`   | Integer |
| `base_time`     | Integer |
| `increment`     | Integer |
| `eco_family`    | Integer |

### Reduced Feature Set (Model 2 — Random Forest)

After analyzing Logistic Regression feature importances, `white_rating` and `black_rating` were dropped (their information is captured by `rating_diff`), leaving **7 features**.

### 4. Train-Test Split

- **Split ratio:** 80% training / 20% testing
- **Random state:** 42 (for reproducibility)
- **Stratified** on the target variable `y` to preserve class balance in both sets.

### 5. Feature Scaling

- Applied `StandardScaler` (zero mean, unit variance) to training and test sets.
- `fit_transform()` on training data; `transform()` on test data to prevent data leakage.
- Scaling was used for Logistic Regression. Random Forest was trained on unscaled data (tree-based models are scale-invariant).

### 6. Model Training & Evaluation

#### Model 1: Logistic Regression

```python
LogisticRegression(max_iter=1000)
```

- Trained on the **full 9-feature** scaled dataset.
- Evaluated with accuracy, classification report, and confusion matrix.

#### Model 2: Logistic Regression (Reduced Features)

- Trained on **7 features** (after dropping `white_rating` and `black_rating`).
- Same parameters and evaluation pipeline.

#### Model 3: Random Forest Classifier

```python
RandomForestClassifier(n_estimators=300, max_depth=None, random_state=42, n_jobs=-1)
```

- Trained on the **7-feature unscaled** dataset.
- 300 decision trees with no depth limit.
- Parallelized across all CPU cores (`n_jobs=-1`).

### 7. Feature Importance Analysis

#### Logistic Regression

- Used **absolute coefficient values** (`|coef_|`) as a proxy for feature importance.
- Plotted as a bar chart showing percentage contribution of each feature.

#### Random Forest

- Used built-in **`feature_importances_`** (mean decrease in impurity).
- Plotted as a bar chart for comparison.

### 8. Model Comparison

| Model                               | Features | Accuracy | CV Accuracy (5-fold) |
| ----------------------------------- | -------- | -------- | -------------------- |
| Naive Baseline (majority class)     | —        | ~54.0%   | —                    |
| Logistic Regression (full)          | 9        | ~64.6%   | —                    |
| Logistic Regression (reduced)       | 7        | ~64.6%   | —                    |
| Random Forest (300 trees)           | 7        | ~69.8%   | ~69.15%              |

> **Note:** Exact accuracy values depend on the dataset split and execution. Run the notebook to see precise metrics.

---

## Results

### Baseline Comparison

A naive baseline model predicting the majority class achieves ~54% accuracy. Random Forest improves baseline performance by ~15.8 percentage points, demonstrating that the model captures meaningful signal from rating difference and game metadata.

### Cross-Validation (Random Forest)

To validate model robustness beyond a single train-test split, 5-fold cross-validation was performed:

```
CV Accuracy: 69.15%
```

The CV score closely matches the test set accuracy (~69.8%), confirming that the model generalizes well and is not overfitting to the particular split.

### Sensitivity Analysis

When `rating_diff` was removed from the feature set, model accuracy dropped significantly, confirming that skill disparity between players explains the majority of outcome variance. This validates the feature engineering decision and highlights that Elo rating gap is the primary driver of prediction.

### Classification Metrics (Logistic Regression)

- **Accuracy:** ~64.6%
- **Precision / Recall / F1-Score:** Roughly balanced across both classes (white win vs. black win).
- Confusion matrix shows moderate overlap between classes, but the model captures meaningful signal from rating differences and game metadata.

### Classification Metrics (Random Forest)

- **Accuracy:** ~69.8%
- Notable improvement over Logistic Regression (+5.2 percentage points).
- Random Forest captures non-linear relationships and feature interactions that the linear model misses.

### Feature Importance Highlights

**Logistic Regression (top features by coefficient magnitude):**

| Rank | Feature       | Insight                                    |
| ---- | ------------- | ------------------------------------------ |
| 1    | `rating_diff` | Strongest predictor — higher-rated player wins more often |
| 2    | `turns`       | Game length correlates with outcomes       |
| 3    | `opening_ply` | Opening depth has moderate influence       |

**Random Forest (top features by impurity decrease):**

| Rank | Feature       | Insight                                    |
| ---- | ------------- | ------------------------------------------ |
| 1    | `rating_diff` | Dominant feature                           |
| 2    | `turns`       | Important non-linear signal                |
| 3    | `opening_ply` | Consistent across both models              |

---

## Visualizations

The notebook includes the following visualizations:

1. **Winner Distribution Bar Chart** — Percentage of games won by white, black, and draw.
2. **Confusion Matrix (Logistic Regression)** — Heatmap of true vs. predicted labels.
3. **Logistic Regression Feature Importance** — Bar chart of absolute coefficient percentages.
4. **Confusion Matrix (Random Forest)** — Heatmap of true vs. predicted labels.
5. **Random Forest Feature Importance** — Bar chart of impurity-based importance scores.

---

## Key Findings

1. **Rating difference is the single most important predictor** of game outcome across both models.
2. **White has a slight advantage** (~50–52% win rate vs. ~45–47% for black), consistent with known chess statistics.
3. **Random Forest outperforms Logistic Regression** (~69.8% vs. ~64.6%), showing that non-linear feature interactions improve prediction from game metadata.
4. **Removing `white_rating` and `black_rating`** (while keeping `rating_diff`) did not significantly hurt performance, confirming that the difference captures the essential information.
5. **Draws are hard to model** — they were excluded from the binary classification task.
6. **Tree-based models provide measurable gains** (+5.2%) by capturing non-linear feature interactions that linear models cannot represent.

---

## Technologies Used

| Tool / Library     | Purpose                                |
| ------------------ | -------------------------------------- |
| Python 3.10+       | Programming language                   |
| Pandas             | Data manipulation and analysis         |
| NumPy              | Numerical computations                 |
| Matplotlib         | Data visualization                     |
| Seaborn            | Statistical visualization (heatmaps)  |
| Scikit-learn       | Machine learning models and utilities  |
| Jupyter Notebook   | Interactive development environment    |

---

## Future Improvements

- **Add more features:** Extract features from move sequences (e.g., average centipawn loss, blunders) using a chess engine.
- **Try advanced models:** Gradient Boosting (XGBoost, LightGBM), Neural Networks.
- **Hyperparameter tuning:** Use GridSearchCV or RandomizedSearchCV for optimal parameters.
- **~~Cross-validation:~~** ✅ Implemented — 5-fold CV confirms ~69.15% accuracy.
- **Include draws:** Frame as a 3-class problem or use ordinal regression.
- **Time-series features:** Leverage timestamps for player form / momentum analysis.
- **Handle class imbalance:** Apply SMOTE or class weighting if imbalance is significant.

---

## License

This project is for educational purposes.

---

*Built with Python, Scikit-learn, and curiosity about chess.*
