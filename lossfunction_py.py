# -*- coding: utf-8 -*-
"""lossfunction.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j_zUaj3W21rXhp2lTbN0TYFVRoTiuvTr
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define true values (y_true) and model predictions (y_pred)
# For MSE (Regression)
y_true_mse = np.array([3.0, 5.0, 2.5, 7.0, 6.5])
y_pred_mse_1 = np.array([2.8, 5.2, 2.7, 6.8, 6.2])  # Slight deviation
y_pred_mse_2 = np.array([3.5, 5.5, 3.0, 7.5, 7.0])  # More deviation

# For CCE (Classification - One-hot encoded)
y_true_cce = np.array([[0, 1, 0], [1, 0, 0]])  # True labels
y_pred_cce_1 = np.array([[0.1, 0.8, 0.1], [0.7, 0.2, 0.1]])  # Close to correct
y_pred_cce_2 = np.array([[0.3, 0.6, 0.1], [0.6, 0.3, 0.1]])  # More deviation

# Step 2: Compute Mean Squared Error (MSE) Loss
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

mse_loss_1 = mean_squared_error(y_true_mse, y_pred_mse_1)
mse_loss_2 = mean_squared_error(y_true_mse, y_pred_mse_2)

# Step 3: Compute Categorical Cross-Entropy (CCE) Loss
def categorical_cross_entropy(y_true, y_pred):
    y_pred = np.clip(y_pred, 1e-9, 1.0)  # Avoid log(0)
    return -np.sum(y_true * np.log(y_pred)) / y_true.shape[0]

cce_loss_1 = categorical_cross_entropy(y_true_cce, y_pred_cce_1)
cce_loss_2 = categorical_cross_entropy(y_true_cce, y_pred_cce_2)

# Print loss values
print(f"MSE Loss (Prediction 1): {mse_loss_1:.4f}")
print(f"MSE Loss (Prediction 2 - Modified): {mse_loss_2:.4f}")
print(f"Categorical Cross-Entropy Loss (Prediction 1): {cce_loss_1:.4f}")
print(f"Categorical Cross-Entropy Loss (Prediction 2 - Modified): {cce_loss_2:.4f}")

# Step 4: Plot loss function values using Matplotlib
loss_labels = ["MSE (Pred 1)", "MSE (Pred 2)", "CCE (Pred 1)", "CCE (Pred 2)"]
loss_values = [mse_loss_1, mse_loss_2, cce_loss_1, cce_loss_2]

plt.figure(figsize=(8, 5))
plt.bar(loss_labels, loss_values, color=['blue', 'cyan', 'red', 'orange'])
plt.xlabel("Loss Types")
plt.ylabel("Loss Value")
plt.title("Comparison of MSE and Categorical Cross-Entropy Loss")
plt.show()