import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
import os
import time

# 1. Load Data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, '..', '..', 'data', 'Housing.csv')

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    df = pd.read_csv('Housing.csv')

# 2. Preprocessing
if 'rownames' in df.columns:
    df = df.drop('rownames', axis=1)

binary_cols = ['driveway', 'recroom', 'fullbase', 'gashw', 'airco', 'prefarea']
for col in binary_cols:
    if col in df.columns:
        df[col] = df[col].map({'yes': 1, 'no': 0}).astype('int8')

# Feature Engineering (float32 for GPU efficiency)
df['log_lotsize'] = np.log1p(df['lotsize']).astype('float32')

df['luxury_score'] = (
    df['bathrms'] * 2 +
    df['airco'] * 1.5 +
    df['prefarea'] * 1.5 +
    df['recroom'] +
    df['fullbase']
).astype('float32')

df['size_per_bedroom'] = (df['lotsize'] / df['bedrooms']).astype('float32')
df['bath_bed_ratio'] = (df['bathrms'] / df['bedrooms']).astype('float32')

X = df.drop('price', axis=1).astype('float32')
Y = np.log1p(df['price']).astype('float32')

# 3. Split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# 4. Hyperparameter Grid
param_grid = {
    'n_estimators': [800, 1200],
    'learning_rate': [0.03, 0.05],
    'max_depth': [3, 4, 5],
    'subsample': [0.8],
    'colsample_bytree': [0.8],
    'min_child_weight': [1, 3]
}

print("Starting GPU Training...")
start_time = time.time()

# 5. GPU-Optimized XGBoost
gb = XGBRegressor(
    random_state=42,
    device="cuda",
    tree_method="hist",
    predictor="gpu_predictor",
    eval_metric="rmse",
    verbosity=1
)

# n_jobs=1 avoids CPU thread contention; GPU does the heavy work
grid = GridSearchCV(
    gb,
    param_grid,
    cv=5,
    scoring='r2',
    n_jobs=1,
    verbose=2
)

grid.fit(X_train, Y_train)

end_time = time.time()

print(f"\nTraining Complete in: {end_time - start_time:.2f} seconds")
print(f"Best params: {grid.best_params_}")

# 6. Evaluation
best_gb = grid.best_estimator_
preds_log = best_gb.predict(X_test)

Y_test_act = np.expm1(Y_test)
preds_act = np.expm1(preds_log)

r2 = r2_score(Y_test_act, preds_act)
print(f"Best GB R2 Score: {r2:.4f}")
print(f"Best GB RMSE: {np.sqrt(np.mean((Y_test_act - preds_act) ** 2)):.2f}")# 7. Results