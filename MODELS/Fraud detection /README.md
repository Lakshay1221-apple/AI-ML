# Credit Card Fraud Detection using Machine Learning

## Overview

Credit card fraud detection is the process of identifying and preventing unauthorized or deceptive transactions. It is a critical component of financial security, protecting consumers and institutions from significant financial losses while maintaining trust in digital payment systems. This project develops a robust machine learning pipeline designed to distinguish inherently rare fraudulent transactions from millions of legitimate ones, demonstrating an end-to-end approach to a complex, real-world data science problem.

## Problem Statement

Credit card fraud detection presents a classical anomaly detection challenge characterized by highly imbalanced data. In a typical financial environment, fraudulent activities represent a microscopic fraction of overall transaction volume. Building an effective model requires not only identifying these rare fraudulent transactions but also doing so with high precision to avoid continuously flagging legitimate behavior, which degrades the user experience.

## Dataset

This project utilizes a large-scale dataset containing approximately 1.2 million credit card transactions. 

* **Size:** ~1.2M transactions
* **Features:** The dataset comprises standard transaction details (such as the transaction amount and timestamp) alongside various features resulting from principal component analysis, ensuring user privacy while retaining critical variance for predictive modeling.

## Approach

### Data Processing

* **Cleaning:** Standardized data formats, removed duplicated entries, and addressed inconsistent data structures to prepare a reliable foundation for modeling.
* **Handling Missing Values:** Imputed critical missing values using statistically sound techniques to ensure data integrity without introducing artificial bias.
* **Feature Selection:** Systematically removed highly correlated or low-variance features to streamline the model, reduce noise, and improve computational efficiency.

### Feature Engineering

* **Time-based Features:** Extracted specific temporal elements, such as the hour of the day or day of the week, to capture periodic patterns corresponding to fraudulent activity.
* **Behavioral Features:** Engineered derived features directly comparing a transaction against historical user behavior, specifically metrics like `user_avg_amt` and `amt_vs_avg_past`.
* **Distance Calculation:** Utilized the Haversine formula to approximate the geographical distance between consecutive transaction locations as an indicator of compromised card present activities.
* **Transaction Velocity:** Calculated the time difference (`time_diff`) between sequential transactions to flag unusually rapid purchasing patterns common in fraud scenarios.

### Handling Imbalance

* **Class Weighting:** Specifically addressed the severe class imbalance at the algorithm level by utilizing `class_weight='balanced'`. This technique penalizes the misclassification of the minority (fraud) class more heavily than the majority (legitimate) class during the training process.

## Model

* **Algorithm:** Random Forest Classifier
* **Rationale:** Random Forest was chosen for its strong performance on tabular data, inherent resistance to overfitting through ensemble learning, and its ability to capture complex, non-linear relationships. Crucially, it provides clear feature importance metrics, allowing for the explainability required in financial compliance.

## Evaluation Strategy

* **Validation:** Implemented a rigorous, time-based train-test split to respect the chronological nature of transactional data and simulate real-world model deployment conditions. 
* **Metrics:** Evaluated model efficacy utilizing metrics robust to class imbalance, specifically:
  * Precision
  * Recall
  * F1-score

## Threshold Optimization

The default classification threshold (typically 0.5) is often sub-optimal for heavily skewed datasets, as it naturally favors predicting the majority class. By systematically analyzing the Precision-Recall curve and fine-tuning the decision threshold, the model's sensitivity (Recall) was significantly improved. This optimization ensured the model successfully captured a higher percentage of true fraudulent transactions without unacceptable degradation to the false positive rate.

## Results

The optimized model yielded strong, practical performance on the holdout test set:

* **Precision:** ~0.94
* **Recall:** ~0.81
* **Key Insight:** The combination of targeted feature engineering, algorithmic class balancing, and bespoke threshold tuning significantly improved the overall fraud detection capability.

## Feature Importance

Analysis of the Random Forest model revealed the most critical predictors of fraud within this dataset:

* `amt` (Transaction amount)
* `amt_vs_avg_past` (Amount relative to user history)
* `hour` (Time of day)
* `time_diff` (Velocity between transactions)

## Key Insights

* Fraudulent activity is heavily predicated on deviations in user behavior rather than underlying demographic information.
* Unusual transaction characteristics, such as amounts significantly higher than a user's average or highly rapid consecutive transactions, serve as the highest-signal indicators of potential fraud.

## Future Improvements

* **Advanced Algorithms:** Transitioning to gradient boosting frameworks, such as XGBoost or LightGBM, to further enhance predictive performance and execution speed.
* **Real-time Deployment:** Developing an API to deploy the model for streaming data, allowing for the evaluation and flagging of transactions in real-time.
* **Advanced Feature Engineering:** Incorporating external data sources and exploring network analysis techniques to identify complex, coordinated fraud rings.

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

## How to Run

1. Clone the repository to your local environment.
2. Install the required project dependencies.
3. Open and run the `fraudd.ipynb` Jupyter Notebook sequentially to reproduce the data processing, model training, and evaluation steps.
