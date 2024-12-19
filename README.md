# Exponentially Weighted Averages (EWA) Visualization

This repository demonstrates the concept of **Exponentially Weighted Averages (EWA)**, a fundamental mathematical technique widely used in deep learning for smoothing noisy data and tracking trends over time. 

The code simulates noisy data, applies EWA to smooth the data, and visualizes the results using `matplotlib`.

---

## 🧪 Key Features

- **Simulated Data:** Generates noisy data using a sine function with added random noise.
- **EWA Smoothing:** Implements EWA to reduce noise and track trends.
- **Visualization:** Plots both the original noisy data and the smoothed data for comparison.

---

## 📂 Repository Structure


---

## 📊 Exponentially Weighted Averages (EWA) Formula

The EWA is calculated using the formula:
\[
v_t = \beta v_{t-1} + (1 - \beta) \theta_t
\]

Where:
- \( v_t \): Exponentially Weighted Average at time \( t \)
- \( \beta \): Smoothing factor (0 < \( \beta \) < 1)
- \( \theta_t \): Current observation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Required Libraries:
  - `numpy`
  - `matplotlib`


