import numpy as np
import matplotlib.pyplot as plt

# Simulated data
data = [np.sin(x / 10) + np.random.randn() * 0.2 for x in range(100)]

# Exponentially Weighted Average
beta = 0.9
v = 0
ewa = []

for theta in data:
    v = beta * v + (1 - beta) * theta
    ewa.append(v)


print(data)
print(ewa)
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data, label='Original Data', alpha=0.5)
plt.plot(ewa, label='Exponentially Weighted Average', color='red')
plt.legend()
plt.title("Exponentially Weighted Averages")
plt.show()
