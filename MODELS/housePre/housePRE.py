import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Set backend for non-GUI environments
matplotlib.use('Agg')

# 1. Load Data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, '..', '..', 'data', 'Housing.csv')

print(f"Loading data from: {csv_path}")
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    df = pd.read_csv('Housing.csv')

print(f"Original shape: {df.shape}")

# 2. Preprocessing & Cleaning
# Remove 'rownames' or 'id' columns if they exist (Noise)
if 'rownames' in df.columns:
    print("Dropping 'rownames' column...")
    df = df.drop('rownames', axis=1)

# Encode Categorical Data
# We manually specify binary columns to ensure correct encoding (1=yes, 0=no)
binary_cols = ['driveway', 'recroom', 'fullbase', 'gashw', 'airco', 'prefarea']
le = LabelEncoder()

# Check if columns exist before encoding
for col in binary_cols:
    if col in df.columns:
        df[col] = le.fit_transform(df[col])

# 3. Advanced Feature Engineering
# Improvement A: Log-transform 'lotsize' (Diminishing returns on land size)
if 'lotsize' in df.columns:
    df['log_lotsize'] = np.log1p(df['lotsize'])
    # Interaction features before dropping lotsize
    if 'bedrooms' in df.columns:
        df['size_per_bedroom'] = df['lotsize'] / df['bedrooms']
    
    df = df.drop('lotsize', axis=1) # Remove original to prevent multicollinearity

# Improvement B: Create a 'Luxury Score'
# Summing up high-value amenities to give the model a clear signal of "quality"
df['luxury_score'] = (
    df['bathrms'] * 2 +  # Bathrooms are high value
    df['airco'] * 1.5 + 
    df['prefarea'] * 1.5 +
    df['recroom'] + 
    df['fullbase']
)

# New Interactions
if 'bedrooms' in df.columns and 'bathrms' in df.columns:
    df['bath_bed_ratio'] = df['bathrms'] / df['bedrooms']

# Target Transformation: Log-transform Price
# (Standard practice for money values to handle skewness)
X = df.drop('price', axis=1)
Y = np.log1p(df['price'])

print(f"Features used: {X.columns.tolist()}")

# 4. Data Splitting
X_train, X_test, Y_train_log, Y_test_log = train_test_split(X, Y, test_size=0.2, random_state=42, shuffle=True)

# 5. Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- MODEL: Tuned Gradient Boosting ---
print("\n=== Model: Tuned Gradient Boosting Regressor ===")
# Optimization Strategy: Low learning rate + High estimators = Better Generalization
gb_model = GradientBoostingRegressor(
    n_estimators=2000,     # Increased from 1000
    learning_rate=0.01,    # Decreased from 0.05 (learns slower and more carefully)
    max_depth=4,           # Sligthly deeper to capture more patterns
    subsample=0.8,         # Use 80% of data per tree
    min_samples_leaf=5,    # Reduced to allow finer splits
    random_state=42
)

gb_model.fit(X_train_scaled, Y_train_log)

# Training Performance check
y_train_pred_log = gb_model.predict(X_train_scaled)
Y_train_actual = np.expm1(Y_train_log)
y_train_pred_actual = np.expm1(y_train_pred_log)
train_r2 = r2_score(Y_train_actual, y_train_pred_actual)
print(f"Training R2 Score: {train_r2:.4f}")

y_pred_log = gb_model.predict(X_test_scaled)

# 6. Inverse Transform Results
Y_test_actual = np.expm1(Y_test_log)
y_pred_actual = np.expm1(y_pred_log)

# Metrics
r2 = r2_score(Y_test_actual, y_pred_actual)
mae = mean_absolute_error(Y_test_actual, y_pred_actual)
rmse = mean_squared_error(Y_test_actual, y_pred_actual) ** 0.5

print(f"R2 Score: {r2:.4f}")
print(f"MAE: ${mae:.2f}")
print(f"RMSE: ${rmse:.2f}")

# Performance Check
if r2 > 0.65:
    print("✓ Significant Improvement: Model is stable.")
elif r2 > 0.6:
    print("✓ Moderate Improvement.")
else:
    print("⚠ Data Limitation: The dataset might lack critical features (like location/year built).")

# 7. Visualization
fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(Y_test_actual, y_pred_actual, alpha=0.6, color='#8e44ad', edgecolors='w', s=60, label='Predicted vs Actual')
min_val = min(Y_test_actual.min(), y_pred_actual.min())
max_val = max(Y_test_actual.max(), y_pred_actual.max())
ax.plot([min_val, max_val], [min_val, max_val], 'k--', lw=2, label='Perfect Fit')

ax.set_xlabel('Actual Price ($)')
ax.set_ylabel('Predicted Price ($)')
ax.set_title(f'Optimized Gradient Boosting\nR2: {r2:.3f} | MAE: ${mae:.0f}')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("enhanced_model_results.png", dpi=150)
print("\n✓ Visualization saved as enhanced_model_results.png")

# 8. Feature Importance
importances = gb_model.feature_importances_
indices = np.argsort(importances)[::-1]
print("\n=== Top 5 Drivers of Price (Enhanced) ===")
for i in range(min(5, len(indices))):
    print(f"{i+1}. {X.columns[indices[i]]}: {importances[indices[i]]:.4f}")