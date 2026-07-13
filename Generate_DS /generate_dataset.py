import pandas as pd
import numpy as np

np.random.seed(42)
num_samples = 6000

data = []

for _ in range(num_samples):

    label = np.random.choice([0, 1, 2], p=[0.5, 0.3, 0.2])

    if label == 0:      # Normal
        temp   = np.random.uniform(25, 35)  # DHT11 real range
        vib    = 0                           # SW420: No vibration (digital)
        carbon = np.random.uniform(10, 30)

    elif label == 1:    # Warning
        temp   = np.random.uniform(38, 45)  # DHT11 real range
        vib    = 1                           # SW420: Vibration detected (digital)
        carbon = np.random.uniform(35, 55)

    else:               # Critical / Failure
        temp   = np.random.uniform(47, 50)  # DHT11 max range
        vib    = 1                           # SW420: Vibration detected (digital)
        carbon = np.random.uniform(60, 100)

    data.append([temp, vib, carbon, label])

df = pd.DataFrame(data, columns=["Temp", "Vibration", "Carbon", "Label"])
df.to_csv("dataset.csv", index=False)

print("Dataset created successfully!")
