import numpy as np
import pandas as pd

arr = np.random.randint(1, 100, 10)
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
series = pd.Series(arr, index=labels)
print(series)