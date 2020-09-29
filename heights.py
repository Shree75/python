import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

print("Mean height: ", heights.mean())
print("standard Deviation: ", heights.std())
print("Maximum Height: ", heights.max())
print("Minimum height: ", heights.min())

plt.hist(heights)
plt.title("height Distribution of US Presidents")
plt.xlabel('height(cm)')
plt.ylabel('number')