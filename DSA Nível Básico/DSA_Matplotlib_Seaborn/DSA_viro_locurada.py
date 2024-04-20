import numpy as np
import random
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import seaborn as sea

np.random.seed(42)
n = 1000

issmoker = np.random.rand(n) < 0.2
age = np.random.normal(40, 10, n)
height = np.random.normal(170, 10, n)
weight = np.random.normal(70, 10, n)

datas = pd.DataFrame({'Height': height, 'Weight': weight, 'Is Smoker': issmoker})

datas['Is Smoker'] = datas['Is Smoker'].map({True: 'Smoker', False: 'Non-Smoker'})

sea.set(style = 'ticks')

sea.lmplot(x = 'Height',
           y = 'Weight',
           data = datas,
           hue = 'Is Smoker',
           palette = ['tab:blue', 'tab:orange'],
           height = 7
           )

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height and weight ratio of smokers and non-smokers')

sea.despine()

plt.show()